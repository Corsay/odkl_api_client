from src.main.ApiRequest import ApiRequest


class GetCurrentUser(ApiRequest):
    """
    Запрос 'users.getCurrentUser' к API одноклассников (Сессия обязательна)
    # Получение информации о текущем пользователе
    Дополнительные параметры:
        _format - формат выгрузки данных (по-умолчанию json)
        fields - список запрашиваемых полей (по-умолчанию пустое)
    """

    def __init__(self, _format='json', fields='user.*'):
        super().__init__()
        self.set_method("users.getCurrentUser")
        self.add_param("format", _format)
        self.add_param("fields", fields)
