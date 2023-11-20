import abc

# Fábricas
class Navio(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def metodo_abstrato(self):
        pass

# Classes derivadas da Fábrica
class Fragata(Navio):
    def __init__(self):
        self.nivel = 2
        self.pt_parcial = 5
        self.pt_total = 20
        self.qtd = 4

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Fragata, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

class Corveta(Navio):
    def __init__(self):
        self.nivel = 2
        self.pt_parcial = 5
        self.pt_total = 20
        self.qtd = 4

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Corveta, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

class Destroier(Navio):
    def __init__(self):
        self.nivel = 3
        self.pt_parcial = 10
        self.pt_total = 30
        self.qtd = 3

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Destroier, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

class Cruzador(Navio):
    def __init__(self):
        self.nivel = 3
        self.pt_parcial = 10
        self.pt_total = 30
        self.qtd = 3

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Cruzador, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

class Submarino(Navio):
    def __init__(self):
        self.nivel = 4
        self.pt_parcial = 15
        self.pt_total = 40
        self.qtd = 2

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Submarino, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

class Encouracado(Navio):
    def __init__(self):
        self.nivel = 4
        self.pt_parcial = 15
        self.pt_total = 40
        self.qtd = 2

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(Encouracado, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

class PortaAvioes(Navio):
    def __init__(self):
        self.nivel = 4
        self.pt_parcial = 20
        self.pt_total = 50
        self.qtd = 2

    _instancia = None
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(PortaAvioes, cls).__new__(cls)
        return cls._instancia

    def metodo_abstrato(self):
        pass

