class ApiRequest:
    """
    Запрос к API одноклассников
    """

    def __init__(self):
        self.params = {}
        self.content = None

    def set_method(self, method):
        self.add_param("method", method)

    def add_param(self, param, value):
        self.params[param] = value
