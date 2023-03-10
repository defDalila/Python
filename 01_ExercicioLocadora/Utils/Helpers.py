from datetime import date
from datetime import datetime


def formataStringParaAno(ano: str) -> date:
    return datetime.strptime(ano, "%Y")


def formatarDataParaString(data: date) -> str:
    return data.strftime("%d/%m/%Y")


def formatarStringParaData(data: str) -> date:
    return datetime.strptime(data, "%d/%m/%Y")


def formatarValorMonetario(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def statusParaString(valor: int):
    switch = {
        0: "Carro Disponível",
        1: "Carro Alugado"
    }
    return switch[valor]


def formatarCpf(cpf: str) -> str:
    if len(cpf) < 11:
        cpf = cpf.zfill(11)
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
