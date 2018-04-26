from src.main.utils.ContentUtils import print_content
from src.main.ApiClient import ApiClient
from src.main.users.GetInfoBy import GetInfoBy


class TestGetInfoBy:
    """
    Тест-кейсы класса GetInfoBy
    """

    def __init__(self):
        self.test_get_info_by()

    def test_get_info_by(self):
        # Пример вызова
        api_client = ApiClient()
        api_request = GetInfoBy(uid='*', fields='*')  # в uid поставьте интересующий uid пользователя, к примеру свой
        api_client.process_request(api_request=api_request)
        print_content(api_request.content, 'json')


if __name__ == '__main__':
    TestGetInfoBy()
