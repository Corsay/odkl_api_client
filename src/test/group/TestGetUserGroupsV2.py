from src.main.utils.ContentUtils import print_content
from src.main.ApiClient import ApiClient
from src.main.group.GetUserGroupsV2 import GetUserGroupsV2


class TestGetUserGroupsV2:
    """
    Тест-кейсы класса GetUserGroupsV2
    """

    def __init__(self):
        self.test_get_user_groups_v2()

    def test_get_user_groups_v2(self):
        # Пример вызова
        api_client = ApiClient()
        api_request = GetUserGroupsV2()
        api_client.process_request(api_request=api_request)
        print_content(api_request.content, 'json')


if __name__ == '__main__':
    TestGetUserGroupsV2()
