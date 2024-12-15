# 기존의 재귀 방식으로 피보나치 수열을 구하는 함수
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 동적 프로그래밍 방식으로 피보나치 수열을 구하는 함수
def fibonacci_dp(n):
    # 피보나치 수열의 0번째 항과 1번째 항을 미리 설정합니다.
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])  # fib[i]는 fib[i-1] + fib[i-2]로 계산
    return fib[n]

# 사용자로부터 피보나치 수를 구할 항의 번호와 계산 방법을 입력받음
numero = int(input("피보나치 수열에서 원하는 항의 번호를 입력하세요: "))

# n번째 항이 0 이하인 경우는 피보나치 수열에 해당하지 않으므로 오류 메시지를 출력합니다.
if numero < 0:
    print("잘못된 입력입니다. 양의 정수를 입력하세요.")
else:
    # 계산 방법 선택: 재귀 방식 또는 동적 프로그래밍 방식
    method = input("어떤 방식으로 계산하시겠습니까? (1: 재귀, 2: 동적 프로그래밍): ")
    
    if method == '1':
        # 재귀 방식으로 피보나치 수를 계산
        print(f"{numero}번째 피보나치 수 (재귀 방식): {fibonacci_recursive(numero)}")
    elif method == '2':
        # 동적 프로그래밍 방식으로 피보나치 수를 계산
        print(f"{numero}번째 피보나치 수 (동적 프로그래밍 방식): {fibonacci_dp(numero)}")
    else:
        print("잘못된 입력입니다. 1 또는 2를 선택해주세요.")
