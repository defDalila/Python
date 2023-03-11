from datetime import date
from datetime import datetime


def formataStringParaAno(ano: str) -> date:
    return datetime.strptime(ano, "%y")


def formatarDataParaString(data: date) -> str:
    return data.strftime("%d/%m/%y")


def formatarStringParaData(data: str) -> date:
    return datetime.strptime(data, "%d/%m/%y")


def formatarValorMonetario(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def statusParaString(valor: int):
    switch = {
        0: "Disponível",
        1: "Alugado"
    }
    return switch[valor]


def formatarCpf(cpf: str) -> str:
    if len(cpf) < 11:
        cpf = cpf.zfill(11)
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
