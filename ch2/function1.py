# 함수
# 함수?(자바스크립트, 파이썬) 메소드? ==> 기능 정의
# 함수 : 단독으로 실행
# 메소드 : 클래스 내부에 선언,  객체 생성 후 실행

# 함수 정의
def hello():
    print("Hello")

#  함수 호출
hello()

def add(a, b):
    return a + b
print(add(3,4))

# 기본값 : n = 2 => 함수 호출 시 값이 넘어오지 않는다면 기본값을 2로 지정
def print_n_times(value, n=2):
    for i in range(n):
        print(i, value)

print_n_times("안녕하세요", 5)
print_n_times("반갑습니다")

# 가변 파라메터 : 파라메터의 개수다 일정치 않음
def add_many(*args):
    print(args)

add_many({"dessert": "macaroon", "wine": "merlot"})  #({'dessert': 'macaroon', 'wine': 'merlot'},)
add_many("35","24", "48")   #('35', '24', '48')
add_many(["A", "B", "C", "D"])  #(['A', 'B', 'C', 'D'],)
add_many()

def add_many2(*args):
    result = 0
    for  i in  args:
        result += i

    print("합계", result)

add_many2(1, 2, 3)
add_many2(1, 2, 3, 4, 5, 6)
add_many2(1, 2, 3, 4, 5, 6, 7, 8, 9)


def sum_mul(choice, *args):
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "add":
        result = 0
        for i in args:
            result += i
    return result

# TypeError: sum_mul() missing 1 required keyword-only argument: 'choice'
add_result = sum_mul("add", 1, 2, 3, 4, 5, 6)
mul_result = sum_mul("mul", 1, 2, 3, 4, 5, 6)

print("덧셈", add_result)
print("곱셈", mul_result)

# **kwargs : 키워드 파라미터(key=value)
def args_func1(**kwargs):
    print(kwargs)

args_func1(name="park")
args_func1(name="park", age=12)
args_func1(name="park", age=12, title="python")

# 일반, 기본 파라메터, 가변 파라메터, 키워드 파라메터
def example_mul(arg1, arg2=15, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20)  #10 20 () {}
example_mul(10)     #10 15 () {}
example_mul(10,20, "park", "kim")   #10 20 ('park', 'kim') {}
example_mul(10,20, "park", "kim", age=25, name="cho")   #10 20 ('park', 'kim') {'age': 25, 'name': 'cho'}

# 다중 리턴
def sum_add_mul(a, b):
    return a + b, a * b

print(sum_add_mul(5, 6))    #(11, 30)

add1, sum1 = sum_add_mul(5, 6)
print("덧셈", add1)
print("곱셈", sum1)

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3
r1, r2, r3 = func_mul(100)
print(r1, r2, r3)

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]
r1, r2, r3 = func_mul2(100)
print(r1, r2, r3)

def say_nuck(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nuck("바보")
say_nuck("야호")

# 두 개의 인자와 연산자를 받아 사칙연산을 수행하는 함수 작성
# +, -, *, //
# def totel(num1, num2, op):
#     if op == "+":
#         return num1 + num2        
#     elif op == "-":
#         return num1 - num2        
#     elif op == "*":
#         return num1 * num2        
#     elif op == "/":
#         return num1 // num2   

# num1 = int(input("숫자 입력 : "))
# op = input("연산자 입력 : ")
# num2 = int(input("숫자 입력 : "))     

# print("{} {} {} = {}".format(num1, op, num2, totel(num1,num2,op)))

import random
# random.randrange(1, 46) : 1 ~ 45 까지의 임의의 수 리턴
print("임의의 수",random.randrange(1, 46))
        
# 1 ~ 45 까지의 임의의 수 리턴 함수 작성
# 6개의 숫자가 리스트레 담길 때까지 함수 호출
# 6개의 숫자가 담기면 함수 호출 종료 후 리스트 출력
def lotto():
    return random.randrange(1, 46)
numbers = []

while True:
    num = lotto()
    if numbers.count(num)  == 0:    #중복 숫자 제외
        numbers.append(num)
    if len(numbers) >=6:
        break
numbers.sort()
print(numbers)


a = 1

# 파이썬 함수 내부에서는 외부에 선언한 변수를 사용할 수 없음
# 외부 변수 사용 시 global 키워드 필요
def func1():
    global a
    a += 3
    print(a)    # UnboundLocalError

func1()