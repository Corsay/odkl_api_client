
# Внести в файл ApiClient.py информацию о своём приложении
	APPLICATION_KEY
    APPLICATION_SECRET_KEY
    ACCESS_TOKEN

# Запуск тестов:
1. через PyCharm community
2. через консоль
    1. зайти в папку с проектом
    2. в начале активировать виртуальное окружение:
        source env/bin/activate
    3. запустить интерпретатор:
        python
    4. выполнить любой тест:
        from src.test.users.TestGetCurrentUser import TestGetCurrentUser
        TestGetCurrentUser()
    5. по завершении деактивировать виртуальное окружение:
        deactivate
