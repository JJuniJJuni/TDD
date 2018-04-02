from django.http import HttpResponse
from lists.models import Item,List
from django.shortcuts import render, redirect

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
    ''''
    item = Item()
    item.text = request.POST.get('item_text', '')
    # 사용자로부터 Item input requect를 POST method로 받는다.
    item.save()
    # 전달 받은 Item을 데이터베이스에 저장
    '''
    '''
    if request.method == 'POST':
        
        new_item_text = request.POST['item_text']
        # POST 처리 할 때 html에서 정한 name 값으로 해당 필드 값에
        # 접근 가능하다는 것은 이제 알지?
        # 원래 주석 처리 되있던 블럭
        
        # 위의 처리를 매개 변수에다 바로 때려 박아 버리기

        Item.objects.create(text=request.POST['item_text'])
        # Item()로 인스턴트를 안 만들고, create() method를 쓰면
        # 데이터베이스에 저장 가능(간소화 가능)
        return redirect('/lists/the-only-list-in-the-world/')
        # 원래 페이지로 해당 매개변수(루트 url)로 다시 views 함수 호출
    
    else:
        new_item_text = ''
        # 입력 안했을 시에는 빈 공백만 보여주도록!!
        # 이 블럭은 원래 주석 처리 되있던 거다!!
    
    # redirect를 해주었으므로, 굳이 빈 공백 해줄 필요 없지!!

    # POST 입력 요청 처리를 했을 때만 데이터베이스 저장을 해주도록 처리
    # POST 한 뒤에는 항상 redirect를 해주어야 한다는 것을 명시!!

    return render(request, 'home.html')
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
    '''
    return render(request, 'home.html')
    # 이제 다른 html 파일에 기능들을 설정해놨으니 다른건 필요 x


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items
    })


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')