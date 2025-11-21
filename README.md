# CRC_Simulation

데이터 통신과 네트워크 CRC 구현 과제
<p align="center">
	<a href="https://www.python.org/">
		<img src="https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white" alt="Python" />
	</a>
	<a href="https://colab.research.google.com/">
		<img src="https://img.shields.io/badge/Google_Colab-F9AB00?logo=googlecolab&logoColor=white" alt="Google Colab" />
	</a>
</p>

## 시뮬레이션 결과 시각화
Environment
- Device: MacBook Air (M2, 2022)
- Processor: Apple M2 (8-core CPU, 10-core GPU)
- Memory: 24GB Unified Memory

에러 확률 0%는 평균치 계산에서 제외했습니다.
<img width="800" alt="타입별 디텍션 BarChart_0제외" src="https://github.com/user-attachments/assets/6296aa3b-7863-4cd7-ad64-bc9905f5d714" />

<img width="600" alt="디텍션 hitmap_0제외" src="https://github.com/user-attachments/assets/3f227894-50ac-489b-bfb3-152e42cb5b6f" />

<img width="800" alt="Delay violinChart" src="https://github.com/user-attachments/assets/cfb659d4-fd3a-4e86-af8b-fe4c3656b859" />


<br>에러 확률 0%를 제외했습니다.<br>
<img width="500" alt="CRC8_errorRate별 디텍션" src="https://github.com/user-attachments/assets/f674d1d6-8c5b-4886-962c-575c8368a54e" />
<img width="500" alt="CRC10_errorRate별 디텍션" src="https://github.com/user-attachments/assets/aee11265-4904-4f3e-9451-529f68416b64" />
<img width="500" alt="CRC16_errorRate별 디텍션" src="https://github.com/user-attachments/assets/fc53e6ce-3a44-425a-bd8d-3085018b64b0" />
<img width="500" alt="CRC32_errorRate별 디텍션" src="https://github.com/user-attachments/assets/a4c29e86-b828-44b0-96a5-d05fa216f70c" />

### Trade-off Error detection rate vs Delay
<img width="500" alt="trade-off 16bit" src="https://github.com/user-attachments/assets/37814782-4384-4a0b-9d1b-2ed8dd642664" />
<img width="500" alt="trade-off 32bit" src="https://github.com/user-attachments/assets/a5df933f-b064-4754-8605-3081211f3380" />
<img width="500" alt="trade-off 64bit" src="https://github.com/user-attachments/assets/d75033b0-5c3c-4f76-a85f-1c1a5b16bf59" />
<img width="500" alt="trade-off 128bit" src="https://github.com/user-attachments/assets/ae39a91d-dee2-49b5-bec7-c31b342e3ecf" />


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

