from src.main.utils.ContentUtils import print_content
from src.main.ApiClient import ApiClient
from src.main.users.GetCurrentUser import GetCurrentUser


class TestGetCurrentUser:
    """
    Тест-кейсы класса GetCurrentUser
    """

    def __init__(self):
        self.test_get_current_user()

    def test_get_current_user(self):
        # Пример вызова
        api_client = ApiClient()
        content = api_client.process_request(api_request=GetCurrentUser())
        print_content(content, 'json')


if __name__ == '__main__':
    TestGetCurrentUser()
