# class UserInfo:
#     """
#     Author : Hong
#     Date : 2023.06.21
#     Description : 클래스 작성법
#     """
#     def user_info(self):
#         print("메소드 실행")
    
# user1 = UserInfo()
# print(user1)    # <__main__.UserInfo object at 0x00000145C8D67190>
# user1.user_info()

class UserInfo:
    # """
    # Author : Hong
    # Date : 2023.06.21
    # Description : 클래스 작성법
    # """

    def __init__(self, name, age) -> None:
        self.name = name
        self.age =  age

    def user_info(self):
        return "name : {}, age : {}".format(self.name,self.age)
    
# 두 명의 객체 생성
user1 = UserInfo("홍길동", 30)
user2 = UserInfo("김길동", 40)


# user_info 호출
print(user1.user_info)
print(user2.user_info)