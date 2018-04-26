
# Дополнительные полезные функции при работе с полученным контентом


import json


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
