from task1 import Student

## 문제 2: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        avg_score = sum(self.scores) / len(self.scores)
        return avg_score

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 / add_score 메서드를 호출하세요. 
        # 기본점수 : 60점, 최대 추가 점수 : 40점 
        # 최대 공부시간 8시간으로 시간에 비례해서 점수 추가
        # YOUR CODE HERE
        base_score = 60
        extra_score = 5 * hours
        score = base_score + extra_score
        if hours > 8:
            score = 100
            self.add_score(score)
            return 
        else:
            self.add_score(score)

# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE
if __name__ == "__main":
    student = GradedStudent('홍박사',15,2)

    # 4일동안 각각 12 ~ 0 시간 공부
    student.study(12)
    student.study(8)
    student.study(4)
    student.study(0)

    # 평균 구하기
    avg_score = student.calculate_average()
    print(f"평균 점수는 {avg_score}점 입니다.")
