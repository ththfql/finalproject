

def fibonacci(n):
	# 기본적인 재귀 종료 조건
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		# 피보나치 수를 계산하는 재귀 함수
		return fibonacci(n-1) + fibonacci(n-2)

# 사용자로부터 피보나치 수의 위치를 입력받음
numero = int(input("원하는 피보나치 수의 위치를 입력하세요: "))

# 음수 입력에 대한 예외 처리
if numero < 0:
	print("잘못된 입력입니다. 0 이상의 정수를 입력해주세요.")
else:
	# 원하는 위치의 피보나치 수를 출력
	print(f"피보나치 수열에서 위치 {numero}의 값은 {fibonacci(numero)} 입니다.")

