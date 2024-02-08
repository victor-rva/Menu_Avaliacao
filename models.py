class Relevancia:
    def __init__(self):
        self.__desemprego = None
        self.__etica = None
        self.__seguranca = None
        self.__regulamentacao = None
        self.__potencial = None

    def desemprego(self, desemprego):
        self.__desemprego = desemprego

    def etica(self, etica):
        self.__etica = etica

    def seguranca(self, seguranca):
        self.__seguranca = seguranca

    def regulamentaca(self, regulamentacao):
        self.__regulamentacao = regulamentacao

    def potencial(self, potencial):
        self.__potencial = potencial
