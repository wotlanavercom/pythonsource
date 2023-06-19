# 파이썬 자료형
# 1. 문자열
# "", '', """ """, ''' '''

# + : 결합
print("Python " + "is fun")

# * : 복제(곱하기)
print("Python" * 3)

print("*" * 50)
print("내 프로그램")
print("*" * 50)

# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)

str1 = "Life is too short"
print(str1[3])

# 슬라이싱 [시작위치 : 끝위치] =>끝 위치 포함하지 않음
print("str1[2:6]", str1[2:6])
print("str1[:6]", str1[:6]) # 시작위치 지정하지 않은 경우 0
print("str1[:]", str1[:]) # 위치 지정하지 않은 경우 0 ~ 끝
print("str1[:-4]", str1[:-4]) # - 값은 오른쪽 끝에서부터 위치를 잡는 경우 -1 부터 시작

# len() : 길이 함수
print("str1 길이", len(str1))


str2 = "20230615Sunny"
# 년도, 날씨를 구별해서 변ㄴ수에 담기
date = str2[:8]
weather = str2[8:]
print(date, weather)

# date 변수에 단긴 값을 년-월-일
yaer = date[:4]
month = date[4:6] 
day = date[6:]
print("{}-{}-{}".format(yaer,month,day))
# print(yaer, month, day, sep="-")

# 주민등록번호 001205-3234567
# 남자(1,3) / 여자(2,4) 출력
str3 = "001205-3234567"
no = str3[7]
if no == "1" or no == "3":
    print("남")
elif no == "2" or no == "4":
    print("여")

if int(no) % 2 == 1:
    print("남")
else:
    print("여")

str1 = "대한민국"
for s in str1:
    print(s+"$", end="")   # 대$한$민$국$

print()
# 입력받은 숫자만큼 하트 출력
# 54321
# ♥♥♥♥♥
# ♥♥♥♥
# ♥♥♥
# ♥♥
# ♥

# num = input("숫자를 입력해 주세요")

# for i in range(len(num)):
#     for j in range(int(num[i])):
#         print("♥",end="")
#     print()

# 문자열 관련 함수
# count
print("\n문자열 관련 함수")
str1 = "hobby"
print("원본 문자열에 포함된 특정 문자 개수", str1.count("b"))

str1 = "python is best choice"

# find() : 없는 경우 -1 반환
print("찾는 문자의 시작 위치 반환", str1.find("b"))
print("찾는 문자의 시작 위치 반환", str1.find("k"))     # 없으면 -1 반환
print("찾는 문자의 시작 위치 반환", str1.find("i", 10))
print("찾는 문자의 시작 위치 반환", str1.rfind("i"))

# index() : 못찾는 경우 ValueError 발생
print("찾는 문자의 시작 위치 반환", str1.index("b"))
# print("찾는 문자의 시작 위치 반환", str1.index("k"))

# startswith() / endswith() : 특정 문자열로 시작하는지 / 끝나는지
print(str1.startswith("p"))
print(str1.endswith("p"))

# join()
str2 = ","
print("문자열 삽입", str2.join("abcde"))

# upper() / lower()
print("대문자", "abcdef".upper())
print("소문자", "ABCDEF".lower())

# swapcase() : 대문자 -> 소문자, 소문자 -> 대문자 변환
str1 = "Python is Easy"
print(str1.swapcase())

print("abc" == "ABC")

# 공백 제거 : 왼쪽, 오른쪽, 양쪽
str1 = "      hi"
print(str1)
print("왼쪽 공백 제거", str1.lstrip())

str1 = "hi             "
print(str1)
print("오른쪽 공백 제거", str1.rstrip())

str1 = "       hi             "
print(str1)
print("양쪽 공백 제거", str1.strip())

#replace()
str1 = "Life is too short"
print("특정 문자열 변경", str1.replace("Life", "Your leg"))

# split() => [](리스트) 로 반환
print(str1.split())     #['Life', 'is', 'too', 'short']

a = "abcd"
print(a.split())        #['abcd']

a = "a:b:c:d"
print(a.split(":"))

a = "하나\n둘\n셋"
print(a.splitlines())   #['하나', '둘', '셋']
print(a.split())    #['하나', '둘', '셋']

# 문자열 구성 파악 - isdigit(), isalpha(), isalnum(), islower(), isupper()
print("12345".isdigit())    # 숫자로만 구성되어 있느냐?
print("12345".isalpha())    # 알파벳으로 구성되어 있느냐?
print("12345".isalnum())    # 알파벳 or 숫자로 구성되어 있느냐?


# 사이트별 비밀번호를 만들어 주는 프로그램
# https://www.naver.com

# 규칙 1 : https://www. 제외 ==> naver.com
# 규칙 2 :  처음 나오는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 e 개수 + ! 구성
# 완성된 비밀번호 : nav51!

url = "https://www.naver.com"

# 규칙 1 적용
# url = url[12:]
url = url.replace("https://www.","")

# 규칙 2 적용
# idx = url.find(".")
# url = url[:idx]
url = url[: url.find(".")]

# 규칙 3 적용
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"

print(password)