
from quiz import Quiz
from quiz_data import create_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None

    def show_menu(self):
        print("\n========================================")
        print("       나만의 Python 퀴즈 게임")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {number}]")
            quiz.show()

            while True:
                answer = input("정답 입력 (1-4): ").strip()

                if answer in ["1", "2", "3", "4"]:
                    answer = int(answer)
                    break

                print("1-4 사이의 숫자를 입력하세요.")

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        percentage = round(score / total * 100)

        print("\n========================================")
        print(f"결과: {total}문제 중 {score}문제 정답!")
        print(f"점수: {percentage}점")

        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage
            print("새로운 최고 점수입니다!")

        print("========================================")

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("문제는 비워둘 수 없습니다.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"선택지 {number}: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("선택지는 비워둘 수 없습니다.")

        while True:
            answer = input("정답 번호 (1-4): ").strip()

            if answer in ["1", "2", "3", "4"]:
                answer = int(answer)
                break

            print("1-4 사이의 숫자를 입력하세요.")

        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    def run(self):
        while True:
            self.show_menu()
            choice = input("메뉴를 선택하세요 (1-5): ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_best_score()
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
