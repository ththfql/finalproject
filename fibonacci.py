

import math

# 재귀를 사용한 피보나치 계산
def fibonacci_recursive(n):
    """재귀 방식으로 n번째 피보나치 수를 계산"""
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 동적 프로그래밍을 사용한 피보나치 계산
def fibonacci_dynamic(n):
    """동적 프로그래밍 방식으로 n번째 피보나치 수를 계산"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]

# 사용자 지정 범위의 피보나치 수열 출력
def fibonacci_range(start, end):
    """start부터 end 사이의 피보나치 수열 출력"""
    fib = [0, 1]
    while fib[-1] < end:
        fib.append(fib[-1] + fib[-2])
    return [x for x in fib if start <= x <= end]

# 특정 숫자가 피보나치 수열에 포함되는지 확인
def is_fibonacci_number(num):
    """
    특정 숫자가 피보나치 수열에 포함되는지 확인.
    5*num^2 + 4 또는 5*num^2 - 4가 완전제곱수라면 피보나치 수입니다.
    """
    def is_perfect_square(x):
        return int(math.sqrt(x))**2 == x

    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

# 메인 실행
if __name__ == "__main__":
    print("=== 피보나치 수열 계산기 ===")
    mode = int(input("원하는 기능을 선택하세요 (1: 범위 출력, 2: n번째 항 계산, 3: 특정 숫자 확인): "))

    if mode == 1:
        # 범위 출력
        start = int(input("피보나치 수열의 시작 범위를 입력하세요: "))
        end = int(input("피보나치 수열의 끝 범위를 입력하세요: "))
        print(f"피보나치 수열 ({start} ~ {end}): {fibonacci_range(start, end)}")

    elif mode == 2:
        # n번째 항 계산
        n = int(input("피보나치 수열에서 원하는 항의 번호를 입력하세요: "))
        method = int(input("어떤 방식으로 계산하시겠습니까? (1: 재귀, 2: 동적 프로그래밍): "))
        if method == 1:
            print(f"{n}번째 피보나치 수 (재귀 방식): {fibonacci_recursive(n)}")
        elif method == 2:
            print(f"{n}번째 피보나치 수 (동적 프로그래밍 방식): {fibonacci_dynamic(n)}")
        else:
            print("잘못된 입력입니다.")

    elif mode == 3:
        # 특정 숫자 확인
        num = int(input("피보나치 수열에서 확인할 숫자를 입력하세요: "))
        if is_fibonacci_number(num):
            print(f"{num}는 피보나치 수열에 포함됩니다!")
        else:
            print(f"{num}는 피보나치 수열에 포함되지 않습니다.")
    else:
        print("잘못된 입력입니다.")

