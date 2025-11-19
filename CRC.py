import random
import math
import csv
import time
import os
from enum import Enum

# 4비트 마다 _ 삽입 함수 #################
def binForm(num, length = 0):
    binary = bin(num)[2:]
    reversed_binary = binary[::-1]
    grouped = '_'.join([reversed_binary[i:i+4] for i in range(0, len(reversed_binary), 4)])
    return grouped[::-1]

######################################

class CRC_TYPE(Enum):
    CRC8  = (8,  0b1_0000_0111)
    CRC10 = (10, 0b110_0011_0101)
    CRC16 = (16, 0b1_0001_0000_0010_0001)
    CRC32 = (32, 0b1_0000_0100_1100_0001_0001_1101_1011_0111)

def generateDataWord(length):
    data_word = random.getrandbits(length)

    # FIXME: 디버그용 출력문 - binForm으로 포맷
    # print(f"[Debug] dataWord: {binForm(dataWord)}")

    return data_word

def _makeerror_pattern(length, errorRate):
    # 에러 비트 개수
    numErrors = math.ceil(length * (errorRate * 0.01))

    if numErrors == 0: return 0 # 에러 없음-빠른 종료
    
    errorIndices = random.sample(range(length), numErrors)
    error_pattern = 0
    for index in errorIndices:
        error_pattern = error_pattern | (1 << index)

    return error_pattern

def __generateErrorData(length, errorRate):
    dataWord = generateDataWord(length)
    error_pattern = _makeerror_pattern(length, errorRate)
    errorData = dataWord ^ error_pattern

    # FIXME: 디버그용 출력문 - binForm으로 포맷
    # print(f"[Debug] Data Word: \t{binForm(dataWord)}")
    # print(f"[Debug] Error Pattern: \t{binForm(error_pattern)}")
    # print(f"[Debug] Error Data: \t{binForm(errorData)}")
    return errorData

def calculateCRC(CRCType: CRC_TYPE, dataWord):
    crcBitNum, polynomial = CRCType.value
    dividend = (dataWord << crcBitNum)
    dividend_debug = (dataWord << crcBitNum) # FIXME: 디버그용
    current_len = dividend.bit_length()
    
    for i in range(current_len, crcBitNum, -1):
        # 현재 비트가 1일 경우 나누기 수행
        if (dividend >> (i - 1) & 1):
            shift_amount = (i - 1) - crcBitNum
            dividend ^= (polynomial << shift_amount)

    mask = (1 << crcBitNum) - 1  # 예: CRC-8이면 0xFF (11111111)
    crc = dividend & mask
    
    # FIXME: 디버그용 출력문 - binForm으로 포맷
    # print(f"[Debug] CRC Bit Num: {crcBitNum}, Polynomial: {binForm(polynomial)}")
    # print(f"[Debug] Initial Data Word : {binForm(dataWord)}")
    # print(f"[Debug] Data Word shifted: {binForm(dividend_debug)}")
    # print(f"[Debug] CRC length: {crc.bit_length()}")
    # print(f"[Debug] CRC: {binForm(crc)}")
    
    return crc

def makecode_word(CRCType: CRC_TYPE, dataWord, crc):
    shift_amount, _ = CRCType.value
    return dataWord << shift_amount | crc


def runSimulation(crc_type: CRC_TYPE, data_word_length: int, error_rate: int, run_num = 4096):

    crc_bit_num, _ = crc_type.value
    code_word_length = data_word_length + crc_bit_num

    results = [] 
    detection_count = 0
    total_time = 0

    num_errors_injected = run_num if error_rate > 0 else 0

    for k in range(run_num):
        # Sender
        data_word = generateDataWord(data_word_length)
        
        start_time = time.perf_counter() # 타이머 시작
        code_word = makecode_word(crc_type, data_word, calculateCRC(crc_type, data_word))

        # Error Injection
        error_pattern = _makeerror_pattern(code_word.bit_length(), error_rate)
        error_data = code_word ^ error_pattern

        # Receiver
        syndrome = calculateCRC(crc_type, error_data)
        end_time = time.perf_counter() # 타이머 종료

        # 통계 계산
        is_error_injected = (error_pattern != 0)
        is_error_detected = (syndrome != 0)

        if is_error_injected and is_error_detected:
            detection_count += 1

        delay = end_time - start_time
        total_time += delay

        # CSV 저장용 데이터
        results.append({
            'DataWord': data_word,
            'CodeWord': code_word,
            'ErrorPattern': error_pattern,
            'Syndrome': syndrome,
            'Delay_s': delay,
            'ErrorInjected': is_error_injected,
            'ErrorDetected': is_error_detected
        })

    detection_rate_pct = (detection_count / num_errors_injected) * 100 if num_errors_injected > 0 else 0.0
    avg_delay_ms = (total_time / run_num) * 1000

    # CSV 파일 저장 (result_csv 디렉터리로 이동)
    filename = f"{crc_type.name}_Data{data_word_length}bit_Error{error_rate}pct.csv"
    out_dir = 'result_csv'
    os.makedirs(out_dir, exist_ok=True)
    filepath = os.path.join(out_dir, filename)
    
    fieldnames = results[0].keys()
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in results:
            csv_row = {
                'DataWord': binForm(row['DataWord'], data_word_length),
                'CodeWord': binForm(row['CodeWord'], code_word_length),
                'ErrorPattern': binForm(row['ErrorPattern'], code_word_length),
                'Syndrome': binForm(row['Syndrome'], crc_bit_num),
                'Delay_s': f"{row['Delay_s']:.9f}",
                'ErrorInjected': row['ErrorInjected'],
                'ErrorDetected': row['ErrorDetected']
            }
            writer.writerow(csv_row)

    print(f"✅ Simulation Complete. Results saved to {filepath}")
    
    return {
        'CRC': crc_type.name,
        'DataLength': data_word_length,
        'ErrorPercent': error_rate,
        'ErrorDetectionRate_%': f"{detection_rate_pct:.4f}",
        'AverageDelay_ms': f"{avg_delay_ms:.6f}"
    }


def main():
    # 1. 과제에 제시된 파라미터 조합 정의
    parameters = [
        # (1) CRC-8
        (CRC_TYPE.CRC8, 16), (CRC_TYPE.CRC8, 32), (CRC_TYPE.CRC8, 64), (CRC_TYPE.CRC8, 128),
        # (2) CRC-10
        (CRC_TYPE.CRC10, 32), (CRC_TYPE.CRC10, 64), (CRC_TYPE.CRC10, 128), (CRC_TYPE.CRC10, 256),
        # (3) CRC-16
        (CRC_TYPE.CRC16, 32), (CRC_TYPE.CRC16, 64), (CRC_TYPE.CRC16, 128), (CRC_TYPE.CRC16, 256),
        # (4) CRC-32
        (CRC_TYPE.CRC32, 64), (CRC_TYPE.CRC32, 128), (CRC_TYPE.CRC32, 256), (CRC_TYPE.CRC32, 512),
    ]
    error_rates = [0, 1, 10, 20, 50]
    report_stats = []

    # 시뮬레이션 조건
    for crc_type, data_word_length in parameters:
        for error_rate in error_rates:

            print(f"\n[RUN]: {crc_type.name} / Data:{data_word_length}bit / Error:{error_rate}%")
            stats = runSimulation(crc_type, data_word_length, error_rate)
            report_stats.append(stats)

    print("\n--- All Simulations Complete ---")

    # 최종 통계 요약 저장
    summary_dir = 'result_csv'
    os.makedirs(summary_dir, exist_ok=True)
    summary_filename = "Summary_Report_Statistics.csv"
    summary_path = os.path.join(summary_dir, summary_filename)
    fieldnames = report_stats[0].keys()
    with open(summary_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_stats)
        
    print(f"\nFinal statistics summary saved to {summary_path}")



# print("\n----- CRC Simulation Test -----")

if __name__ == "__main__":
    main()

# print("--------------------------------\n")