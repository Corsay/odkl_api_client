import requests
import hashlib


class ApiClient:
    """
    Клиент к API одноклассников
    """

    """
        Порядок параметров (для отправки в API - важно при вычислении md5):
        application_key
        fields
        format
        method
        register_as_guest
        uid
        uids
        ********SECRET KEY*******
    """
    FIELDS = ['application_key', 'fields', 'format', 'method', 'register_as_guest', 'uid', 'uids']
    API_URL = 'https://api.ok.ru/fb.do?'
    APPLICATION_KEY = None
    APPLICATION_SECRET_KEY = None
    ACCESS_TOKEN = None

    def __init__(self, api_url=API_URL, app_key=APPLICATION_KEY, app_secret_key=APPLICATION_SECRET_KEY, access_token=ACCESS_TOKEN):
        self.api_url = api_url
        self.app_key = app_key
        self.app_secret_key = app_secret_key
        self.session_secret_key = app_secret_key
        self.access_token = access_token

    """
    Функция отправки на обработку запроса
    Обязательные параметры:
        запрос
    Результат:
        контент
    """
    def process_request(self, api_request):
        # валидация основных параметров
        if self.app_key is None or len(self.app_key) == 0: raise Exception("Некорректный app_key")
        if self.app_secret_key is None or len(self.app_secret_key) == 0: raise Exception("Некорректный app_secret_key")
        # выполнение запроса
        api_request.add_param('application_key', self.app_key)
        api_request.content = self.send_request(api_request.params, self.app_secret_key, self.access_token)
        # возврат результата
        return api_request.content

    """
    Функция для подсчета md5
    Обязательные параметры:
        строка
    Результаты:
        md5 хэш
    """
    def md5sum(self, string):
        md5 = hashlib.md5()
        md5.update(bytes(string, "UTF-8"))
        return md5.hexdigest()

    """
    Функция отправляющая запрос к методу API одноклассники
    Обязательные параметры:
        params - параметры которые необходимо передать методу API
        application_secret_key - секретный ключ приложения
        access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
    Результаты:
        Ответ API одноклассников или ошибку
    """
    def send_request(self, params, application_secret_key, access_token):
        # формируем параметры к текущему запросу (и строку конкатенации)
        params_key_value = ""
        concatenation = ""
        for key in self.FIELDS:
            if key in params:
                if params_key_value != "":
                    params_key_value += "&" + key + "=" + params[key]
                else:
                    params_key_value += key + "=" + params[key]
                concatenation += key + "=" + params[key]

        secret_key = self.md5sum(access_token + application_secret_key)
        concatenation += secret_key
        sig = self.md5sum(concatenation)
        url = 'https://api.ok.ru/fb.do?' + params_key_value + '&sig=' + sig + "&access_token=" + access_token

        # отравляем запрос
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # если получено не 200 Ок
        except requests.Timeout:
            error = "ошибка timeout, url: " + url
            return error
        except requests.HTTPError as err:
            code = err.response.status_code
            error = "ошибка url: {0}, code: {1}".format(url, code)
            return error
        except requests.RequestException:
            error = "ошибка скачивания url: " + url
            return error
        else:
            return response.content
