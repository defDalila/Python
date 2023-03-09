from Models.Carro import Carro
from Models.Cliente import Cliente
from datetime import date
from Utils.Helpers import formatarDataParaString, formatarStringParaData
from Utils.Helpers import formatarValorMonetario


class Locacao:

    valor_por_dia: float = 30.00

    def __init__(self, carro: Carro, cliente: Cliente, data_inicial: str, data_final: str ):
        self.__carro: Carro = carro
        self.__cliente: Cliente = cliente
        self.__data_inicial: date = formatarStringParaData(data_inicial)
        self.__data_final: date = formatarStringParaData(data_final)
        self.__total_dias_aluguel: int = self.total_dias_aluguel

    @property
    def carro(self):
        return self.__carro

    @property
    def cliente(self):
        return self.__cliente

    @property
    def data_inicial(self):
        return self.__data_inicial

    @property
    def data_final(self):
        return self.__data_final

    def alugarCarro(self):
        self.carro.status = 0
        self.cliente.alugou_carro = True

    def devolverCarro(self):
        self.carro.status = 1
        self.cliente.alugou_carro = False

    @property
    def total_dias_aluguel(self):
        return (self.data_final - self.data_inicial).days

    def calcularValorAluguel(self) -> float:
        return Locacao.valor_por_dia * self.__total_dias_aluguel

    def __str__(self):
        return f'{str(self.carro)}\n' \
               f'{str(self.cliente)}\n' \
               f'Data inicial: {formatarDataParaString(self.data_inicial)}\n' \
               f'Data Devolução: {formatarDataParaString(self.data_final)}\n' \
               f'Total de diárias: {self.__total_dias_aluguel} dias' \
               f'Valor Total do Aluguel: {formatarValorMonetario(self.calcularValorAluguel())}\n'
