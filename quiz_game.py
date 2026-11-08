
import json
from pathlib import Path

from quiz import Quiz
from quiz_data import create_default_quizzes


class QuizGame:
    def __init__(self):
        self.state_file = Path(__file__).resolve().parent / "state.json"
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.load_data()

    # 메뉴 출력
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

    # 데이터 저장
    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        temp_file = self.state_file.with_suffix(".json.tmp")

        try:
            # UTF-8 인코딩 검사
            for index, quiz in enumerate(self.quizzes, start=1):
                for field_name, value in [
                    ("question", quiz.question),
                    *[
                        (f"choice_{i}", choice)
                        for i, choice in enumerate(quiz.choices, start=1)
                    ]
                ]:
                    try:
                        value.encode("utf-8")
                    except UnicodeEncodeError:
                        print(
                            f"문자 오류: {index}번 퀴즈 "
                            f"{field_name}: {ascii(value)}"
                        )
                        return False

            # 임시 파일에 데이터 기록
            with temp_file.open("w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            # 저장 완료 후 실제 파일로 교체
            temp_file.replace(self.state_file)
            return True

        except (OSError, UnicodeError, TypeError, ValueError) as error:
            print(f"데이터 저장 오류: {error}")
            return False

    # 데이터 불러오기
    def load_data(self):
        if not self.state_file.exists():
            print("저장 파일이 없어 기본 퀴즈를 사용합니다.")
            return

        try:
            with self.state_file.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식이 올바르지 않습니다.")

            raw_quizzes = data["quizzes"]
            best_score = data["best_score"]

            if not isinstance(raw_quizzes, list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            if best_score is not None and (
                type(best_score) is not int
                or not 0 <= best_score <= 100
            ):
                raise ValueError("최고 점수 형식이 잘못되었습니다.")

            loaded_quizzes = []

            for item in raw_quizzes:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 항목 형식이 잘못되었습니다.")

                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if (
                    not isinstance(question, str)
                    or not question.strip()
                    or not isinstance(choices, list)
                    or len(choices) != 4
                    or any(
                        not isinstance(choice, str) or not choice.strip()
                        for choice in choices
                    )
                    or type(answer) is not int
                    or not 1 <= answer <= 4
                ):
                    raise ValueError("퀴즈 데이터가 잘못되었습니다.")

                # 문자열에 잘못된 Unicode 문자가 있는지 확인
                question.encode("utf-8")
                for choice in choices:
                    choice.encode("utf-8")

                loaded_quizzes.append(
                    Quiz(question, choices, answer)
                )

            self.quizzes = loaded_quizzes
            self.best_score = best_score

            print(
                f"저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개, "
                f"최고 점수 {self.best_score})"
            )

        except (
            OSError,
            UnicodeError,
            ValueError,
            KeyError,
            TypeError
        ) as error:
            print(f"데이터 불러오기 오류: {error}")
            print("기본 퀴즈 데이터로 초기화합니다.")
            self.quizzes = create_default_quizzes()
            self.best_score = None

    # 퀴즈 풀기
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
                answer_text = input("정답 입력 (1-4): ").strip()

                if answer_text in ["1", "2", "3", "4"]:
                    answer = int(answer_text)
                    break

                print("1-4 사이의 숫자를 입력하세요.")

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print(
                    f"오답입니다. 정답은 {quiz.answer}번입니다."
                )

        percentage = round(score / total * 100)

        print("\n========================================")
        print(f"결과: {total}문제 중 {score}문제 정답!")
        print(f"점수: {percentage}점")

        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage

            if self.save_data():
                print("새로운 최고 점수가 저장되었습니다!")
            else:
                print("최고 점수가 갱신되었지만 저장에 실패했습니다.")

        print("========================================")

    # 퀴즈 추가
    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if not question:
                print("문제는 비워둘 수 없습니다.")
                continue

            try:
                question.encode("utf-8")
                break
            except UnicodeEncodeError:
                print("저장할 수 없는 문자가 포함되어 있습니다.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"선택지 {number}: ").strip()

                if not choice:
                    print("선택지는 비워둘 수 없습니다.")
                    continue

                try:
                    choice.encode("utf-8")
                    choices.append(choice)
                    break
                except UnicodeEncodeError:
                    print("저장할 수 없는 문자가 포함되어 있습니다.")

        while True:
            answer_text = input("정답 번호 (1-4): ").strip()

            if answer_text in ["1", "2", "3", "4"]:
                answer = int(answer_text)
                break

            print("1-4 사이의 숫자를 입력하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        if self.save_data():
            print("퀴즈가 추가되고 저장되었습니다!")
            print(f"현재 등록된 퀴즈: {len(self.quizzes)}개")
        else:
            print("퀴즈는 추가되었지만 파일 저장에 실패했습니다.")

    # 퀴즈 목록
    def show_quiz_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print("\n========================================")
        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("========================================")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("========================================")

    # 최고 점수 확인
    def show_best_score(self):
        if self.best_score is None:
            print("\n아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"\n최고 점수: {self.best_score}점")

    # 게임 실행
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
                if self.save_data():
                    print("데이터를 저장했습니다.")
                else:
                    print("데이터 저장에 실패했습니다.")

                print("게임을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
