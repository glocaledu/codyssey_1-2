
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


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요 (1-5): ").strip()

        if choice == "1":
            print("퀴즈 풀기 기능은 준비 중입니다.")
        elif choice == "2":
            print("퀴즈 추가 기능은 준비 중입니다.")
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
