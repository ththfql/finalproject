import math  # 수학 연산을 위한 math 모듈

# 재귀를 사용한 피보나치 계산
def fibonacci_recursive(n):
    """
    주어진 n번째 피보나치 수를 재귀 방식으로 계산합니다.
    계산 시 이전 결과를 저장하지 않아 호출 횟수가 많아질 수 있습니다.

    매개변수:
        n (int): 계산하려는 피보나치 수의 위치
    반환값:
        int: n번째 피보나치 수
    """
    if n == 0 or n == 1:  # 기본 조건: 0번째와 1번째는 바로 반환
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  # 이전 두 항의 합 반환

# 동적 프로그래밍을 사용한 피보나치 계산
def fibonacci_dynamic(n):
    """
    주어진 n번째 피보나치 수를 동적 프로그래밍 방식으로 계산합니다.
    이전 결과를 저장하여 효율적으로 계산합니다.

    매개변수:
        n (int): 계산하려는 피보나치 수의 위치
    반환값:
        int: n번째 피보나치 수
    """
    if n == 0:  # 0번째 항은 0
        return 0
    elif n == 1:  # 1번째 항은 1
        return 1

    # 이전 계산 결과를 저장할 리스트
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])  # 현재 항은 이전 두 항의 합
    return fib[-1]  # n번째 피보나치 수 반환

# 사용자 지정 범위의 피보나치 수열 출력
def fibonacci_range(start, end):
    """
    주어진 시작 값(start)과 끝 값(end) 사이의 피보나치 수열을 계산합니다.

    매개변수:
        start (int): 출력할 피보나치 수열의 시작 범위
        end (int): 출력할 피보나치 수열의 끝 범위
    반환값:
        list: 지정된 범위 내의 피보나치 수열
    """
    # 초기값 설정
    fib = [0, 1]
    while fib[-1] < end:  # 수열의 마지막 값이 끝 범위를 초과하기 전까지 반복
        fib.append(fib[-1] + fib[-2])  # 다음 항 계산 및 추가
    return [x for x in fib if start <= x <= end]  # 지정된 범위의 항만 반환

# 특정 숫자가 피보나치 수열에 포함되는지 확인
def is_fibonacci_number(num):
    """
    주어진 숫자가 피보나치 수열에 포함되는지 확인합니다.
    5*num^2 + 4 또는 5*num^2 - 4가 완전제곱수이면 피보나치 수입니다.

    매개변수:
        num (int): 확인하려는 숫자
    반환값:
        bool: 숫자가 피보나치 수열에 포함되면 True, 그렇지 않으면 False
    """
    # 완전제곱수인지 확인하는 함수 정의
    def is_perfect_square(x):
        return int(math.sqrt(x))**2 == x

    # 피보나치 수 확인 공식 적용
    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

# 메인 실행
if __name__ == "__main__":
    """
    피보나치 수열 계산기:
    - 1: 범위 내 피보나치 수열 출력
    - 2: n번째 피보나치 항 계산
    - 3: 특정 숫자가 피보나치 수열에 포함되는지 확인
    """
    print("=== 피보나치 수열 계산기 ===")
    # 사용자로부터 모드를 선택받습니다.
    mode = int(input("원하는 기능을 선택하세요 (1: 범위 출력, 2: n번째 항 계산, 3: 특정 숫자 확인): "))

    if mode == 1:
        # 범위 출력 기능
        start = int(input("피보나치 수열의 시작 범위를 입력하세요: "))
        end = int(input("피보나치 수열의 끝 범위를 입력하세요: "))
        result = fibonacci_range(start, end)
        print(f"피보나치 수열 ({start} ~ {end}): {result}")

    elif mode == 2:
        # n번째 항 계산 기능
        n = int(input("피보나치 수열에서 원하는 항의 번호를 입력하세요: "))
        method = int(input("어떤 방식으로 계산하시겠습니까? (1: 재귀, 2: 동적 프로그래밍): "))
        if method == 1:
            # 재귀 방식으로 계산
            result = fibonacci_recursive(n)
            print(f"{n}번째 피보나치 수 (재귀 방식): {result}")
        elif method == 2:
            # 동적 프로그래밍 방식으로 계산
            result = fibonacci_dynamic(n)
            print(f"{n}번째 피보나치 수 (동적 프로그래밍 방식): {result}")
        else:
            print("잘못된 입력입니다.")  # 잘못된 입력 처리

    elif mode == 3:
        # 특정 숫자 확인 기능
        num = int(input("피보나치 수열에서 확인할 숫자를 입력하세요: "))
        if is_fibonacci_number(num):
            print(f"{num}는 피보나치 수열에 포함됩니다!")
        else:
            print(f"{num}는 피보나치 수열에 포함되지 않습니다.")
    else:
        print("잘못된 입력입니다.")  # 잘못된 입력 처리

