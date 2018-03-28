from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

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

        """
        self.assertTrue(response.content.startswith(b'<html>'))
        # response의 내용(content)이 '<html>'로 시작하는지 확인
        # responese.content는 byte 형이므로 문자열을 바이트로 변환해서 비교!!
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        # endswith은 해당 문자열로 끝나는지 확인하는 것!! (정규식 '문자열$'과 비슷)
        # html 파일 마지막에 Enter 누르고 공백 추가하면 에러 발생한다
        # 그러면 content.strip() 해서 공백 제거해줘야 됨
        """

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
        request = HttpRequest()
        request.method = 'POST'  # 메소드 형태가 'POST' 형인지 확인
        request.POST['item_text'] = '신규 작업 아이템'
        # 지금 사용자가 '신규 작업 아이템'이라고 입력하고 서버에 보낸 거임

        response = home_page(request)
        # 지금 home_page가 이제 request를 받아서 처리를 해주어야 한다.
        # 만일 안되있으면 home_page에 구현을 해줘야 한다는 것!!

        self.assertIn('신규 작업 아이템', response.content.decode())
        # 사용자가 입력했을 시 이것이 실제 반영 되있는지 확인






