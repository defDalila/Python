from Models.Cliente import Cliente
from Models.Carro import Carro
from Models.ModeloCarro import ModeloCarro
from Models.Locacao import Locacao
from typing import List
from typing import Dict
from time import sleep

from Utils.Helpers import formatarCpf

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
        print("[8] Listar modelos cadastrados")
        print("[0] Encerrar a sessão")

        opcao_usuario = int(input("\nOpção desejada: "))

        if opcao_usuario == 0:
            print("Encerrando sessão...")
            sleep(1)
            print("Até a Próxima!")
            break

        elif opcao_usuario == 1:
            print("Cadastrar um novo Veículo")
            print()
            retorno = listarModelosCadastrados()
            opcao_modelo = checarNovoCadastroDeModelo(retorno)

            if opcao_modelo == -1:
                modelo = cadastrarModelo()
                cadastrarCarro(modelo)
            else:
                modelo = buscarModeloPorNumero(opcao_modelo)
                cadastrarCarro(modelo)
            print("Retornando ao menu principal...")
            sleep(1)
        elif opcao_usuario == 2:
            print("Cadastrar um novo Cliente")
            print()
            cpf_cliente_existente = checarExistenciaCliente()

            if cpf_cliente_existente == "000000000":
                print("Cliente já cadastrado")
            else:
                cadastrarCliente(cpf_cliente_existente)
            print("Retornando ao menu principal...")
            sleep(1)
        elif opcao_usuario == 3:
            print("Realizar a locação de um veículo")
            print()
            efetuarAluguelCarro()
            print("Retornando ao menu principal...")
            sleep(1)
        elif opcao_usuario == 4:
            print("Devolver um veículo Alugado")
            print()
            efetuarDevolucaoCarro()
            print("Retornando ao menu principal...")
            sleep(1)
        elif opcao_usuario == 5:
            print("Relatório de Locação de veículos")
            print()
            gerarRelatorioLocacao()
            print("Retornando ao menu principal...")
            sleep(1)

        elif opcao_usuario == 6:
            print("Carros Cadastrados")
            print()
            listarCarrosCadastrados()
            print("Retornando ao menu principal...")
            sleep(1)

        elif opcao_usuario == 7:
            print("Clientes cadastrados")
            print()
            listarClientesCadastrados()
            print("Retornando ao menu principal...")
            sleep(1)

        elif opcao_usuario == 8:
            print("Modelos Cadastrados")
            print()
            listarModelosCadastrados()
            print("Retornando ao menu principal...")
            sleep(1)

        else:
            print("Opção Inválida! Retornando ao menu principal...")
            sleep(1)


def checarNovoCadastroDeModelo(retorno):
    while True:

        numero_modelo = -1

        if retorno < 0:
            break
        else:
            opcao_usuario = input("O Modelo já está cadastrado [s/n]? ").lower()

            if opcao_usuario == 's':
                numero_modelo = int(input("Digite o número do modelo base para novo carro: "))
                break
            elif opcao_usuario == 'n':
                break
            else:
                print("Opção Inválida, tente novamente!")

    return numero_modelo


def cadastrarModelo():
    print("Cadastrando um novo modelo...")
    sleep(1)
    print("Insira os dados do novo modelo:")
    categoria = input("Categoria: ")
    transmissao = input("Transmissao: ")
    combustivel = input("Combustivel: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")

    novo_modelo = ModeloCarro(categoria, transmissao, combustivel, marca, modelo)
    cadastro_novo_modelo = {novo_modelo.id_modelo: novo_modelo}
    modelos_cadastrados.update(cadastro_novo_modelo)
    print("Novo modelo cadastrado com sucesso!")
    sleep(1)

    return novo_modelo


def cadastrarCarro(modelo_carro: ModeloCarro):
    print()
    print("Insira os dados específicos do novo carro")
    sleep(1)
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
    print()
    print("Novo carro cadastrado com sucesso!")
    sleep(1)


def checarExistenciaCliente():
    cpf_procurado = input("Digite o CPF do cliente: ")

    cliente_encontrado = buscarClientePorCpf(formatarCpf(cpf_procurado))

    if cliente_encontrado:
        return "000000000"
    else:
        return cpf_procurado


def cadastrarCliente(cpf):
    print("Cadastrando um novo cliente...")
    print()
    sleep(1)
    nome = input("Digite o nome: ")
    rg = input("Digite o RG: ")

    novo_cliente = Cliente(nome=nome, cpf=cpf, rg=rg)
    cadastro_novo_cliente = {novo_cliente.cpf: novo_cliente}
    clientes_cadastrados.update(cadastro_novo_cliente)
    print()
    print("Cliente cadastrado com sucesso!")
    sleep(1)


def efetuarAluguelCarro():
    while True:
        print("Listando os carros disponíveis")
        print()
        sleep(1)
        listarCarrosdisponiveis()
        id_carro_escolhido = int(input("Digite o Id do carro escolhido para locação: "))

        carro_encontrado = carros_cadastrados.get(id_carro_escolhido)

        if carro_encontrado:
            while True:
                print()
                print("Listando os clientes cadastrados...")
                sleep(1)
                listarClientesCadastrados()
                print()
                cpf_cliente = formatarCpf(input("Digite o cpf do cliente que irá locar o veículo:"))
                cliente_encontrado = clientes_cadastrados.get(cpf_cliente)

                if cliente_encontrado:

                    data_inicial = input("Insira da data de inicio (dd/mm/aaaa): ")
                    data_final = input("Insira a data final (dd/mm/aaaa):")

                    nova_locacao = Locacao(carros_cadastrados.get(id_carro_escolhido),
                                           clientes_cadastrados.get(cpf_cliente), data_inicial, data_final)
                    nova_locacao.alugarCarro()
                    registros_locacoes.append(nova_locacao)
                    sleep(1)
                    print("Processo de Locação Concluído!")
                    print()
                    print("Dados da locação")
                    print(nova_locacao)
                    break
                else:
                    print("Cliente não localizado!")
                    sleep(1)
            break
        else:
            print("Carro não localizado!")
            sleep(1)


def efetuarDevolucaoCarro():
    print()
    cpf_procurado = formatarCpf(input("Entre com o cpf do cliente: "))
    print("Localizando o registro de locação do cliente informado...")
    sleep(1)
    for registro in registros_locacoes:

        if registro.cliente.cpf == cpf_procurado:
            locacao_index = registros_locacoes.index(registro)
            locacao = registros_locacoes[locacao_index]
            print()
            print("Registro de Locação encontrado:")
            print()
            print(locacao)

            opcao = input(f"Confirma devolução do veículo {locacao.carro.id_carro} [s/n]: ").lower()
            if opcao == 's':
                locacao.devolverCarro()
                registros_locacoes.pop(locacao_index)
                print("Devolução realizada com sucesso!")
                print()
                sleep(1)
            else:
                print('Operação não realizada!')
        else:
            print("Cliente não encontrado!")


def gerarRelatorioLocacao():
    if len(registros_locacoes) == 0:
        print("Não existem veículos alugados!")
        print()
    else:
        for item in registros_locacoes:
            print(item)
            print()


def listarModelosCadastrados():
    if len(modelos_cadastrados) == 0:
        print("Ainda não existem modelos cadastrados!")
        sleep(1)
        return -1
    else:
        for i in modelos_cadastrados.keys():
            print(f"Modelo: {i}")
            print(modelos_cadastrados[i])
            print()
        return 1


def listarCarrosCadastrados():
    if len(carros_cadastrados) == 0:
        print("Ainda não existem carros cadastrados!")
        print()
        sleep(1)
    else:
        for i in carros_cadastrados.keys():
            print(carros_cadastrados[i])
            print()


def listarClientesCadastrados():
    if len(clientes_cadastrados) == 0:
        print("Ainda não existem clientes cadastrados")
        sleep(1)
    else:
        for i in clientes_cadastrados.keys():
            print(clientes_cadastrados[i])
            print()


def listarCarrosdisponiveis():
    for carro in carros_cadastrados.keys():
        if carros_cadastrados[carro].status == 0:
            print(carros_cadastrados[carro])
            print()


def buscarModeloPorNumero(numero_procurado: int):
    return modelos_cadastrados.get(numero_procurado)


def buscarClientePorCpf(cpf_procurado: str):
    return clientes_cadastrados.get(cpf_procurado)


def buscarCarroPorId(id_procurado: int):
    return carros_cadastrados.get(id_procurado)


if __name__ == "__main__":
    menu()
