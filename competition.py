import requests
import socket

server_ip = 'http://127.0.0.1'
server_port = 5555
server_host = '{}:{}'.format(server_ip, server_port)

competition_url = '{}/{}'.format(server_host, 'competitions')

pc = socket.getfqdn(socket.gethostname())
client1_ip = socket.gethostbyname(pc)
client2_ip = client1_ip
client1_port = 9000
client2_port = 9001
client1_host = 'http://{}:{}'.format(client1_ip, client1_port)
client2_host = 'http://{}:{}'.format(client2_ip, client2_port)

competition_name = 'test2'
player1 = '精武门'
player2 = '索嗨'


def init_competition():
    # 初始化比赛
    header = {
        'Content-Type': 'application/json'
    }
    competition = {
        'name': competition_name,
        'player1': player1,
        'player2': player2,
        'player1_host': client1_host,
        'player2_host': client2_host,
        'seed': 10,
    }
    resp = requests.post(competition_url, json=competition, headers=header)
    print("比赛创建结果：{}".format(resp.text))


if __name__ == '__main__':
    init_competition()
