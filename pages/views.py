from django.shortcuts import render
from datetime import datetime
import random



def index(request):  # 첫번째 인자는 반드시 request가 온다 -> 사용자가 보내는 요청에 대한 정보가 있음.
    # 요청이 들어오면 index.html을 보여준다.
    return render(request, 'index.html')  # render의 첫번째 인자 = request / 두번째 인자 = 사용자한테 보여줄 페이지


def introduce(request):
    return render(request, 'introduce.html')


# template Variable Example
# variable routing으로 'name'을 받아서 context에 'name'도 함께 넣기.
# dinner.html에서 'name'님의 저녁식사는 'pick'입니다
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name' : name
    }
    # Django template으로 context전달
    return render(request, 'dinner.html', context)


def image(request):
    image_url = 'https://picsum.photos/500'
    context = { 
        'image_url': image_url,
        }
    return render(request, 'image.html', context)

# greeting/IU/ -> name에 IU가 들어감
def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def info(request):
    teacher = 'Jason'
    stu1 = 'Sungwon'
    stu2 = 'dalbong'
    stu3 = 'sumin'

    context = {
        'name': teacher,
        'name1': stu1,
        'name2': stu2,
        'name3': stu3,
    }
    return render(request, 'info.html', context)


def student(request, name):
    age = 28
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'student.html', context)


def isitbirthday(request):
    today = datetime.now()
    
    if today.month == 10 and today.day == 31:
        result = 'YESSSSSSSSSSSSSSSSS!'
    else:
        result = 'Noooooooooooooooooo!'

    context = {
        'result': result
    }
    return render(request, 'isitbirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    my_lotto = sorted(list(random.sample(range(1, 46), 6)))
    context = {
        'real_lotto': real_lotto,
        'my_lotto': my_lotto,
    }
    return render(request, 'lotto.html', context)