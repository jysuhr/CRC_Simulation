# CRC_Simulation

데이터 통신과 네트워크 CRC 구현 과제
<p align="center">
	<a href="https://www.python.org/">
		<img src="https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white" alt="Python" />
	</a>
</p>

## CRC 규칙
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