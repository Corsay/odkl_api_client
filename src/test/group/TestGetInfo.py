from src.main.utils.ContentUtils import print_content
from src.main.ApiClient import ApiClient
from src.main.group.GetInfo import GetInfo


class TestGetInfo:
    """
    Тест-кейсы класса GetInfo
    """

    def __init__(self):
        self.test_get_info()

    def test_get_info(self):
        # Пример вызова
        api_client = ApiClient()
        content = api_client.process_request(api_request=GetInfo(uids='53038939046008', fields='*'))
        print_content(content, 'json')


if __name__ == '__main__':
    TestGetInfo()
