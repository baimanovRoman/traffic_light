from app import app
from config import BASE_PORT, BASE_HOST


def get_setting():
    dict_setting: dict = {}
    host = input('Enter to host or enter default (127.0.0.1): ')
    port = input('Enter to port or enter default (9999): ')
    dict_setting['host'] = host if host != "" else BASE_HOST
    dict_setting['port'] = port if port != "" else BASE_PORT
    return dict_setting


if __name__ == '__main__':
    setting = get_setting()
    app.run(debug=False, host=setting.get('host'),  port=setting.get('port'), threaded=True)
