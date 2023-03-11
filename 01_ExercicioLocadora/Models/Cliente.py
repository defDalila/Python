from Models.Carro import Carro
from Utils.Helpers import formatarCpf


class Cliente:

    def __init__(self, nome: str, cpf: str, rg: str):
        self.__nome: str = nome
        self.__cpf: str = formatarCpf(cpf)
        self.__rg: str = rg
        self.__alugou_carro = 0
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
    def alugou_carro(self, valor):
        self.__alugou_carro = valor

    @property
    def carro_alugado(self):
        return self.__carro_alugado

    @carro_alugado.setter
    def carro_alugado(self, carro: Carro):
        if self.alugou_carro == 1:
            self.__carro_alugado = carro
        elif self.alugou_carro == 0:
            self.__carro_alugado = None

    def __str__(self):

        if self.alugou_carro == 0:
            return f'Nome: {self.nome}\n' \
                   f'CPF: {self.cpf}\n' \
                   f'RG: {self.rg}\n' \
                   f'Sem carro alugado em seu registro'
        elif self.alugou_carro == 1:
            return f'Nome: {self.nome}\n' \
                   f'CPF: {self.cpf}\n' \
                   f'RG: {self.rg}\n' \
                   f'ID do carro alugado: {str(self.carro_alugado.id_carro).zfill(3)}'
