from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item

# Create your tests here.


class HomePageTest(TestCase):
    def test_url_resolves_to_home_page(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)
        # 문제: 해당 url이 view 함수와 연결이 되는지 확인해야 한다.
        # resolve 함수로 해당 주소로 매핑이 되는 함수를 알 수 있다
        # 그것이 view 함수와 일치하는지 보면 된다.
        # 즉, view 함수를 만들고, url로 연결시켜야 함!!

    def test_home_page_returns_correct_html(self):
        # 문제: HTML 형식의 실제 응답을 반환하는 함수를 확인해야 한다.
        request = HttpRequest()  # HttRequest()로 사용자가 보내는 요청을 반환
        response = home_page(request)  # 뷰 함수에 기본
        # 매개변수인 request를 전달해야 한다. 이 정도는 알지?
        # 반환되는 것은 HttpResponse라는 클래스의 인스턴트 이다.
        # 즉, 사용자에게 보내주는 출력 값이라는 이야기!! (template 호출이 안되는 것!!)

        '''
        self.assertTrue(response.content.startswith(b'<html>'))
        # response의 내용(content)이 '<html>'로 시작하는지 확인
        # responese.content는 byte 형이므로 문자열을 바이트로 변환해서 비교!!
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        # endswith은 해당 문자열로 끝나는지 확인하는 것!! (정규식 '문자열$'과 비슷)
        # html 파일 마지막에 Enter 누르고 공백 추가하면 에러 발생한다
        # 그러면 content.strip() 해서 공백 제거해줘야 됨
        '''

        expected_html = render_to_string("home.html")
        # html 파일을 가져오는 것은 render() 함수와 비슷하다.
        # 해당 html 파일을 문자열 형태 객체로 반환!!

        self.assertEqual(response.content.decode(), expected_html)

        # refactoring 과정
        # html content를 바이트로 비교하지 말고 'render_to_string'을 이용하면
        # html 파일을 문자열 그대로 비교 가능하다.
        # 반환되는 Httpresponse 파일을 decode()로 문자열로 변환
        # 위 코드는 home.html이 정적 파일이기 때문에 상세 사항은 검사 하지 않는다.
        # 그저 home_page 함수가 옳바른 html 파일을 가리키고 있는지만 확인 한다는 것!!
        # 대신 값이 변할 때마다 다르게 출력하는 동적 html 파일은 테스트 해줘야 한다!!

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()  # 홈페이지로 들어와서 사용자의 요청을 받는다.
        request.method = 'POST'  # 메소드 형태는 'POST'로 날라온다.
        request.POST['item_text'] = '신규 작업 아이템'
        # 지금 사용자가 '신규 작업 아이템'이라고 입력하고 서버에 보낸 거임

        response = home_page(request)
        # 지금 home_page가 이제 request를 받아서 처리를 해주어야 한다.
        # 만일 안되있으면 home_page에 구현을 해줘야 한다는 것!!

        self.assertEqual(Item.objects.count(), 1)
        # 사용자가 POST 요청으로 Item 입력 했는지 확인
        # 위에서 1개 넣었으니 개수 확인

        new_item = Item.objects.first()
        # 1개 넣었으므로, 첫번 째 아이템 갖고오고
        # Item.objects.all()[0]과 같이 쓸 수 있음

        self.assertEqual(new_item.text, '신규 작업 아이템')
        # 옳바르게 text를 넣어 요청을 할 수 있는지 확인

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'
        # 얘도 POST로 text 값 넣어주어야 한다. 왜냐하면, 진행 과정이
        # POST 처리를 하고 다시 루트 url로 redirect를 해주는지 확인
        # 해주는 것이기 때문!!

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        # status_code 란 말이 그 자체의 코드를 얘기하는 것 보다는 지금 response가
        # 어떤 상태인지를 나타내준 것!!
        # 302는 redirection 완료라는 것이다.

        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        # home_page 처리를 거치고, 현재 위치가 루트 주소인지 확인!!
        # 즉, redirect가 옳바르게 됐냐 이거지!!

        '''
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'}
        )
        # 현재 html 파일에 내가 값을 임의로 주고 나온 결과 값
        '''
        # redirect 처리를 해주기 때문에, 요청 확인을 해줄 필요 없음!!

        # render_to_string으로 html 파일 문자열로 가져오는데, dictionary 형태로
        # 두번 째 인자 context로 들어감. 키 값에 해당하는 값에다가 넣어줄 수 있음
        # 사용자가 보내온 request(이것도 내가 임의로 줘서 보내온 것)에 따라서
        # home_page를 거쳐 반환되는 response(html 파일 코드)와 그냥 html 파일
        # 변수에 값을 넣은 html 코드가 일치하는지 확인!!

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        # 잘 보자. 지금 request를 줄 때 POST로 주지도 않고,
        # 입력하지도 않은거다. 즉, 비어 있는 요청은 처리하지 않는 지를 확인!!

        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        request = HttpRequest()
        # 매개변수로 request를 주어야 하니깐 일단 임의로 호출을 받는 것!!
        response = home_page(request)
        # 이제 home_page에서 데이터베이스에서 꺼내와서, 출력이 된채로 반환 됐겠지!!

        self.assertIn('itemy 1', response.content.decode())
        self.assertIn('itemy 2', response.content.decode())

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_items = Item.objects.all()
        # Django는 디폴트로 모든 모델 클래스에 대해 'objects'라는 Manager 객체를
        # 자동으로 추가한다. 이 Manager 객체를 통해 특정 데티러를 필터링 하고 정렬 하는 등
        # 여러 기능들을 사용 가능하다.

        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')