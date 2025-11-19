# CRC_Simulation

데이터 통신과 네트워크 CRC 구현 과제
<p align="center">
	<a href="https://www.python.org/">
		<img src="https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white" alt="Python" />
	</a>
</p>

## 시뮬레이션 결과 시각화
에러 확률 0, 1, 10, 20, 50의 평균치는 0에서의 Error Detection이 0%이므로 최대 80%입니다.

<img width="800" alt="타입과 길이별 DetectionRate_Barplot" src="https://github.com/user-attachments/assets/6c73a3b7-8fb9-4d40-a372-068dc4f96dc1" />

<img width="500" alt="타입별 평균 errorDetection Rate_Barplot" src="https://github.com/user-attachments/assets/cb0ea734-4ad4-4284-974c-f20371c00ecf" />

<img width="600" alt="타입과 길이별 DetectionRate_Hitmap" src="https://github.com/user-attachments/assets/0d11a10e-571a-44f9-bfed-5ca2193bb673" />

<br>에러 확률 0%를 제외했습니다.<br>
<img width="500" alt="CRC8 에러율별 detection_dotPlot" src="https://github.com/user-attachments/assets/f13db0b1-6afa-4bdf-b758-cc1ab6b43c1e" />
<img width="500" alt="CRC10 에러율별 디텍션" src="https://github.com/user-attachments/assets/9f5b0f3a-7a23-4772-9eaa-7fd8081eed97" />
<img width="500" alt="CRC16 에러율별 디텍션" src="https://github.com/user-attachments/assets/f5e57073-37f8-4d9d-a021-f4c859393260" />
<img width="500" alt="CRC32 에러율별 디텍션" src="https://github.com/user-attachments/assets/93fbffde-cb66-455d-9086-9ecd9ae77768" />


## CRC 규칙

<img src="https://github.com/user-attachments/assets/37b8a013-28de-4753-bd8e-392c9e14063f" width="700px">


(1) CRC-8

Data Word 길이: 16, 32, 64, 128

에러 패턴 중 에러 비트 비율: 0%, 1%, 10%, 20%, 50% (소수점일 경우 올림 연산으로 수행)

(e.g., 0%: 에러가 없음, 50%: code word 길이의 절반에 해당하는 에러 비트가 임의의 위치에서 발생함)

(2) CRC-10

Data Word 길이: 32, 64, 128, 256

에러 패턴 중 에러 비트 비율: 0%, 1%, 10%, 20%, 50% (소수점일 경우 올림 연산으로 수행)

(3) CRC-16

Data Word 길이: 32, 64, 128, 256

에러 패턴 중 에러 비트 비율: 0%, 1%, 10%, 20%, 50% (소수점일 경우 올림 연산으로 수행)

(4) CRC-32

Data Word 길이: 64, 128, 256, 512

에러 패턴 중 에러 비트 비율: 0%, 1%, 10%, 20%, 50% (소수점일 경우 올림 연산으로 수행)

