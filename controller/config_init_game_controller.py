from model.config_init_game_model import *

class ConfigInitGameController():
    def __init__(self):
        self._config = ConfigInitGameModel()

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(ConfigInitGameController, cls).__new__(cls)
        return cls._instancia

    def screen(self, width, height):
        return self._config.screen(width, height)

    def background_color(self, color):
        return self._config.background_screen(color)

    def grid(self, rows, cols):
        return self._config.grid(rows, cols)

class AcceptConnectionsController():
    def __init__(self):
        self._accept = AcceptConnectionsModel()

    def listen(self):
        self._accept.daemon = True
        self._accept.start()
        self._accept.join()


class RequestConnectionsController():
    def __init__(self):
        self._request = RequestConnectionsModel()

    def request(self):
        self._request.run()

    def close(self):
        self._request.close()
