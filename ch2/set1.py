# 파이썬 자료형
# 5. 집합
# set() : 자바의 Set 과 동일
# 중복을 허용하지 않음
# 순서가 없음(==> 인덱싱 사용 불가)

set1 = set()
set2 = set([1, 12, 13, 14])
set3 = set([1, 4, 5, 6, 6, 6])

print(set1)
print(set2)
print(set3)     #{1, 4, 5, 6}

t1 = (1, 3, 5, 7)
set4 = set(t1)
print(set4)

dict1 = {"a":10, "b":20, "c":30}
set5 = set(dict1)
print(set5)

str1 = "abcdefg"
print(set(str1))    #{'b', 'f', 'e', 'a', 'c', 'd', 'g'}

# set => list, tuple
print(list(set2))
print(tuple(set2))

# 함수
# 교집합, 합집함, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print("교집합")
print(s1 & s2)
print(s1.intersection(s2))

print("합집합")
print(s1 | s2)
print(s1.union(s2))

print("차집합")
print(s1 - s2)
print(s1.difference(s2))

# add() - 1개의 값만 추가 
s1.add(9)
print(s1)

# update(0) - 여러 개의 값 추가
s1.update([10, 11, 12])
print(s1)

# remove() - 특정 값 제거
s1.remove(10)
print(s1)