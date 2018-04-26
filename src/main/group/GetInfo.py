from src.main.ApiRequest import ApiRequest


class GetInfo(ApiRequest):
    """
    Запрос 'group.getInfo' к API одноклассников (Сессия опциональна (для External (Внешних) приложений - обязательна))
    # Получение информации о группах
    Обязательные параметры:
        uids - Список идентификаторов групп, разделённых запятой, о которых нужно запросить информацию
        fields - Список запрашиваемых полей
    Дополнительные параметры:
        _format - формат выгрузки данных (по-умолчанию json)
        move_to_top - Если вызов происходит от имени пользователя, а пользователь состоит в запрашиваемой группе,
            то данная группа перемещается на верх в списке групп пользователя. Имеет смысл, только если запрашиваемая группа единственная. По умолчанию false.
    """
    def __init__(self, uids, fields, _format='json', move_to_top=''):
        super().__init__()
        self.set_method("group.getInfo")
        self.add_param("uids", uids)
        self.add_param("fields", fields)
        self.add_param("format", _format)
        self.add_param("move_to_top", move_to_top)
