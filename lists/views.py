from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
    # AttributeError: 'NoneType' object has no attribute 'content'
    # 이 오류가 나오므로 일단 반환한다.
    # 그런 다음 조건을 만족시키면서 매개변수 값을 추가 시킨다.
