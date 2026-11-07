
from quiz import Quiz
from quiz_data import create_default_quizzes


def show_menu():
    print("\n========================================")
    print("       나만의 Python 퀴즈 게임")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")


def play_quiz(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    score = 0
    total = len(quizzes)

    print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

    for number, quiz in enumerate(quizzes, start=1):
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

    percentage = score / total * 100

    print("\n========================================")
    print(f"결과: {total}문제 중 {score}문제 정답!")
    print(f"점수: {percentage:.0f}점")
    print("========================================")

def add_quiz(quizzes):
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

    new_quiz = Quiz(question, choices, answer)

    quizzes.append(new_quiz)

    print("퀴즈가 추가되었습니다!")
    print(f"현재 등록된 퀴즈: {len(quizzes)}개")


def main():
    quizzes = create_default_quizzes()

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요 (1-5): ").strip()

        if choice == "1":
            play_quiz(quizzes)
        elif choice == "2":
            add_quiz(quizzes)
        elif choice == "3":
            print("퀴즈 목록 기능은 준비 중입니다.")
        elif choice == "4":
            print("점수 확인 기능은 준비 중입니다.")
        elif choice == "5":
            print("게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
