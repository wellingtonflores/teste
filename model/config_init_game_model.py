import pygame
import time
import socket, threading

class ConfigInitGameModel():
    def __init__(self):
        pygame.init()

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(ConfigInitGameModel, cls).__new__(cls)
        return cls._instancia

    def background_screen(self, color):
        background_color = {}
        background_color['black'] = (0, 0, 0)
        background_color['white'] = (255, 255, 255)
        background_color['blue'] = (0, 0, 255)
        background_color['red'] = (255, 0, 0)
        background_color['green'] = (0, 255, 0)
        background_color['yellow'] = (255, 255, 0)
        background_color['marrom'] = (92, 51, 23)

        return background_color[color]

    def screen(self, width, height):
        WINDOW_SIZE = [width, height]
        pygame.display.set_caption('BATALHA NAVAL')
        screen = pygame.display.set_mode(WINDOW_SIZE)

        return screen

    def grid(self, rows, cols):
        grid = []
        for row in range(rows):
            grid.append([])
            for col in range(cols):
                grid[row].append(0)

        return grid

class PlayerThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        print('\n_______________________________________________________\n')
        print("New connection added: ", self.clientAddress)

    def run(self):
        self.csocket.close()
        print("encerrando conexão", self.clientAddress)

    def send_msg(self, msg):
        self.csocket.send(msg.encode())

    def recv_msg(self):
        msg = self.csocket.recv(1028)
        msg = msg.decode()
        return msg

class AcceptConnectionsModel(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.LOCALHOST = "192.168.15.126"
        self.PORT = 8088
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self.server.bind((self.LOCALHOST, self.PORT))
        print("\nServer started")
        print("Waiting for client request..")
        time.sleep(0.2)
        self.server.listen(1)
        _clientsock, _clientAddress = self.server.accept()
        _newthread = PlayerThread(_clientAddress, _clientsock)
        _newthread.daemon = True
        _newthread.start()
        _newthread.join()


class RequestConnectionsModel():
    def __init__(self):
        self.SERVER = "192.168.15.126"
        self.PORT = 8088
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.client.connect((self.SERVER, self.PORT))

    def send_msg(self, msg):
        self.client.sendall(msg.encode())

    def recv_msg(self):
        msg = self.client.recv(1024)
        msg = msg.decode()
        return msg

    def close(self):
        self.client.close()