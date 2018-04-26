
### Клиент к API одноклассников
# полезный материал - https://apiok.ru/dev/methods/

import requests
import json
import hashlib


application_key = 'Your'
application_secret_key = 'Your'
access_token = 'Your'	# токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")


"""
	Функция для подсчета md5
	Обязательные параметры:
		строка
	Результаты:
		md5 хэш
"""
def md5sum(string):
    md5 = hashlib.md5()
    md5.update(bytes(string,"UTF-8"))
    return md5.hexdigest()


"""
	Функция для проверки основных параметров
	Обязательные параметры:
		отсутствуют
	Результаты:
		статус проверки:
			0 - всё отлично
			сообщение - сообщение об ошибке
"""
def check_params():
	if len(application_key) == 0:
		return "Application key should be specified"
	if len(application_secret_key) == 0:
		return "Application secret key should be specified"
	if len(access_token) == 0:
		return "Access token should be specified"


"""
	Функция для печати полученного контента
	Обязательные параметры:
		content - содержимое для печати
		_format - формат содержимого (json, xml, unknown)
	Результаты:
		Печать контента на экран
"""
def print_content(content, _format):
	if _format == 'json':
		content_json = json.loads(content)
		content_json = json.dumps(content_json, indent=4, ensure_ascii=False)
		print(content_json + "\n")
	elif _format == 'xml':
		print("XML not included")
		print(content)
		print("")
	else:
		print(content)
		print("")


"""
	Функция запрашивающее данные по users.getCurrentUser методу API одноклассники (Сессия обязательна)
	# Получение информации о текущем пользователе
	Обязательные параметры:
		application_key - ключ приложения
		application_secret_key - секретный ключ приложения
		access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
	Дополнительные параметры:
		_format - формат выгрузки данных (по-умолчанию json)
		_fields - список запрашиваемых полей (по-умолчанию пустое)
	Результаты:
		вывод на экран результата запроса (согласно запрошенному формату)
"""
def users_getCurrentUser(application_key, application_secret_key, access_token, _format = 'json', _fields = ''):
	# проверка некоторых параметров
	msg = check_params()
	if msg: return msg
	# формирование словаря параметров
	params = {
		'application_key': application_key,
		'fields': _fields,
		'format': _format,
		'method': 'users.getCurrentUser',
	}
	content = send_request(params, application_secret_key, access_token)
	# вывод результата пользователю
	print_content(content, _format)


"""
	Функция запрашивающее данные по users.getInfoBy методу API одноклассники (Сессия обязательна)
	# Возвращает большой массив информации, связанной с пользователем, с учетом его связи с вызывающим юзером
	Обязательные параметры:
		application_key - ключ приложения
		application_secret_key - секретный ключ приложения
		access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
		_uid - идентификатор пользователя, информацию о котором требуется получить
		_fields - список запрашиваемых полей
	Дополнительные параметры:
		_format - формат выгрузки данных (по-умолчанию json)
		_register_as_guest - отмечать как заход в гости, по умолчанию true
	Результаты:
		вывод на экран результата запроса (согласно запрошенному формату)
"""
def users_getInfoBy(application_key, application_secret_key, access_token, _uid, _fields, _format = 'json', _register_as_guest = ''):
	# проверка некоторых параметров
	msg = check_params()
	if msg: return msg
	# формирование словаря параметров
	params = {
		'application_key': application_key,
		'fields': _fields,
		'format': _format,
		'method': 'users.getInfoBy',
		'register_as_guest': _register_as_guest,
		'uid': _uid,
	}
	content = send_request(params, application_secret_key, access_token)
	# вывод результата пользователю
	print_content(content, _format)


"""
	Функция запрашивающее данные по group.getUserGroupsV2 методу API одноклассники (Сессия опциональна (для External (Внешних) приложений - обязательна))
	# Получение списка групп пользователя
	Обязательные параметры:
		application_key - ключ приложения
		application_secret_key - секретный ключ приложения
		access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
	Дополнительные параметры:
		_format - формат выгрузки данных (по-умолчанию json)
		_uid - Идентификатор пользователя, список групп которого необходимо получить (по-умолчанию пустое)
		_anchor - Идентификатор постраничного вывода (по-умолчанию пустое)
		_direction - Направление постраничного вывода (по-умолчанию пустое)
		_count - Количество возвращаемых результатов (по-умолчанию пустое)
	Результаты:
		вывод на экран результата запроса (согласно запрошенному формату)
"""
def group_getUserGroupsV2(application_key, application_secret_key, access_token, _format = 'json', _uid = '', _anchor = '', _direction = '', _count = ''):
	# проверка некоторых параметров
	msg = check_params()
	if msg: return msg
	# формирование словаря параметров
	params = {
		'anchor': _anchor,
		'application_key': application_key,
		'count': _count,
		'direction': _direction,
		'format': _format,
		'method': 'group.getUserGroupsV2',
		'uid': _uid,
	}
	content = send_request(params, application_secret_key, access_token)
	# вывод результата пользователю
	print_content(content, _format)


"""
	Функция запрашивающее данные по group.getInfo методу API одноклассники (Сессия опциональна (для External (Внешних) приложений - обязательна))
	# Получение информации о группах
	Обязательные параметры:
		application_key - ключ приложения
		application_secret_key - секретный ключ приложения
		access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
		_uids - Список идентификаторов групп, разделённых запятой, о которых нужно запросить информацию
		_fields - Список запрашиваемых полей
	Дополнительные параметры:
		_format - формат выгрузки данных (по-умолчанию json)
		_move_to_top - Если вызов происходит от имени пользователя, а пользователь состоит в запрашиваемой группе,
			то данная группа перемещается на верх в списке групп пользователя. Имеет смысл, только если запрашиваемая группа единственная. По умолчанию false.
	Результаты:
		вывод на экран результата запроса (согласно запрошенному формату)
"""
def group_getInfo(application_key, application_secret_key, access_token, _uids, _fields, _format = 'json', _move_to_top = ''):
	# проверка некоторых параметров
	msg = check_params()
	if msg: return msg
	# формирование словаря параметров
	params = {
		'application_key': application_key,
		'fields': _fields,
		'format': _format,
		'method': 'group.getInfo',
		'move_to_top': _move_to_top,
		'uids': _uids,
	}
	content = send_request(params, application_secret_key, access_token)
	# вывод результата пользователю
	print_content(content, _format)


"""
	Функция отправляющая запрос к методу API одноклассники
	Обязательные параметры:
		params - параметры которые необходимо передать методу API
		application_secret_key - секретный ключ приложения
		access_token - токен доступа (https://apiok.ru/dev/app/create в блоке "Получение токенов доступа для создателя приложения")
	Результаты:
		Ответ API одноклассников или ошибку
"""
def send_request(params, application_secret_key, access_token):
	paramsKeyValue = ""
	concatenation = ""
	for k, val in params.items():
		if paramsKeyValue != "":
			paramsKeyValue += "&" + k + "=" + val
		else:
			paramsKeyValue += k + "=" + val
		concatenation += k + "=" + val

	secret_key = md5sum(access_token + application_secret_key)
	concatenation += secret_key
	sig = md5sum(concatenation)
	url = 'https://api.ok.ru/fb.do?' + paramsKeyValue + '&sig=' + sig + "&access_token=" + access_token

	# Дополнительная полезная информация
	# print("params = " + paramsKeyValue)
	# print("secret_key = " + secret_key)
	# print("concatenation = " + concatenation)
	# print("sig = " + sig)
	# print("url = " + url + "\n")

	# отравляем запрос
	try:
		response = requests.get(url, timeout=30)
		response.raise_for_status() # если получено не 200 Ок
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


if __name__ == "__main__":
	_fields = '*'
	_format = 'json'

	# Примеры вызовов
	users_getCurrentUser(
		application_key = application_key,
		application_secret_key = application_secret_key,
		access_token = access_token,
		_fields = _fields,
		_format = _format)


	_uid = '*'	# ID пользователя (подробнее в описании функции)
	users_getInfoBy(
		application_key = application_key,
		application_secret_key = application_secret_key,
		access_token = access_token,
		_uid = _uid,
		_fields = _fields,
		_format = _format)

	group_getUserGroupsV2(
		application_key = application_key,
		application_secret_key = application_secret_key,
		access_token = access_token,
		_format = _format)

	_uids = '53038939046008'	# ID групп (через запятую) (подробнее в описании функции)
	group_getInfo(
		application_key = application_key,
		application_secret_key = application_secret_key,
		access_token = access_token,
		_fields = _fields,
		_format = _format,
		_uids = _uids)
