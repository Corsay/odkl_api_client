from src.main.ApiRequest import ApiRequest


class GetInfoBy(ApiRequest):
    """
    Запрос 'users.getInfoBy' к API одноклассников (Сессия обязательна)
    # Возвращает большой массив информации, связанной с пользователем, с учетом его связи с вызывающим юзером
    Обязательные параметры:
        application_key - ключ приложения
        application_secret_key - секретный ключ приложения
        access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
        uid - идентификатор пользователя, информацию о котором требуется получить
        fields - список запрашиваемых полей
    Дополнительные параметры:
        _format - формат выгрузки данных (по-умолчанию json)
        register_as_guest - отмечать как заход в гости, по умолчанию true
    """
    def __init__(self, uid, fields, _format='json', register_as_guest=''):
        super().__init__()
        self.set_method("users.getInfoBy")
        self.add_param("uid", uid)
        self.add_param("fields", fields)
        self.add_param("format", _format)
        self.add_param("register_as_guest", register_as_guest)
