# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.
# 입력 : 2개의 실수가 공백으로 구분되어 입력된다.
# 출력 : 첫 번째 실수와 두 번째 실수를 곱한 값을 출력한다.

a, b = input().split()

a = float(a)
b = float(b)

answer = a * b

print(answer)