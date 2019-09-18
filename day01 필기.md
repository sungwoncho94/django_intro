# 190814_Django_day01

MVC (Model–View–Controller)
모델 : DB (ex. 사용자에 대한 기록, 정보를 가지고만 있음)
view : 요청하는 페이지 (사용자가 보는 화면)
컨트롤러 : 실제 작업, 기능을 수행

쟝고 - MTV패턴 (Model Template View)
모델 : 데이터 관리, 저장
템플릿 : 사용자가 보는 화면
view : 중간관리자 (특정 기능, 작업 수행)

웹 서비스 흐름
: 사용자가 1번 강의를 달라고 요청 -> view가 인식하고 model에게 1번 강의를 찾으라고 명령 -> model에서 찾아서 view에 전달 -> view가 template에 html파일을 넘겨줘서 사용자가 화면을 본다.

어플리케이션 : 로직을 수행  <  어플리케이션을 모아놓은게 프로젝트임

--------------

-------------------

### Settings.py 기본설정

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
# 한글 / 아시아.서울 시간으로 바꿔주기
```



----------------------

### 파일 설명

_ _init_ _.py : 패키지로 인식시키기 위한 빈 파일

django_intro > settings.py : 우리가 만든 어플리케이션을 등록

admin.py : 관리자 페이지를 custormize 하는 곳 (ex. 유저 라는 모델을 만들고  관리자 페이지에서 보고싶으면 유저라는 모델을 이 파일에 등록)

apps.py : 앱에 대한 정보가 입력되는 곳

tests.py : 테스크 코드를 작성하는 페이지.

**models.py** : 어플리케이션에서 사용할 데이터를 저장하는 곳. DB관리

**views.py** : **엄청중요!!!** 어떤 작업들이 실제로 일어나는 함수들을 정의. == view 함수를 정의

**urls.py** : 사용자가 들어올 수 있는 경로를 설정함.

-----------------

### Django 작성 순서

1. `urls.py`에서 사용자가 접속하는 경로와, 해당 페이지를 보여주는 함수(views)를 mapping 시킴
2. `views.py`에서 우리가 보여주고자 하는 페이지 함수 작성
3. `template`을 만든다.

---------------

실습1

localhost : 8000/introduce/

views.introduce로 들어오면, render -> introduce.html을 rendering할 것.

introduce.html
<h.1>자기소개</.h1>

실습2

url : image/

template : image.html

view:

```python
def image(request):
    #image url을 context에 담아서 image.html에 전달한다
```

template : image.html // 전달받은 image url을 img태그 src속성에 담아서 랜덤 이미지를 보여준다.

실습3

url : times/

- variable routing으로 숫자 2개를 각각 int type num1, num2로 받는다.

view:

```python
def times(request, num1, num2):
    # 두 숫자를 곱한 result변수와 num1, num2 를 context에 담아서 times.html에 전달한다.
```

template : times.html

- 전달받은 context의 값들을 알맞게 표시한다.







