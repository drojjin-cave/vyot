import datetime
import json
from pprint import pprint

import requests
import uuid
from pprint import pprint

class X3_UI:
    def __init__(self):
        login = 'admroot'
        password = 'VasiliyInokentievich2037%'
        self.host = 'http://150.241.69.225:50969'
        self.header = []
        self.data = {"username": login, "password": password}
        self.ses = requests.Session()

        self.test_login()
    # Тестовое соединение
    def test_login(self):
        response = self.ses.post(f"{self.host}/login", data=self.data)
        return response

    # Список клиентов
    def list(self):
        resource = self.ses.get(f'{self.host}/panel/api/inbounds/list', json=self.data).json()
        return resource

    def add_client(self, day, tg_id, user_id):
        epoch = datetime.datetime.fromtimestamp(0) - datetime.timedelta(hours=3)


        x_time = int((datetime.datetime.now() - epoch).total_seconds() * 1000.0)
        x_time += 86400000 * day - 10800000
        header = {"Accept": "application/json"}
        data1 = {
            "id": 1,
            "settings":
                "{\"clients\":"
                "[{\"id\":\"" + str(uuid.uuid1()) + "\","
                                                    "\"alterId\":90,\"email\":\"" + str(user_id) + "\","
                                                                                                   "\"limitIp\":3,\"totalGB\":0,"
                                                                                                   "\"expiryTime\":" + str(
                    x_time) + ",\"enable\":true,\"tgId\":\"" + str(tg_id) + "\",\"subId\":\"\"}]}"
        }
        resource = self.ses.post(f'{self.host}/panel/api/inbounds/addClient', headers=header, json=data1)
        pprint(data1)
        return resource

    def time_active(self, user_id: str):
        dict_x = {}

        epoch = datetime.datetime.fromtimestamp(0) - datetime.timedelta(hours=3)
        x_time = int((datetime.datetime.now() - epoch).total_seconds() * 1000.0)
        y = json.loads(self.list()['obj'][0]['settings'])
        for i in y["clients"]:
            if i['email'] == user_id:
                if i['enable'] and i['expiryTime'] > x_time:
                    dict_x[i['id']] = i['expiryTime']
                    return dict_x
                else:
                    dict_x[i['id']] = '0'
                    return dict_x

        if len(dict_x) == 0:
            dict_x['0'] = '0'
        return dict_x


    def update_client(self, day, user_id):
        dict_x = self.time_active(user_id)

        for key, val in dict_x.items():
            if key != '0' and val != '0':
                val /= 1000
                val += 10800
                date_x = datetime.datetime.fromtimestamp(val)
                # date_x += datetime.timedelta(day)
                epoch = datetime.datetime.fromtimestamp(0) - datetime.timedelta(hours=3)
                x_time = int((date_x - epoch).total_seconds() * 1000.0)
                x_time += 86400000 * day - 10800000
                header = {"Accept": "application/json"}
                data1 = {
                    "id": 1,
                    "settings":
                        "{\"clients\":"
                        "[{\"id\":\"" + str(key) + "\","
                                                   "\"alterId\":90,\"email\":\"" + str(user_id) + "\","
                                                                                                  "\"limitIp\":3,\"totalGB\":0,"
                                                                                                  "\"expiryTime\":" + str(
                            x_time) + ",\"enable\":true,\"tgId\":\"" + str(user_id) + "\",\"subId\":\"\"}]}"
                }
                resource = self.ses.post(f'{self.host}/panel/api/inbounds/updateClient/{key}', headers=header, json=data1)
                return resource
            else:
                epoch = datetime.datetime.fromtimestamp(0) - datetime.timedelta(hours=3)
                x_time = int((datetime.datetime.now() - epoch).total_seconds() * 1000.0)
                x_time += 86400000 * day - 10800000
                header = {"Accept": "application/json"}
                data1 = {
                    "id": 1,
                    "settings":
                        "{\"clients\":"
                        "[{\"id\":\"" + str(key) + "\","
                                                   "\"alterId\":90,\"email\":\"" + str(user_id) + "\","
                                                                                                  "\"limitIp\":3,\"totalGB\":0,"
                                                                                                  "\"expiryTime\":" + str(
                            x_time) + ",\"enable\":true,\"tgId\":\"" + str(user_id) + "\",\"subId\":\"\"}]}"
                }
                resource = self.ses.post(f'{self.host}/panel/api/inbounds/updateClient/{key}', headers=header,
                                         json=data1)
                return resource

    # Получение ссылки ключа
    def link(self, user_id: str):
        """
        Получение ссылки!
        :param user_id: str
        :return: str
        """

        id = ''
        y = json.loads(self.list()['obj'][0]['settings'])
        for i in y["clients"]:
            if i['email'] == user_id:
                id = i["id"]
        x = json.loads(self.list()['obj'][0]['streamSettings'])
        tcp = x['network']
        reality = x['security']
        val = f"vless://{id}@vpn-x3.ru:52687/?type={tcp}&security={reality}&fp=chrome&pbk=T_95HnSovtH9WNr_XfaJ9iL7xnwp96p8E2A8Q3_t_xk&sni=microsoft.com&sid=24705084&spx=%2F#VPN-X3-{user_id}"
        return val

    def activ_list(self):
        """
        Проверка активности подписки
        :param user_id: str
        :return: str
        """
        termless = ((datetime.datetime.fromtimestamp(0) - datetime.timedelta(hours=3)) - datetime.datetime.now()).days
        dict_x = {}
        y = json.loads(self.list()['obj'][0]['settings'])
        for i in y["clients"]:
            ts = i['expiryTime']
            ts /= 1000
            ts += 10800
            x = datetime.datetime.now()
            y = datetime.datetime.fromtimestamp(ts) - datetime.timedelta(hours=3)
            z = y - x
            dict_x[i['email']] = z.days
            if termless == z.days:
                dict_x[i['email']] = 'Неограниченно'
        return dict_x

    # статистика пользователя
    def client_stat(self, user_id):
        """
        Статистика пользователя
        :param user_id: str
        :return: str
        """
        y = json.loads(self.list()['obj'][0]['settings'])['clients']
        all_clients = self.list()['obj'][0]['clientStats']
        for client in all_clients:
            if client['email'] == user_id:
                for one in y:
                    if one['email'] == user_id:
                        client['tgId'] = one['tgId']
                return client
        return 'Пользователь не найден'


    def check_user(self, tg_id):
        all_clients = json.loads(self.list()['obj'][0]['settings'])['clients']
        for client in all_clients:
            if client['tgId'] and int(client['tgId']) == tg_id:
                return True
        return False

    def get_emails_user(self, tg_id):
        emails = []
        users = json.loads(self.list()['obj'][0]['settings'])['clients']
        for user in users:
            if user['tgId'] and int(user['tgId']) == tg_id:
                emails.append(user['email'])
        return emails


    def print_stat(self, email):
        data = self.client_stat(email)
        text = (f'<b>Ваша статистика</b>:\n'
                f'👤 Имя: {email}\n'
                f'💡 Активен: {"Да" if data["enable"] else "Нет"}\n'
                #f' Статус соединения:  Офлайн\n'
                f'📅 Дата окончания: {"Неограниченно" if data["expiryTime"] == 0 else data["expiryTime"]}\n'
                f'🔼 Исходящий трафик: ↑ {self.trafic(data["up"])}\n'
                f'🔽 Входящий трафик: ↓ {self.trafic(data["down"])}\n'
                f'📊 Всего: ↑↓ {self.trafic(data["up"] + data["down"])}\n'
                f'📋🔄 Обновлено: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}')

        return text

    def trafic(self, traf):
        names = ['B', 'KB', 'MB', 'GB', 'TB']
        cnt = 0
        while traf >= 1024:
            traf /= 1024
            cnt += 1
        return f'{round(traf, 2)} {names[cnt]}'
