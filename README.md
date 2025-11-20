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
에러 확률 0, 1, 10, 20, 50의 평균치는 0에서의 Error Detection이 0%이므로 최대 80%입니다.
<img width="800" alt="타입별 디텍션 BarChart" src="https://github.com/user-attachments/assets/31526ab8-2986-49ca-91d8-763a2bf4a4d9" />

<img width="500" alt="타입별 평균 errorDetection Rate_Barplot" src="https://github.com/user-attachments/assets/cb0ea734-4ad4-4284-974c-f20371c00ecf" />

<img width="600" alt="Error Detection Hitmap" src="https://github.com/user-attachments/assets/007e14d9-75b1-49b2-b573-9124de3ef23a" />

<img width="800" alt="Delay violinChart" src="https://github.com/user-attachments/assets/cfb659d4-fd3a-4e86-af8b-fe4c3656b859" />


<br>에러 확률 0%를 제외했습니다.<br>
<img width="500" alt="CRC8_errorRate별 디텍션" src="https://github.com/user-attachments/assets/f674d1d6-8c5b-4886-962c-575c8368a54e" />
<img width="500" alt="CRC10_errorRate별 디텍션" src="https://github.com/user-attachments/assets/aee11265-4904-4f3e-9451-529f68416b64" />
<img width="500" alt="CRC16_errorRate별 디텍션" src="https://github.com/user-attachments/assets/fc53e6ce-3a44-425a-bd8d-3085018b64b0" />
<img width="500" alt="CRC32_errorRate별 디텍션" src="https://github.com/user-attachments/assets/a4c29e86-b828-44b0-96a5-d05fa216f70c" />


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

