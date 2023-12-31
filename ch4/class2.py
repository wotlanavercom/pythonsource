class Student:
    def __init__(self, name, number, grade, details) -> None:
        """
        생성자(오버로딩 없음)
        self == 자바에서 this
        """
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    def __str__(self) -> str:
        """
        toString 역할
        """
        return "이름 : {}, 학년 : {}, 반 : {}, 학생정보 : {}".format(
            self.name,
            self.grade,
            self.number,
            self.details,
        )


# 객체 생성
Student1 = Student("Kim", 1, 1, {"gender": "male", "score1": 95, "score2": 99})
Student2 = Student("Park", 2, 1, {"gender": "female", "score1": 88, "score2": 89})
Student3 = Student("Hong", 3, 1, {"gender": "male", "score1": 78, "score2": 79})

# 확인 
print(Student1)
print(Student2)
print(Student3)
