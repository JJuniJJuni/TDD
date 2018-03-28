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

        self.assertTrue(response.content.startswith(b'<html>'))
        # response의 내용(content)이 '<html>'로 시작하는지 확인
        # responese.content는 byte 형이므로 문자열을 바이트로 변환해서 비교!!
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        # endswith은 해당 문자열로 끝나는지 확인하는 것!! (정규식 '문자열$'과 비슷)

