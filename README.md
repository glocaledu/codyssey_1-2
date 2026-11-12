# 나만의 Python 퀴즈 게임

> **Codyssey Mission 2** · Python 콘솔 기반 4지선다 퀴즈 게임  
> 문제를 풀고 직접 추가하면서 **객체지향 프로그래밍, JSON 데이터 저장, 예외 처리, Git/GitHub 협업 흐름**을 학습한 프로젝트입니다.

**GitHub 저장소:** [glocaledu/codyssey_1-2](https://github.com/glocaledu/codyssey_1-2)

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [퀴즈 주제와 선정 이유](#2-퀴즈-주제와-선정-이유)
3. [실행 방법](#3-실행-방법)
4. [주요 기능](#4-주요-기능)
5. [실행 및 개발 스크린샷](#5-실행-및-개발-스크린샷)
6. [클래스 설계 및 프로그램 구조](#6-클래스-설계-및-프로그램-구조)
7. [프로젝트 파일 구조](#7-프로젝트-파일-구조)
8. [JSON 데이터 저장 구조](#8-json-데이터-저장-구조)
9. [예외 처리 설계](#9-예외-처리-설계)
10. [Git 작업 및 커밋 기록](#10-git-작업-및-커밋-기록)
11. [개발 과정](#11-개발-과정)
12. [에러 해결 기록](#12-에러-해결-기록)
13. [배운 점과 향후 개선 계획](#13-배운-점과-향후-개선-계획)

---

## 1. 프로젝트 개요

Python으로 구현한 **터미널(콘솔) 기반 퀴즈 게임**입니다. 사용자는 네 가지 선택지 중 정답을 고르고, 새로운 문제를 등록하거나 퀴즈 목록과 최고 점수를 확인할 수 있습니다. 퀴즈 데이터와 최고 점수는 `state.json` 파일에 저장되어 재실행 시 불러올 수 있습니다.

| 항목 | 내용 |
| --- | --- |
| 프로젝트 | 나만의 Python 퀴즈 게임 |
| 학습 과정 | Codyssey Mission 2 |
| 개발 환경 | Ubuntu (WSL), Visual Studio Code |
| Python | 3.10 이상 필요 / 개발 환경 3.14.4 |
| 주요 기술 | Python, 클래스, 리스트·딕셔너리, JSON, 예외 처리 |
| 버전 관리 | Git / GitHub |
| 외부 라이브러리 | 없음 (Python 표준 라이브러리 사용) |
| 데이터 파일 | `state.json` (UTF-8) |

### 프로젝트 목표

단순히 게임을 실행하는 것을 넘어 다음 질문을 이해하고 설명하는 것을 목표로 했습니다.

- 입력된 값이 어떤 순서로 처리되고 점수로 계산되는가?
- `Quiz`와 `QuizGame`은 어떤 역할을 나눠 맡는가?
- 프로그램을 종료해도 데이터가 유지되는 이유는 무엇인가?
- 기능별 개발 이력을 Git으로 어떻게 남기고 GitHub로 공유하는가?

## 2. 퀴즈 주제와 선정 이유

- **주제:** Python 기초 및 Git 버전 관리
- **선정 이유:** Codyssey에서 학습한 Python 기초 문법과 Git의 주요 개념을 복습하고, 이를 퀴즈 게임으로 구현하면서 조건문, 반복문, 클래스, JSON 파일 입출력 및 Git 버전 관리 능력을 향상시키기 위해 선정했습니다.
- **문제 수:** 기본 퀴즈 **5개** 제공, 사용자가 추가 가능
- **저장 데이터 예시:** 기본 5개에 사용자 등록 문제 1개가 추가된 **총 6개**, 최고 점수 **80점**

기본 문제는 Python의 출력 함수, 리스트 자료형, 조건문, Git 커밋, Docker에 관한 내용입니다.

## 3. 실행 방법

### 3-1. 사전 준비

Python **3.10 이상**이 필요합니다. 별도의 패키지 설치는 필요하지 않습니다.

```bash
python3 --version
```

### 3-2. 저장소 복제 및 실행

```bash
# GitHub 저장소 복제
git clone https://github.com/glocaledu/codyssey_1-2.git

# 프로젝트 폴더로 이동
cd codyssey_1-2

# 퀴즈 게임 실행
python3 main.py
```

> Ubuntu/WSL 기준 명령어입니다. 다른 환경에서는 Python 설치에 따라 `python main.py`를 사용할 수도 있습니다.

### 3-3. 메인 메뉴

```text
========================================
 나만의 Python 퀴즈 게임
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
메뉴를 선택하세요 (1-5):
```

메뉴 번호 `1`~`5`를 입력하면 해당 기능을 실행합니다. 저장소에 `state.json`이 포함되어 있으므로 복제 후 실행하면 저장된 퀴즈와 최고 점수를 불러옵니다. 파일이 없으면 기본 퀴즈 5개로 시작합니다.

## 4. 주요 기능

| 메뉴 | 기능 | 동작 |
| :---: | --- | --- |
| 1 | 퀴즈 풀기 | 등록된 문제를 순서대로 출제, 정오답 표시, 100점 만점으로 점수 계산 |
| 2 | 퀴즈 추가 | 문제·선택지 4개·정답 번호(1~4) 입력 후 JSON 저장 |
| 3 | 퀴즈 목록 | 현재 등록된 퀴즈 제목과 총문제 수 확인 |
| 4 | 점수 확인 | 현재 저장된 최고 점수 확인 |
| 5 | 종료 | 데이터를 저장하고 정상 종료 |

### 추가 구현 사항

- 기본 퀴즈 5개를 제공하고 사용자 등록 문제를 추가할 수 있습니다.
- 점수는 **`round(정답 수 / 전체 문제 수 × 100)`** 으로 계산합니다.
- 기존 최고 점수보다 높은 기록이 나오면 갱신하여 저장합니다.
- 잘못된 메뉴 번호, 답안 범위, 빈 문제·선택지 입력에 재입력을 안내합니다.
- 저장 파일이 없거나 잘못된 JSON·스키마가 감지되면 기본 데이터로 초기화합니다.
- UTF-8 인코딩을 점검하고 임시 파일을 사용해 JSON 저장을 처리합니다.

## 5. 실행 및 개발 스크린샷

> 아래 이미지는 저장소의 `docs/screenshots/` 경로를 참조합니다. README와 이미지가 함께 GitHub에 올라가 있어야 정상 표시됩니다.

### 5-1. 개발 환경 확인

![Python 버전, Git 버전 및 작업 경로 확인](docs/screenshots/01-environment.png)

### 5-2. 메인 메뉴

![퀴즈 게임 메인 메뉴](docs/screenshots/02-menu.png)

### 5-3. 퀴즈 풀기

![퀴즈 실행과 점수 결과](docs/screenshots/03-play.png)

### 5-4. 퀴즈 추가

![새로운 퀴즈 등록 과정](docs/screenshots/04-add_quiz.png)

### 5-5. 퀴즈 목록

![등록된 퀴즈 목록](docs/screenshots/05-quiz_list.png)

### 5-6. 최고 점수

![최고 점수 확인](docs/screenshots/06-best_score.png)

### 5-7. JSON 데이터 확인

![state.json 파일 확인](docs/screenshots/07-json.png)

### 5-8. Git 커밋 및 브랜치 기록

![Git 로그와 브랜치 병합 기록](docs/screenshots/08-git_log.png)

### 5-9. 손상된 JSON 오류 처리

![손상된 JSON 파일 복구 테스트](docs/screenshots/09-error_handling.png)

### 5-10. Git clone 실습

![Git clone 실습](docs/screenshots/10-git_clone.png)

### 5-11. Git pull 실습

![Git pull 실습](docs/screenshots/11-git_pull.png)

## 6. 클래스 설계 및 프로그램 구조

### 6-1. 클래스별 역할

| 클래스 | 역할 | 주요 속성 | 주요 메서드 |
| --- | --- | --- | --- |
| `Quiz` | 퀴즈 문제 한 개를 표현 | `question`, `choices`, `answer` | `show()`, `check_answer()` |
| `QuizGame` | 전체 게임 진행 및 데이터 관리 | `quizzes`, `best_score`, `state_file` | `run()`, `show_menu()`, `play_quiz()`, `add_quiz()`, `show_quiz_list()`, `show_best_score()`, `load_data()`, `save_data()` |

- **`Quiz`**는 문제, 네 개의 선택지, 정답 번호를 보유하고 문제 출력과 정답 판정을 담당합니다.
- **`QuizGame`**은 메뉴, 게임 진행, 퀴즈 목록, 최고 점수, JSON 저장·불러오기를 담당합니다.
- **`__init__`**은 객체 생성 시 처음 사용할 속성을 설정하고, **`self`**는 해당 객체 자신을 가리킵니다.

### 6-2. 전체 데이터 흐름

```text
사용자 입력 (메뉴 번호 / 정답 번호)
                │
                ▼
         main.py (시작점)
                │
                ▼
      QuizGame (quiz_game.py)
        ├─ 메뉴 선택 및 진행
        ├─ Quiz 객체 목록 관리 ──► Quiz (quiz.py)
        │                           ├─ 문제 출력
        │                           └─ 정답 판정
        ├─ 점수 계산 / 최고 점수 관리
        └─ JSON 읽기·쓰기 ◄──────► state.json
                ▲
                │
       quiz_data.py (기본 5문제)
```

Git과 GitHub는 게임 실행 흐름과 별개로 **소스 코드와 문서의 변경 이력**을 관리합니다.

### 6-3. 객체지향 코드 예시

프로젝트의 `Quiz` 클래스는 다음과 같은 구조입니다.

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer
```

## 7. 프로젝트 파일 구조

```text
codyssey_1-2/
├── main.py                 # 프로그램 시작점
├── quiz.py                 # Quiz 클래스
├── quiz_game.py            # QuizGame 클래스, 메뉴/점수/저장
├── quiz_data.py            # 기본 퀴즈 5개 생성
├── state.json              # 퀴즈 데이터와 최고 점수
├── README.md               # 프로젝트 설명 및 학습 기록
├── .gitignore              # Git 추적 제외 규칙
└── docs/
    └── screenshots/        # 실행 및 Git 실습 스크린샷 11개
        ├── 01-environment.png
        ├── 02-menu.png
        ├── 03-play.png
        ├── 04-add_quiz.png
        ├── 05-quiz_list.png
        ├── 06-best_score.png
        ├── 07-json.png
        ├── 08-git_log.png
        ├── 09-error_handling.png
        ├── 10-git_clone.png
        └── 11-git_pull.png
```

## 8. JSON 데이터 저장 구조

### 8-1. 파일과 스키마

- **경로:** 프로젝트 루트의 `state.json`
- **인코딩:** UTF-8 (`ensure_ascii=False`를 사용해 한글 저장)
- **최고 점수:** 정답 개수가 아니라 **0~100점 기준** (`null`은 기록 없음)
- **저장 시점:** 퀴즈 추가, 최고 점수 갱신, 정상적인 메뉴 종료 시

아래는 형식을 보여주기 위해 퀴즈 한 개만 기재한 **축약 예시**입니다. 실제 저장 파일에는 여러 문제가 있습니다.

```json
{
  "quizzes": [
    {
      "question": "Python에서 화면에 글자를 출력하는 함수는?",
      "choices": ["input()", "print()", "open()", "return()"],
      "answer": 2
    }
  ],
  "best_score": 80
}
```

| 키 | 타입 | 의미 |
| --- | --- | --- |
| `quizzes` | `list` | 퀴즈 목록 |
| `quizzes[].question` | `str` | 문제 텍스트 |
| `quizzes[].choices` | `list[str]` | 빈 문자열이 아닌 선택지 4개 |
| `quizzes[].answer` | `int` | 정답 번호(1~4) |
| `best_score` | `int` 또는 `null` | 최고 점수(0~100점) 또는 기록 없음 |

### 8-2. 저장 및 불러오기

1. 게임을 시작할 때 `state.json`을 읽고 구조와 데이터 타입을 검사합니다.
2. JSON이 올바르면 퀴즈 데이터를 `Quiz` 객체로 만들어 사용합니다.
3. 퀴즈를 추가하거나 최고 점수를 갱신하면 데이터를 저장합니다.
4. 저장할 때는 `state.json.tmp` 임시 파일에 먼저 기록하고, 성공하면 `state.json`으로 교체합니다.
5. 파일이 없으면 기본 문제를 사용합니다. 파일이 손상되거나 형식이 틀리면 안내한 뒤 기본 문제로 초기화합니다.

> 참고: 손상된 파일을 테스트할 때는 먼저 백업해야 합니다. 기본 데이터로 초기화한 후 종료하면 기존 데이터가 덮어써질 수 있습니다.

## 9. 예외 처리 설계

| 상황 | 처리 방식 |
| --- | --- |
| 메뉴에 잘못된 값 입력 | `1~5` 범위 안내 후 메뉴 다시 표시 |
| 답안에 문자 또는 범위 밖 숫자 입력 | `1~4` 입력을 안내하고 재입력 요청 |
| 문제 또는 선택지 빈 문자열 | 입력을 다시 요청 |
| `Ctrl+C` (`KeyboardInterrupt`) / 입력 종료 (`EOFError`) | `main.py`에서 예외를 받아 종료 안내 메시지 출력 |
| `state.json` 파일 없음 | 기본 퀴즈로 시작 |
| JSON 손상 또는 잘못된 데이터 구조 | 오류 메시지 출력 후 기본 퀴즈·점수 초기화 |
| 저장 중 인코딩 또는 파일 입출력 문제 | 오류를 안내하고 저장 실패를 반환 |

**주의:** Ctrl+C/EOFError를 처리하는 `main.py`의 예외 처리 구문 자체에는 별도의 저장 호출이 없습니다. 퀴즈 추가·최고 점수 갱신 시 이미 저장된 데이터는 유지되지만, 해당 예외가 발생하는 순간 새로 저장한다고 설명하지 않았습니다.

## 10. Git 작업 및 커밋 기록

### 10-1. 버전 관리 방식

- `main`: 통합된 결과를 관리하는 기준 브랜치
- `feature/quiz-play`: 퀴즈 풀기 기능을 별도로 구현한 브랜치
- 기능 개발 후 `main`에서 `git merge`로 병합
- 작업 단위에 따라 `feat:`, `refactor:`, `docs:` 등의 커밋 메시지 사용

### 10-2. 사용한 주요 Git 명령어

| 명령어 | 실습 내용 |
| --- | --- |
| `git init` | 로컬 Git 저장소 생성 |
| `git add` | 변경된 파일을 스테이징 영역에 등록 |
| `git commit` | 변경사항을 이력으로 저장 |
| `git checkout` | 작업 브랜치 생성·전환 |
| `git merge` | 기능 브랜치의 내용을 `main`으로 병합 |
| `git push` | 로컬 커밋을 GitHub로 업로드 |
| `git clone` | GitHub 저장소를 별도 폴더에 복제 |
| `git pull` | GitHub의 변경사항을 기존 폴더에 반영 |

### 10-3. 확인된 커밋 기록

다음은 프로젝트 진행 중 확인한 주요 커밋의 일부입니다. 전체 이력은 `git log`로 확인할 수 있습니다.

```text
09f36c1 docs: document Git clone and pull practice
8e6c634 docs: finalize README and add mission screenshots
a782c04 feat: persist quiz data and best score in JSON
6acf191 refactor: organize game logic into QuizGame class
538460f merge: integrate quiz play feature
```

```bash
# 전체 커밋과 브랜치 흐름 확인
git log --oneline --graph --all --decorate

# 현재 원격 동기화 상태 확인
git status
```

### 10-4. Git clone / pull 실습

기존 프로젝트를 유지하면서 별도의 복제본에서 변경사항을 만들고 동기화했습니다.

```bash
# 별도 복제본 생성
cd ~/projects/myapp
git clone https://github.com/glocaledu/codyssey_1-2.git codyssey_1-2-clone

# 복제본에서 README 수정 후 커밋·업로드
cd codyssey_1-2-clone
git add README.md
git commit -m "docs: document Git clone and pull practice"
git push origin main

# 기존 프로젝트에서 GitHub 변경사항 가져오기
cd ~/projects/myapp/codyssey_1-2
git pull origin main
```

이 실습으로 `clone`은 **저장소를 처음 복제하는 것**, `pull`은 **이미 있는 저장소를 최신 내용으로 동기화하는 것**임을 확인했습니다.

## 11. 개발 과정

완성된 코드를 한 번에 만들기보다, 기능을 나누어 구현하고 테스트한 뒤 Git으로 기록했습니다.

| 단계 | 작업 내용 | 학습한 개념 | 상태 |
| :---: | --- | --- | :---: |
| 1 | 개발 환경 점검 및 Git 초기화 | CLI, Python, Git | 완료 |
| 2 | 메인 메뉴 구현 | `input`, `print`, `while`, 조건문 | 완료 |
| 3 | `Quiz` 클래스 구현 | 객체, `__init__`, `self` | 완료 |
| 4 | 기본 문제 5개 구성 | 리스트, 객체 생성 | 완료 |
| 5 | 브랜치에서 퀴즈 풀이 기능 개발 | 반복문, 정답 확인, 점수 계산 | 완료 |
| 6 | 퀴즈 추가·목록·최고 점수 | 입력 검증, 데이터 관리 | 완료 |
| 7 | `QuizGame` 클래스 분리 | 클래스 책임 분담, 구조 개선 | 완료 |
| 8 | JSON 영속 저장 및 오류 복구 | `json`, `try/except`, UTF-8 | 완료 |
| 9 | README 및 실행 스크린샷 정리 | 문서화, 증빙 자료 관리 | 완료 |
| 10 | GitHub 복제·푸시·풀 실습 | `clone`, `commit`, `push`, `pull` | 완료 |

문제가 생길 때마다 동작을 다시 확인하고, 파일 구조와 예외 처리를 보완하면서 개발을 마무리했습니다.

## 12. 에러 해결 기록

### 12-1. Python 들여쓰기 오류 (`IndentationError`)

- **상황:** 클래스와 메서드를 작성하거나 수정한 뒤 프로그램 실행 중 들여쓰기 오류가 발생했습니다.
- **원인:** Python은 들여쓰기로 코드 블록을 구분하므로 공백 깊이가 맞지 않으면 실행할 수 없습니다.
- **해결:** `quiz_game.py`의 클래스·메서드·조건문 블록을 다시 정리하고 실행해 확인했습니다.
- **배운 점:** Python에서는 기능뿐 아니라 코드의 **들여쓰기 구조**도 문법의 일부입니다.

### 12-2. Unicode 인코딩 오류 (`UnicodeEncodeError`)

- **상황:** 사용자 입력을 JSON으로 저장하는 과정에서 처리할 수 없는 문자가 문제가 되었습니다.
- **원인:** 일부 입력 문자에 UTF-8로 정상 인코딩할 수 없는 값이 포함될 수 있습니다.
- **해결:** 문제·선택지 입력 시 UTF-8 인코딩을 검사하고, 저장 단계에서도 예외를 처리하도록 수정했습니다.
- **배운 점:** 한글 저장을 위해 인코딩을 지정하는 것뿐 아니라 **입력 데이터의 유효성**도 확인해야 합니다.

### 12-3. 손상된 JSON 파일 복구 테스트

- **상황:** `state.json` 내용을 의도적으로 잘못된 JSON으로 바꾼 뒤 프로그램을 실행했습니다.
- **원인:** 올바르지 않은 JSON 문법은 `json.load()`에서 파싱할 수 없습니다.
- **해결:** 불러오기 오류를 안내하고 기본 퀴즈 5개로 초기화하는 경로를 확인했습니다. 테스트 전 원본 파일을 백업하고 이후 복원했습니다.
- **배운 점:** 파일 읽기 기능은 **파일이 정상일 때뿐 아니라 누락·손상된 상황**도 고려해야 합니다.

> 위 기록은 실제 개발·테스트에서 경험한 문제의 요약입니다. 오류 메시지 전문은 임의로 재구성하지 않았습니다.

## 13. 배운 점과 향후 개선 계획

### 13-1. 배운 점

- **Python 기본 문법:** `if/elif`, `for`, `while`, 함수, 리스트, 딕셔너리로 실행 흐름과 데이터를 관리했습니다.
- **객체지향:** 문제 하나를 표현하는 `Quiz`와 전체 게임을 관리하는 `QuizGame`으로 역할을 나누었습니다.
- **데이터 영속성:** 프로그램 실행 중 메모리의 정보는 사라질 수 있으므로 JSON 파일에 저장해야 한다는 점을 이해했습니다.
- **예외 처리:** 잘못된 사용자 입력, 파일 손상, 인코딩 문제 등 실패 상황도 정상적인 프로그램 설계의 일부임을 배웠습니다.
- **Git 협업 흐름:** `add → commit → push`뿐 아니라 별도 폴더에 `clone`한 뒤 변경사항을 `pull`로 동기화하는 과정을 직접 실습했습니다.
- **AI 활용:** 코드 생성 결과를 그대로 사용하는 대신 파일별 역할, 데이터 흐름, 오류 원인을 확인하고 수정하는 과정이 중요하다는 점을 배웠습니다.

### 13-2. 아쉬운 점

- 퀴즈가 저장된 순서대로 출제되어 반복 학습 시 문제 순서가 같습니다.
- 최고 점수만 기록하므로 이전 시도별 점수 변화는 확인할 수 없습니다.
- 오류 처리를 직접 실행해 확인했지만 자동화된 테스트 코드는 아직 없습니다.

### 13-3. 다음 개선 계획

1. `random` 모듈을 활용한 문제 순서 섞기
2. 출제 문제 수 선택 및 힌트 기능 추가
3. 퀴즈 수정·삭제 및 시도별 점수 기록
4. `unittest` 또는 `pytest`를 이용한 자동 테스트
5. GitHub Pull Request와 코드 리뷰 실습

---

## 제출 정보

- **프로젝트:** Codyssey Mission 2 — 나만의 Python 퀴즈 게임
- **GitHub:** https://github.com/glocaledu/codyssey_1-2
- **증빙:** 개발 환경, 기능 실행, JSON 데이터 및 오류 처리, Git 로그, clone·pull 스크린샷 **총 11개**
- **실행:** `python3 main.py`
