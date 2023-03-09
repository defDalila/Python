from Models.Carro import Carro


class Cliente:

    def __init__(self, nome: str, cpf: str, rg: str ):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__rg: str = rg
        self.__alugou_carro = False
        self.__carro_alugado = None

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rg(self):
        return self.__rg

    @property
    def alugou_carro(self):
        return self.__alugou_carro

    @alugou_carro.setter
    def alugou_carro(self, valor: int):
        if valor == 0 or valor == 1:
            self.__alugou_carro = valor

        if self.alugou_carro == 0:
            self.carro_alugado = None

    @property
    def carro_alugado(self):
        return self.__carro_alugado

    @carro_alugado.setter
    def carro_alugado(self, carro: Carro):
        self.__carro_alugado = carro

