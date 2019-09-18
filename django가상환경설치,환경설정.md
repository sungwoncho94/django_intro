## Django Setting

1. 가상환경
   새로운 장고 프로젝트를 시작할 때 마다 그 프로젝트만의 가상환경을 구축해야함.
   이유 : 프로젝트마다 사용하는 라이브러리, 버전이 다를 수 있음. --> 호환성, 의존성 발생

```bash
# django - django_intro 폴더 내에서 진행

# 파이썬 버전 확인
# 반드시 3.7 버전이 맞는지 확인
$ python -V
Python 3.7.4

# 가상환경 생성
# -m : 모듈 사용, venv라는 모듈을 사용하고, venv라는 가상환경 폴더를 만들 것.
$ python -m venv venv

# 가상환경 적용
$ source venv/Scripts/activate

# 버전 확인
(venv)  # <- 가상환경 적용 시 git bash에서 해당 환경 이름이 표시됨
$ python -V
Python 3.7.4

# 설치된 모듈 확인
(venv)
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

# pip upgrade 
$ python -m pip install --upgrade pip

$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0
```



------

## VScode 및 기타 셋팅

### VSCode 파이썬 환경 선택

1. vscode extensions에서 `python`과 `Django`  설치
2. `ctrl + shift + P`  -> `python select interpreter` -> 방금 생성한 가상환경 선택 (`.venv\Scripts\python.exe`)
3. kill terminal 후 다시 터미널 켜면, 자동으로 가상환경이 잡힘.
   .vscode/settings.json 파일이 생성되며 터미널에서 자동으로 가상환경이 적용되면 OK

### git.ignore 셋팅

가상환경 설정 자체를 github에 올릴 필요가 없음. 너무 무겁고 많기때문에 
--> 가상환경 설정 방법 및 소스만 올려두고, 다음에 사용할 때 그대로 가상환경 구축해서 사용

1. gitignore.io 접속 -> python, django, visualstudiocode, sindows 선택 후 파일생성, 복사
2. `$ touch .gitignore` 선택 -> 복사했던 코드들 붙여넣기
   195번째 줄에서 vscode밑에 있는 !들 모두 삭제 
   (gitignore파일도 안올리고싶으면 추가하기)

### VSCode Django 기본 환경 셋팅

```json
// .vscode파일 -> setting.json폴더에 붙여넣기
// extension -> Django검색하면 밑에 코드가 나온다.

{
    // 파이썬 환경 선택  (자동으로 설정됨)
    "python.pythonPath": "venv\\Scripts\\python.exe",

    // Django에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    
    // django-html에서도 일반 html emmet을 적용 (ex. h1, !+tap ....)
    "emmet.includeLanguages": {"django-html": "html"},

    // django-html에서 tab size를 2칸으로 고정
    "[django-html]": {
        "editor.tabSize": 2
    }
}
```



------

## Start Django project

```bash
# 가상환경(venv)이 잘 잡혀있는지 확인 후, Django 설치하기
(venv)
$ pip install django

$ pip list
Package    Version
---------- -------
Django     2.2.4
pip        19.2.2
pytz       2019.2
setuptools 40.8.0
sqlparse   0.3.0
```

- 장고를 설치한 순간부터 django-admin 이라는 command를 사용할 수 있게 된다.
- 이 command를 통해 django profect에 여러가지 명령을 할 수 있다.

```bash
$ django-admin startproject django_intro .  # 띄어쓰기 한칸 주의
# 현재 디렉토리에서 django_intro라는 이름으로 프로젝트를 시작하겠다.
# django_intro라는 폴더와 manage.py 가 만들어져야함

```

- Django project naming
  - (-)캐릭터는 사용될 수 없다
  - python과 django에서 이미 사용되는 이름은 사용하지 않는다.
    (django라는 이름은 django 그 자체와 충돌이 발생하며, test라는 이름도 django 내부적으로 사용하는 모듈임)
- django-admin startproject 프로젝트이름 .  
  --> .을 안붙이면 새로운 폴더가 만들어짐.

------

## Runserver

```bash
$ python manage.py runserver
```

- `ctrl + c `로 종료
- 기본적으로 localhost : 8000에서 실행됨

