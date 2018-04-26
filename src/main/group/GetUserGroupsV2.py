from src.main.ApiRequest import ApiRequest


class GetUserGroupsV2(ApiRequest):
    """
    Запрос 'group.getUserGroupsV2' к API одноклассников (Сессия опциональна (для External (Внешних) приложений - обязательна))
    # Получение списка групп пользователя
    Дополнительные параметры:
        _format - формат выгрузки данных (по-умолчанию json)
        uid - Идентификатор пользователя, список групп которого необходимо получить (по-умолчанию пустое)
        anchor - Идентификатор постраничного вывода (по-умолчанию пустое)
        direction - Направление постраничного вывода (по-умолчанию пустое)
        count - Количество возвращаемых результатов (по-умолчанию пустое)
    """

    def __init__(self, _format='json', fields='user.*'):
        super().__init__()
        self.set_method("group.getUserGroupsV2")
        self.add_param("format", _format)
        self.add_param("fields", fields)
