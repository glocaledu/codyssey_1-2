
from quiz import Quiz


def create_default_quizzes():
    quizzes = [
        Quiz(
            "Python에서 화면에 글자를 출력하는 함수는?",
            ["input()", "print()", "open()", "return()"],
            2
        ),
        Quiz(
            "Python에서 여러 데이터를 순서대로 저장하는 자료형은?",
            ["int", "bool", "list", "str"],
            3
        ),
        Quiz(
            "Python에서 조건을 판단할 때 사용하는 키워드는?",
            ["for", "def", "class", "if"],
            4
        ),
        Quiz(
            "Git에서 변경사항을 기록하는 명령어는?",
            ["git commit", "git clone", "git pull", "git status"],
            1
        ),
        Quiz(
            "Docker에서 컨테이너의 실행 기반이 되는 것은?",
            ["Volume", "Image", "Branch", "Commit"],
            2
        )
    ]

    return quizzes
