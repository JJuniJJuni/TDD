from django.http import HttpResponse
from lists.models import Item
from django.shortcuts import render

# Create your views here.


def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # AttributeError: 'NoneType' object has no attribute 'content'
    # 이 오류가 나오므로 일단 반환한다.
    # 그런 다음 조건을 만족시키면서 매개변수 값을 추가 시킨다.
    """
    if request.method == "POST":
        return HttpResponse(request.POST["item_text"])
        # HttpRespone의 매개변수에는 html 파일 형식으로 들어간다는 것을 생각하자
        # 단순히 render(request, 'home.html') 해버리면, 홈페이지 자체를 출력시키는 것!!
        # 입력 처리를 해주어야 함!!
    """
    item = Item()
    item.text = request.POST.get('item_text', '')
    # 사용자로부터 Item input requect를 POST method로 받는다.
    item.save()
    # 전달 받은 Item을 데이터베이스에 저장

    return render(request, 'home.html', {
        'new_item_text': item.text
    })
    # [1]
    # refactoring 과정!!
    # HttpResponse 객체를 render을 이용해 반환한다.
    # 두번 째 인수는 'settings.py'에 등록되 있는 app 디렉토리 내 templates
    # 디렉토리에 들어가서 해당되는 html 파일을 찾는다

    # [2]
    # render로 리팩토링!! POST 요청처리를 조건문을 제거하고 해주는 것!!
    # 없을 시에 빈 공백으로 에러 방지!!
    # request.POST를 하면 사전 형태로 리턴이 된다.
    # request에서 POST.get을 하고 입력 받은 것을 context로 넘긴다는 거지!!

    # [3]
    # 이미 위에서 POST.get 처리를 해줬으므로, 굳이 render에서 해줄 필요가 없다.

