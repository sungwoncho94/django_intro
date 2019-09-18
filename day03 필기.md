# Django_day03 새로운 앱 만들기

앱 이름 : utilities

앱 만들기 : `python manage.py startapp utilities`
출생신고 : `settings.py`  (django_intro 파일)

현재 : 사용자의 요청 -> Django_intro - Urls.py에서 pages로 들어온 요청인지, utilities에 들어온 요청인지 구분함. 

목표 : Django_intro의 urls.py를 pages와 utilities안의 urls.py로 나눌 것. 장고 인트로는 길안내만 하고, 각 앱 내의 urls.py에서 실행할 것.

## 탬플릿 상속

특정 어플리케이션에 종속X, root project에서 만들어서 갖다 쓴다.

(1) 장고_인트로 - templates폴더 - base.html 생성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <title>
  {% block title %}{% endblock %}
  </title>
</head>
<body>
  {% comment %} 다른 html 페이지에서는 base.html을 상속받아 block 안에 내용만 작성 {% endcomment %}
  {% block body %}
  {% endblock %}


  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

사용 예시

```html
{% extends 'base.html' %}

{% block title %}Greeting{% endblock  %}

{% block body %}<h1>{{name}} 안녕!</h1>{% endblock  %}
```





-----------------------



새로 만든 templates를 장고에 인식시키고 싶다면....
BASE_DIR -> crud -> settings.py -> TEMPLATES = [ ] -> DIRS: [ ] 수정

`'DIRS': [os.path.join(BASE_DIR, 'crud.urls', 'templates',)],` 
base_dir + crud의 templates를 합치는 것.

이제 crud의 templates에서도 검색할 수 있다.



