class ModeloCarro:

    chave_primaria_modelo = 1

    def __init__(self, categoria: str, transmissao: str, combustivel: str, marca: str, modelo: str):
        self.__id_modelo = ModeloCarro.chave_primaria_modelo
        self.__categoria: str = categoria
        self.__transmissao: str = transmissao
        self.__combustivel: str = combustivel
        self.__marca: str = marca
        self.__modelo: str = modelo
        ModeloCarro.chave_primaria_modelo += 1

    @property
    def id_modelo(self):
        return self.__id_modelo

    @property
    def categoria(self):
        return self.__categoria

    @property
    def transmissao(self):
        return self.__transmissao

    @property
    def combustivel(self):
        return self.__combustivel

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    def __str__(self):
        return f'Categoria: {self.categoria}\t' \
               f'Transmissão: {self.transmissao}\t\t' \
               f'Combustível: {self.combustivel}\t' \
               f'Marca : {self.marca}\t' \
               f'Modelo: {self.modelo}'

