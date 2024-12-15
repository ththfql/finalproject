# 피보나치 수열을 구하는 재귀 함수
def fibonacci(n):
    # 기본 조건: 0번째 또는 1번째 수는 n 자체를 반환
    if n == 0 or n == 1:
        return n
    else:
        # 재귀적으로 두 개의 이전 숫자를 더함
        return fibonacci(n-2) + fibonacci(n-1)

# 사용자가 시작과 끝 범위를 입력하면, 해당 범위에 해당하는 피보나치 수열을 출력하는 함수
def fibonacci_range(start, end):
    # 피보나치 수열을 담을 리스트
    sequence = []
    # 사용자가 입력한 범위에 맞춰 피보나치 수열을 구함
    for i in range(start, end):
        sequence.append(fibonacci(i))  # 해당 인덱스의 피보나치 수를 추가
    return sequence

# 사용자에게 범위를 입력받음
print("피보나치 수열을 출력할 범위를 입력하세요.")
start = int(input("시작 인덱스를 입력하세요 (예: 0): "))
end = int(input("끝 인덱스를 입력하세요 (예: 10): "))

# 범위가 유효한지 확인
if start < 0 or end <= start:
    print("유효한 범위를 입력하세요!")
else:
    # 피보나치 수열 출력
    result = fibonacci_range(start, end)
    print(f"{start}번째부터 {end-1}번째까지의 피보나치 수열: {result}")

