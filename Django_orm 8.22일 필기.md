# Django_orm <8.22일>

### 기초설정

- shell

  ```bash
  $ python manage.py shell
  ```

  파이썬 쉘을 실행시키는 것. 이렇게 실행시켜야 우리가 만든 장고_orm에 접근가능하다.  (장고 모듈 + 파이썬이 있어야함)

- import model

  ```python
  >>> from articles.models import Article
  ```

- DB 접근

  ```python
  >>> Article.objects.all()
  >>> <QuerySet []>  # (현재 아무 정보도 없음)
  ```

  Article: 우리가 만든 모델. (= class)
  objects: DB에 접근하도록 명령을 내리게 할 수 있는 객체
  => Article.objects 명령을 통해 Article에 명령을 내릴 것임.

**데이터를 저장하는 3 가지 방법**

1. 첫 번째 방식

   - ORM 을 쓰는 이유 => DB를 조작하는 것을 객체지향 프로그래밍(클래스) 처럼 하기 위해서.

     ```python
     # article 생성 (클래스처럼 생성)
     >>> article = Article()
     >>> article
     <Article: Article object (None)>
     
     # article에 정보 넣기
     >>> article.title = "First article"
     >>> article.content = "Hello, article?"
     
     # article확인
     >>> article.title
     'First article'
     >>> article.content
     'Hello, article?'
     
     # 데이터 저장
     >>> article.save()
     >>> article
     <Article: Article object (1)>
         
     ```

     ```python
     # article DB확인
     # ctrl + shift + p => sqlite => articles_article 화살표 클릭
     ```

2. 두 번째 방법

   - 함수에서 keyword 인자 넘기는 방식과 동일

   ```python
   # 아티클 생성 -> 타이틀, 내용 입력 -> 저장 (X)
   # 아티클 생성과 동시에 타이틀, 내용입력 -> 저장
   >>> article = Article(title='Second article', content='Hihi')
   >>> article.save()
   
   >>> article
   <Article: Article object (2)>
   ```

3. 세 번째 방법

   - create()를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스탭

     ```python
     >>> Article.objects.create(title='Third article', content='goodgood')
     <Article: Article object (3)>
     ```

4. 검증

   - full_clean()을 통해 save()하기 적합한 ~인지 확인할 수 있다.

   ```python
   >>> article.title = 'Python is good'
   >>> article.content
   ''
   # title만 있고 content는 없음
   
   >>> article.full_clean()
   Traceback (most recent call last):
     File "<console>", line 1, in <module>
     File "C:\Users\student\0_development\django\django_orm_crud\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
       raise ValidationError(errors)
   django.core.exceptions.ValidationError: {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
   ```

# Read

### 객체 표현 변경

```python
$ python manage.py shell
# python shell open

>>> from articles.models import Article
# models.py의 class Article() 임포트

>>> Article.objects.all()
<QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - Second article :
Hihi>, <Article: 3번 글 - Third article : goodgood>, <Article: 4번 글 - Nonearticle : >]>

''' 표현방식 변경
    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'
'''
```

### 모든 객체

```python
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

# 모든 게시글 리스트를 보여줄 수 있음
# ID = Primary Key = (1), (2) ..
```

- DB에 저장된 글 중에서 title이 second인 글만 가지고 오기

```python
>>> Article.objects.filter(title='Second article')
<QuerySet [<Article: 2번 글 - Second article : Hihi>]>

# 쿼리셋 형태로 가지고와진다.
# 타이틀이 second인 모든 아티클을 가지고 오기 때문에 (이후에는 하나가 아닐 수 있음) 복수형의 형태인 쿼리셋 형태로 출력
```

```python
# title이 second article인 글 하나 더 작성
>>> Article.objects.create(title='Second article', content='Two')
<Article: 5번 글 - Second article : Two>

>>> Article.objects.filter(title='Second article')
<QuerySet [<Article: 2번 글 - Second article : Hihi>, <Article: 5번 글 - Second article : Two>]>
```

- DB에 저장된 글 중에서 title인 Second article인 글 중에서 첫번째만 가지고 오기

```python
>>> queryset = Article.objects.filter(title='Second article')
>>> queryset
<QuerySet [<Article: 2번 글 - Second article : Hihi>, <Article: 5번 글 - Second article : Two>]>
>>> queryset.first()
<Article: 2번 글 - Second article : Hihi>
----------
>>> Article.objects.filter(title='Second article').first()
<Article: 2번 글 - Second article : Hihi>
```

- DB에 저장된 글 중에서 PK가 1인 글만 가지고 오기
  PK만 get()으로 가지고 올 수 있다.
  get()은 오로지 하나만 존재하는 값을 가지고 올 수 있음.

```python
# Primary Key = ID - (1), (2) ..
>>> Article.objects.get(pk=1)
<Article: 1번 글 - First article : Hello, article?>
```

- 오류상황

```python
# 없는 값 가지고 오기
>>> Article.objects.get(pk=19)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\0_development\django\django_orm_crud\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\0_development\django\django_orm_crud\venv\lib\site-packages\django\db\models\query.py", line 408, in get
    self.model._meta.object_name
articles.models.Article.DoesNotExist: Article matching query does not exist.

# 중복된 값 호출
>>> Article.objects.get(title='Second article')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\0_development\django\django_orm_crud\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\0_development\django\django_orm_crud\venv\lib\site-packages\django\db\models\query.py", line 412, in get
    (self.model._meta.object_name, num)
articles.models.Article.MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

- filter 는 에러를 내지 않음

```python
# 중복 가능
>>> Article.objects.filter(title="Second article")
<QuerySet [<Article: 2번 글 - Second article : Hihi>, <Article: 5번 글 - Second article : Two>]>
# 없는 값 가능 (빈 쿼리셋 반환)
>>> Article.objects.filter(pk=10)
<QuerySet []>
```

- 원하는 값 가져오기

```python
# 원하는 값 선택
>>> article = Article.objects.get(pk=1)
>>> article.title
'First article'

# 오름차순
>>> articles = Article.objects.order_by('pk')
>>> articles
<QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - Second article :
Hihi>, <Article: 3번 글 - Third article : goodgood>, <Article: 4번 글 - Nonearticle : >, <Article: 5번 글 - Second article : Two>]>

# 내림차순
>>> articles = Article.objects.order_by('-pk')
>>> articles
<QuerySet [<Article: 5번 글 - Second article : Two>, <Article: 4번 글 - Nonearticle : >, <Article: 3번 글 - Third article : goodgood>, <Article: 2번 글 - Second article : Hihi>, <Article: 1번 글 - First article : Hello, article?>]>

# 쿼리셋은 리스트처럼 인덱스 접근이 가능함
>>> article = articles[2]
>>> article
<Article: 3번 글 - Third article : goodgood>

>>> articles = Article.objects.all()[1:3]
>>> articles
<QuerySet [<Article: 2번 글 - Second article : Hihi>, <Article: 3번 글 - Third article : goodgood>]>

```

- LIKE - 문자열을 포함하고 있는 값을 가지고 옴
  장고 ORM은 이름과 필터를 더블 언더스코어(__)로 구분함

```python
>>> articles = Article.objects.filter(title__contains='Sec')
>>> articles
<QuerySet [<Article: 2번 글 - Second article : Hihi>, <Article: 5번 글 - Second article : Two>]>
```

- startswith

```python
>>> articles = Article.objects.filter(title__startswith='First')
>>> articles
<QuerySet [<Article: 1번 글 - First article : Hello, article?>]>
```

- endswith

```python
>>> articles = Article.objects.filter(content__endswith='good')
>>> articles
<QuerySet [<Article: 3번 글 - Third article : goodgood>]>
```

# Delete

```python
>>> articles = Article.objects.filter(title__startswith='First')
>>> articles.delete()
(1, {'articles.Article': 1})
```

# Update

article 인스턴스 호출 후 값 변경하여 .save()함수 실행

```python
# 빈 아티클 컨텐츠에 내용 채우기
>>> article = Article.objects.get(pk=4)
>>> article.content
''
>>> article.content='new contents'
>>> article.save()
```



-----------

---------

articles/ 경로로 들어올 시, articles앱의 urls.py로 이동시킴

1. crud.urls

   ```python
   from django.urls import path, include
   
   urlpatterns = [
       # articles/ 경로로 들어올 시, articles앱의 urls.py로 이동시킴
       path('articles/', include('articles.urls')),
       path('admin/', admin.site.urls),
   ]
   ```

2. articles 폴더 -> ulrs.py 파일 만들기

   ```python
   from django.urls import path
   from . import views
   
   # articles/_____
   urlpatterns = [
       path('index/', views.index),
   ]
   ```

3. view함수 만들기  -> views.py 로 이동

   ```python
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', context)
   ```

4. index.html 만들기

   ```django
   <!-- articles -> templaes 폴더 -> articles 폴더 -> index.html -->
   <!-- articles/index.html로 접근하기 때문 -->
   
   {% extends 'base.html' %}
   
   {% block title %}Article Index{% endblock %}
   
   {% block content %}
     <h1>Articles List</h1>
     
     <ul>
       {% for article in articles %}
       <li>{{ article.title }}</li>
       {% endfor %}
     </ul>
   {% endblock %}
   ```

   