from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # AttributeError: 'NoneType' object has no attribute 'content'
    # 이 오류가 나오므로 일단 반환한다.
    # 그런 다음 조건을 만족시키면서 매개변수 값을 추가 시킨다.

    return render(request, 'home.html')
    # refactoring 과정!!
    # HttpRespone 객체를 render을 이용해 반환한다.
    # 두번 째 인수는 'settings.py'에 등록되 있는 app 디렉토리 내 templates
    # 디렉토리에 들어가서 해당되는 html 파일을 찾는다


