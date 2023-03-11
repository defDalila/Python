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
        print(" ------------------------------------------------------------ ")
        print("|                  Locadora de Veículos LoCar                 |")
        print(" ------------------------------------------------------------ ")
        print("[1] Cadastrar um novo veículo")
        print("[2] Cadastrar um novo cliente")
        print("[3] Realizar a locação de um veículo")
        print("[4] Efetuar a devolução de um veículo")
        print("[5] Relatório de veículos alugados")
        print("[6] Listar todos os carros cadastrados")
        print("[7] Listar todos os clientes cadastrados")
        print("[8] Listar modelos cadastrados")
        print("[0] Encerrar a sessão")
        print("----")

        opcao_usuario = int(input("Entre com a opção desejada: "))
        print()

        if opcao_usuario == 0:
            print("Encerrando sessão...")
            sleep(1)
            print("Até a Próxima!")
            break

        elif opcao_usuario == 1:
            print("---- Cadastrar Veículo ----")
            print("")
            while True:
                cadastrarCarro()
                opcao = input("Deseja cadastrar outro veículo [s/n]? ").lower()
                print()
                if opcao == 'n':
                    print("Retornando ao menu principal...")
                    print("")
                    sleep(1)
                    break

        elif opcao_usuario == 2:
            print("---- Cadastrar Cliente ----")
            print("")
            while True:
                cadastrarCliente()
                opcao = input("Deseja cadastrar outro cliente [s/n]? ").lower()
                print()
                if opcao == 'n':
                    print("Retornando ao menu principal...")
                    print("")
                    sleep(1)
                    break

        elif opcao_usuario == 3:
            print("---- Locar Veículo ----")
            print()
            efetuarAluguelCarro()
            print("Retornando ao menu principal...")
            print("")
            sleep(1)

        elif opcao_usuario == 4:
            print("---- Devolver Veículo ----")
            print()
            efetuarDevolucaoCarro()
            print("Retornando ao menu principal...")
            print("")
            sleep(1)

        elif opcao_usuario == 5:
            print("---- Emitir Relatório de Locação ----")
            print()
            gerarRelatorioLocacao()
            input("Tecle enter para retornar ao menu...")
            print("Retornando ao menu principal...")
            print("")
            sleep(1)

        elif opcao_usuario == 6:
            print("---- Carros Cadastrados ----")
            print()
            listarCarrosCadastrados()
            input("Tecle enter para retornar ao menu...")
            print("Retornando ao menu principal...")
            print("")
            sleep(1)

        elif opcao_usuario == 7:
            print("---- Clientes Cadastrados ----")
            print()
            listarClientesCadastrados()
            input("Tecle enter para retornar ao menu...")
            print("Retornando ao menu principal...")
            print("")
            sleep(1)

        elif opcao_usuario == 8:
            print("---- Modelos Cadastrados ----")
            print()
            listarModelosCadastrados()
            input("Tecle enter para voltar ao menu...")
            print("Retornando ao menu principal...")
            print("")
            sleep(1)

        else:
            print("Opção Inválida! Retornando ao menu principal...")
            print("")
            sleep(1)


def cadastrarCarro():
    retorno = listarModelosCadastrados()
    opcao_modelo = checarNovoCadastroDeModelo(retorno)

    if opcao_modelo == -1:
        print("Redirecionando para o cadastro de modelo...")
        print("")
        sleep(1)
        modelo = cadastrarModelo()
    else:
        modelo = buscarModeloPorNumero(opcao_modelo)
    print("Insira os dados abaixo para o modelo escolhido:")
    ano = input("Ano: ")
    placa = input("Placa: ").upper()
    print("")

    novo_carro = Carro(
        categoria=modelo.categoria,
        transmissao=modelo.transmissao,
        combustivel=modelo.combustivel,
        marca=modelo.marca,
        modelo=modelo.modelo,
        ano=ano,
        placa=placa
    )
    cadastro_novo_carro = {novo_carro.id_carro: novo_carro}
    carros_cadastrados.update(cadastro_novo_carro)
    print("Carro cadastrado com sucesso!")
    print("")
    sleep(1)


def checarNovoCadastroDeModelo(retorno):
    while True:
        numero_modelo = -1
        if retorno < 0:
            break
        else:
            opcao_usuario = input("O Modelo já está cadastrado [s/n]? ").lower()
            print("")
            if opcao_usuario == 's':
                numero_modelo = int(input("Entre com o número do modelo do novo carro: "))
                print("")
                break
            elif opcao_usuario == 'n':
                break
            else:
                print("Opção Inválida, tente novamente! ")
                print("")
                sleep(1)
    return numero_modelo


def cadastrarModelo():
    print("---- Cadastrar Modelo ----")
    print("")
    print("Insira os dados do novo modelo:")
    categoria = input("Categoria: ").title()
    transmissao = input("Transmissao: ").title()
    combustivel = input("Combustivel: ").title()
    marca = input("Marca: ").title()
    modelo = input("Modelo: ").title()
    print("")

    novo_modelo = ModeloCarro(categoria, transmissao, combustivel, marca, modelo)
    cadastro_novo_modelo = {novo_modelo.id_modelo: novo_modelo}
    modelos_cadastrados.update(cadastro_novo_modelo)
    print("Modelo cadastrado!")
    print("")
    sleep(1)
    return novo_modelo



def cadastrarCliente():
    cpf_cadastro = checarExistenciaCliente()

    if cpf_cadastro == "-1":
        print("Cliente já cadastrado!")
        print("")
        sleep(1)
    else:
        nome = input("Nome: ").title()
        rg = input("RG: ").upper()
        print("")

        novo_cliente = Cliente(nome=nome, cpf=cpf_cadastro, rg=rg)
        cadastro_novo_cliente = {novo_cliente.cpf: novo_cliente}
        clientes_cadastrados.update(cadastro_novo_cliente)
        print("Cliente cadastrado com sucesso!")
        print("")
        sleep(1)


def checarExistenciaCliente():
    print("Entre com od dados do cliente: ")
    cpf_procurado = input("CPF (somente números): ")
    print("")
    cliente_encontrado = buscarClientePorCpf(formatarCpf(cpf_procurado))

    if cliente_encontrado:
        return "-1"
    else:
        return cpf_procurado




def efetuarAluguelCarro():
    while True:
        print("Lista de carros disponíveis para locação")
        listarCarrosdisponiveis()
        print("")

        id_carro_escolhido = int(input("Digite o Id do carro escolhido para locação: "))
        print("")
        carro_encontrado = carros_cadastrados.get(id_carro_escolhido)

        if carro_encontrado:
            while True:
                print("Lista de Clientes (sem registro de locação)")
                listarClientesDisponiveis()
                print("")

                cpf_cliente = formatarCpf(input("Digite o cpf do cliente que irá locar o veículo (somente números): "))
                print("")
                cliente_encontrado = clientes_cadastrados.get(cpf_cliente)

                if cliente_encontrado:
                    print("Insira o período de locação")
                    data_inicial = input("Data inicial (dd/mm/aa): ")
                    data_final = input("Data final (dd/mm/aa): ")
                    print("")

                    nova_locacao = Locacao(carros_cadastrados.get(id_carro_escolhido),
                                           clientes_cadastrados.get(cpf_cliente), data_inicial, data_final)
                    nova_locacao.alugarCarro()
                    registros_locacoes.append(nova_locacao)
                    print("Carro alugado com sucesso!")
                    sleep(2)
                    print("Relatório de locação")
                    print("")
                    print(nova_locacao)
                    print("")
                    break
                else:
                    print("Cliente não localizado!")
                    print("")
                    sleep(1)
            break
        else:
            print("Carro não localizado!")
            print("")
            sleep(1)


def efetuarDevolucaoCarro():
    cpf_procurado = formatarCpf(input("Digite o cpf do locador (somente números): "))
    print("")
    index_registro = -1

    for regitro in registros_locacoes:
        if cpf_procurado == regitro.cliente.cpf:
            index_registro = registros_locacoes.index(regitro)

    if index_registro == -1:
        print("Não foram encontrados registros de locação para este CPF!")
        print("")
        sleep(1)
    else:
        locacao = registros_locacoes[index_registro]
        print("Registro de locação encontrado!")
        sleep(1)
        print(locacao)
        print("")

        confirmacao = input(f"Confirma a devolução do carro de id {str(locacao.carro.id_carro).zfill(3)} [s/n]? ").lower()
        print("")

        if confirmacao == 's':
            locacao.devolverCarro()
            registros_locacoes.pop(index_registro)
            print("Processo concluído! Devolução efetudada com sucesso!")
            print("")
            sleep(1)
        else:
            print("Operação cancelada pelo usuário!")
            print("")
            sleep(1)


def gerarRelatorioLocacao():
    if len(registros_locacoes) == 0:
        print("Não existem veículos alugados para gerar relatório!")
        print("")
        sleep(1)
    else:
        i = 1
        for item in registros_locacoes:
            print(f"Registro {i}")
            print(item)
            print("----")
            i += 1
            sleep(1)


def listarCarrosCadastrados():
    if len(carros_cadastrados) == 0:
        print("Ainda não existem carros cadastrados!")
        print("")
        sleep(1)
    else:
        for i in carros_cadastrados.keys():
            print(carros_cadastrados[i])
            print("---")
            sleep(1)


def listarClientesCadastrados():
    if len(clientes_cadastrados) == 0:
        print("Ainda não existem clientes cadastrados!")
        print("")
        sleep(1)
    else:
        for i in clientes_cadastrados.keys():
            print(clientes_cadastrados[i])
            print("----")
            sleep(1)


def listarModelosCadastrados():
    if len(modelos_cadastrados) == 0:
        print("Ainda não existem modelos cadastrados!")
        print("")
        sleep(1)
        return -1
    else:
        for i in modelos_cadastrados.keys():
            print(f"Modelo: {str(i).zfill(2)}")
            print(modelos_cadastrados[i])
            print("----")
            sleep(1)
        return 1


def listarCarrosdisponiveis():
    for carro in carros_cadastrados.keys():
        if carros_cadastrados[carro].status == 0:
            print(carros_cadastrados[carro])
            print("----")
            sleep(1)


def listarClientesDisponiveis():
    if len(clientes_cadastrados) == 0:
        print("Ainda não existem clientes cadastrados!")
        print("")
        sleep(1)
    else:
        for i in clientes_cadastrados.keys():
            if clientes_cadastrados[i].alugou_carro == 0:
                print(clientes_cadastrados[i])
                print("----")
                sleep(1)


def buscarModeloPorNumero(numero_procurado: int):
    return modelos_cadastrados.get(numero_procurado)


def buscarClientePorCpf(cpf_procurado: str):
    return clientes_cadastrados.get(cpf_procurado)


def buscarCarroPorId(id_procurado: int):
    return carros_cadastrados.get(id_procurado)


if __name__ == "__main__":
    menu()

