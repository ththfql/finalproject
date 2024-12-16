import math  # 수학 연산을 위한 math 모듈

# 재귀를 사용한 피보나치 계산
def fibonacci_recursive(n):
    if n == 0 or n == 1:  # 기본 조건: 0번째와 1번째는 바로 반환
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  # 이전 두 항의 합 반환

# 동적 프로그래밍을 사용한 피보나치 계산
def fibonacci_dynamic(n):
    if n == 0:  # 0번째 항은 0
        return 0
    elif n == 1:  # 1번째 항은 1
        return 1

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])  # 현재 항은 이전 두 항의 합
    return fib[-1]  # n번째 피보나치 수 반환

# 사용자 지정 범위의 피보나치 수열 출력
def fibonacci_range(start, end):
    fib = [0, 1]
    while fib[-1] < end:  # 수열의 마지막 값이 끝 범위를 초과하기 전까지 반복
        fib.append(fib[-1] + fib[-2])  # 다음 항 계산 및 추가
    return [x for x in fib if start <= x <= end]  # 지정된 범위의 항만 반환

# 특정 숫자가 피보나치 수열에 포함되는지 확인
def is_fibonacci_number(num):
    def is_perfect_square(x):
        return int(math.sqrt(x))**2 == x

    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

# 피보나치 수열의 총합 계산
def fibonacci_sum(start, end):
    """
    주어진 범위 내의 피보나치 수열 항들의 총합을 계산합니다.

    매개변수:
        start (int): 계산할 피보나치 수열의 시작 값
        end (int): 계산할 피보나치 수열의 끝 값
    반환값:
        int: 지정된 범위 내의 피보나치 수열의 총합
    """
    fib = [0, 1]
    while fib[-1] < end:  # 수열의 마지막 값이 끝 범위를 초과하기 전까지 반복
        fib.append(fib[-1] + fib[-2])  # 다음 항 계산 및 추가
    fib_in_range = [x for x in fib if start <= x <= end]
    return sum(fib_in_range)  # 지정된 범위 내의 피보나치 수들의 합 반환

# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 피보나치 수열에서 소수만 출력하는 함수
def fibonacci_primes(n):
    fib = [0, 1]
    while fib[-1] < n:  # 수열의 마지막 값이 끝 범위를 초과하기 전까지 반복
        fib.append(fib[-1] + fib[-2])  # 다음 항 계산 및 추가
    primes_in_fib = [x for x in fib if is_prime(x)]  # 피보나치 수열에서 소수만 필터링
    return primes_in_fib  # 소수만 반환

# 메인 실행
if __name__ == "__main__":
    print("=== 피보나치 수열 계산기 ===")
    mode = int(input("원하는 기능을 선택하세요 (1: 범위 출력, 2: n번째 항 계산, 3: 특정 숫자 확인, 4: 범위 내 총합 계산, 5: 피보나치 수열에서 소수만 출력): "))

    if mode == 1:
        start = int(input("피보나치 수열의 시작 범위를 입력하세요: "))
        end = int(input("피보나치 수열의 끝 범위를 입력하세요: "))
        result = fibonacci_range(start, end)
        print(f"피보나치 수열 ({start} ~ {end}): {result}")

    elif mode == 2:
        n = int(input("피보나치 수열에서 원하는 항의 번호를 입력하세요: "))
        method = int(input("어떤 방식으로 계산하시겠습니까? (1: 재귀, 2: 동적 프로그래밍): "))
        if method == 1:
            result = fibonacci_recursive(n)
            print(f"{n}번째 피보나치 수 (재귀 방식): {result}")
        elif method == 2:
            result = fibonacci_dynamic(n)
            print(f"{n}번째 피보나치 수 (동적 프로그래밍 방식): {result}")
        else:
            print("잘못된 입력입니다.")

    elif mode == 3:
        num = int(input("피보나치 수열에서 확인할 숫자를 입력하세요: "))
        if is_fibonacci_number(num):
            print(f"{num}는 피보나치 수열에 포함됩니다!")
        else:
            print(f"{num}는 피보나치 수열에 포함되지 않습니다.")

    elif mode == 4:
        start = int(input("피보나치 수열의 시작 범위를 입력하세요: "))
        end = int(input("피보나치 수열의 끝 범위를 입력하세요: "))
        result = fibonacci_sum(start, end)
        print(f"피보나치 수열 ({start} ~ {end})의 총합: {result}")

    elif mode == 5:
        n = int(input("피보나치 수열에서 원하는 범위의 숫자까지 소수를 출력하려면 범위를 입력하세요: "))
        result = fibonacci_primes(n)  # 피보나치 수열에서 소수만 필터링
        print(f"피보나치 수열 내 소수들: {result}")

    else:
        print("잘못된 입력입니다.")

