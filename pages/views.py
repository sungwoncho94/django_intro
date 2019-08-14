from django.shortcuts import render
import random


def index(request):  # 첫번째 인자는 반드시 request가 온다 -> 사용자가 보내는 요청에 대한 정보가 있음.
    # 요청이 들어오면 index.html을 보여준다.
    return render(request, 'index.html')  # render의 첫번째 인자 = request / 두번째 인자 = 사용자한테 보여줄 페이지


def introduce(request):
    return render(request, 'introduce.html')


# template Variable Example
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick
    }

    # Django template으로 context전달
    return render(request, 'dinner.html', context)
    