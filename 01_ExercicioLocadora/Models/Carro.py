from Utils.Helpers import formataStringParaAno
from Models.ModeloCarro import ModeloCarro


class Carro(ModeloCarro):

    chave_primaria_carro = 1

    def __init__(self, categoria, transmissao, combustivel, marca, modelo, ano: str, placa: str):
        super().__init__(categoria, transmissao, combustivel, marca, modelo)
        self.__id_carro = Carro.chave_primaria_carro
        self.__ano = formataStringParaAno(ano)
        self.__placa = placa
        self.__status = 1
        Carro.chave_primaria_carro += 1

    @property
    def id_carro(self):
        return self.__id_carro

    @property
    def ano(self):
        return self.__ano

    @property
    def placa(self):
        return self.__placa

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        if valor == 1 or valor == 0:
            self.__status = valor

    def __str__(self):
        return f'Carro: {self.id_carro}\n' \
               f'{super().__str__()}\n' \
               f'Ano: {self.ano}\n' \
               f'Placa: {self.placa}\n'