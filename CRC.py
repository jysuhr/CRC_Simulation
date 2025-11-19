import random
import math
from enum import Enum

# TODO: 디버깅용 함수 - 제거 필요 ###################
def binForm(num):
    binary = bin(num)[2:]
    reversed_binary = binary[::-1]
    grouped = '_'.join([reversed_binary[i:i+4] for i in range(0, len(reversed_binary), 4)])
    return grouped[::-1]

################################################

class CRC_TYPE(Enum):
    CRC2 = (2, 0b101) # TODO: 제거하기
    CRC8  = (8,  0b1_0000_0111)
    CRC10 = (10, 0b110_0011_0101)
    CRC16 = (16, 0b1_0001_0000_0010_0001)
    CRC32 = (32, 0b1_0000_0100_1100_0001_0001_1101_1011_0111)

def makeDataWord(length):
    dataWord = random.getrandbits(length)

    # FIXME: 디버그용 출력문 - binForm으로 포맷
    print(f"dataWord: {binForm(dataWord)}")

    return dataWord

def makeErrorPattern(length, errorPercentage):
    # 에러 비트 개수
    numErrors = math.ceil(length * (errorPercentage * 0.01))

    if numErrors == 0: return 0 # 에러 없음-빠른 종료
    
    errorIndices = random.sample(range(length), numErrors)
    errorPattern = 0
    for index in errorIndices:
        errorPattern = errorPattern | (1 << index)

    return errorPattern

def generateErrorData(length, errorPercentage):
    dataWord = makeDataWord(length)
    errorPattern = makeErrorPattern(length, errorPercentage)
    errorData = dataWord ^ errorPattern

    # FIXME: 디버그용 출력문 - binForm으로 포맷
    print(f"Data Word: \t{binForm(dataWord)}")
    print(f"Error Pattern: \t{binForm(errorPattern)}")
    print(f"Error Data: \t{binForm(errorData)}")
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
    print(f"CRC Bit Num: {crcBitNum}, Polynomial: {binForm(polynomial)}")
    print(f"Initial Data Word : {binForm(dataWord)}")
    print(f"Data Word shifted: {binForm(dividend_debug)}")
    print(f"CRC length: {crc.bit_length()}")
    print(f"CRC: {binForm(crc)}")
    
    return crc

def makeCodeWord(CRCType: CRC_TYPE, dataWord, crc):
    shift_amount, _ = CRCType.value
    return dataWord << shift_amount | crc


# Test
print("\n----- CRC Simulation Test -----")
# generateErrorData(16, 10)
# calculateCRC(CRC_TYPE.CRC8, makeDataWord(8))

# dataWord = makeDataWord(8)
dataWord = 0b1110
type = CRC_TYPE.CRC16
codeWord = makeCodeWord(type, dataWord, calculateCRC(type, dataWord))
print(f"CodeWord: {binForm(codeWord)}")

print("--------------------------------\n")
