from Utils.Helpers import statusParaString
from Models.ModeloCarro import ModeloCarro


class Carro(ModeloCarro):

    chave_primaria_carro = 1

    def __init__(self, categoria, transmissao, combustivel, marca, modelo, ano: str, placa: str):
        super().__init__(categoria, transmissao, combustivel, marca, modelo)
        self.__id_carro = Carro.chave_primaria_carro
        self.__ano = ano
        self.__placa = placa
        self.__status = 0
        Carro.chave_primaria_carro += 1
        ModeloCarro.chave_primaria_modelo -= 1

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
        self.__status = valor

    def __str__(self):
        return f'ID Carro: {str(self.id_carro).zfill(3)}\n' \
               f'Status: {statusParaString(self.status)}\n' \
               f'Dados do carro: {self.marca} {self.modelo}, ' \
               f'{self.categoria}, {self.transmissao}, {self.combustivel}\n' \
               f'Ano: {self.ano}\n' \
               f'Placa: {self.placa}'

