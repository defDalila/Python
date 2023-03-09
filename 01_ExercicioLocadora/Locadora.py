from Models.Cliente import Cliente
from Models.Carro import Carro
from Models.ModeloCarro import ModeloCarro
from Models.Locacao import Locacao
from typing import List
from typing import Dict
from time import sleep

modelos_cadastrados: Dict[int, ModeloCarro] = {}
clientes_cadastrados: Dict[str, Cliente] = {}
carros_cadastrados: Dict[int, Carro] = {}
registros_locacoes: List[Locacao] = []


def main():
    menu()


def menu():
    while True:
        print("---------------- Locadora de Veículos LoCar ----------------")
        print()
        print("Escolha uma das opções abaixo:")
        print("[1] Cadastrar um novo veículo")
        print("[2] Cadastrar um novo cliente")
        print("[3] Realizar a locação de um veículo")
        print("[4] Efetuar a devolução de um veículo")
        print("[5] Relatório de veículos alugados")
        print("[6] Listar todos os carros cadastrados")
        print("[7] Listar todos os clientes cadastrados")
        print("[0] Encerrar a sessão")

        opcao_usuario = int(input("\nOpção desejada: "))

        if opcao_usuario == 0:
            print("Encerrando sessão...")
            sleep(1)
            break

        elif opcao_usuario == 1:
            print(" Cadastrar um novo Veículo")
            listarModelosCadastrados()
            opcao_modelo = checarNovoCadastroDeModelo()

            if opcao_modelo == -1:
                modelo = cadastrarModelo()
                cadastrarCarro(modelo)
            else:
                modelo = buscarModeloPorNumero(opcao_modelo)
                cadastrarCarro(modelo)

        elif opcao_usuario == 2:
            print("Cadastrar um novo Cliente")

        elif opcao_usuario == 3:
            print("Realizar a locação de um veículo")

        elif opcao_usuario == 4:
            print("Devolver um veículo Alugado")

        elif opcao_usuario == 5:
            print("Relatório de Locação de veículos")

        elif opcao_usuario == 6:
            print("Carros Cadastrados")

        elif opcao_usuario == 7:
            print("Clientes cadastrados")

        else:
            print("Opção Inválida! Retornando ao menu principal...")
            sleep(1)


def checarNovoCadastroDeModelo():
    while True:

        numero_Modelo = -1
        opcao_usuario = input("O Modelo já está cadastrado [s/n]? ").lower()

        if opcao_usuario == 's':
            numero_Modelo = int(input("Digite o numero do modelo do novo carro: "))
            break

        elif opcao_usuario == 'n':
            break

        else:
            print("Opção Inválida, tente novamente.. ")

    return numero_Modelo


def cadastrarModelo():
    categoria = input("Categoria: ")
    transmissao = input("Transmissao: ")
    combustivel = input("Combustivel: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")

    novo_modelo = ModeloCarro(categoria, transmissao, combustivel, marca, modelo)
    cadastro_novo_modelo = {novo_modelo.id_modelo: novo_modelo}
    modelos_cadastrados.update(cadastro_novo_modelo)

    return novo_modelo


def cadastrarCarro(modelo_carro: ModeloCarro):
    ano = input("Digite o Ano: ")
    placa = input("Digite a placa: ")
    novo_carro = Carro(
        categoria=modelo_carro.categoria,
        transmissao=modelo_carro.transmissao,
        combustivel=modelo_carro.combustivel,
        marca=modelo_carro.marca,
        modelo=modelo_carro.modelo,
        ano=ano,
        placa=placa
    )

    cadastro_novo_carro = {novo_carro.id_carro: novo_carro}
    carros_cadastrados.update(cadastro_novo_carro)


def cadastrarCliente():
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    rg = input("Digite o RG: ")

    novo_cliente = Cliente(nome=nome, cpf=cpf, rg=rg)
    cadastro_novo_cliente = {novo_cliente.cpf: novo_cliente}
    clientes_cadastrados.update(cadastro_novo_cliente)


def efetuarAluguelCarro():
    # Determinar carro
    # determinar cliente
    # efetuar aluguel: Associar carro e cliente
    # adicionar aluguel do registro de locações
    pass


def efetuarDevolucaoCarro():
    # determinar cliente
    # determinar carro que está com cliente
    # remover carro do cliente
    # tornar carro disponível
    pass


def gerarRelatorioLocacao():
    # Imprimir lista de locações com status dos carros alugados
    pass


def listarModelosCadastrados():
    if len(modelos_cadastrados) == 0:
        print("Ainda não existem modelos cadastrados")
    else:
        for i in modelos_cadastrados.keys():
            print(f"Modelo: {i}")
            print(modelos_cadastrados.values())


def listarCarrosCadastrados():
    if len(carros_cadastrados) == 0:
        print("Ainda não existem carros cadastrados")
    else:
        for _ in carros_cadastrados.keys():
            print(carros_cadastrados.values())


def listarClientesCadastrados():
    if len(clientes_cadastrados) == 0:
        print("Ainda não existem clientes cadastrados")
    else:
        for _ in clientes_cadastrados.keys():
            print(clientes_cadastrados.values())


def buscarModeloPorNumero(numero_procurado: int):
    return modelos_cadastrados.get(numero_procurado)


def buscarClientePorCpf(cpf_procurado: str):
    return clientes_cadastrados.get(cpf_procurado)


def buscarCarroPorId(id_procurado: int):
    return carros_cadastrados.get(id_procurado)


if __name__ == "__main__":
    menu()
