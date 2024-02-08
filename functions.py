from constants import pesquisa, estados
from models import Relevancia

def get_valid_vote(prompt):
    """A função garantirá que apenas votos válidos entre 1 e 5 sejam aceitos. Caso o usuário insira um valor inválido,
    será exibida uma mensagem de erro e será solicitado que insira novamente até que um voto válido seja fornecido.
    O voto válido será retornado pela função. A palavra prompt utilizada como parâmetro para definir a mensagem exibida
     para o usuário."""
    while True:
        try:
            vote = int(input(prompt))
            if 1 <= vote <= 5:
                return vote
            else:
                print("Valor inválido. Insira um número entre 1 e 5.")
        except ValueError:
            print("Valor inválido. Insira um número entre 1 e 5.")


def realizar_avaliacao():
    """Essa função permite que o usuário avalie a relevância de diferentes aspectos e associa essas avaliações aos
    estados correspondentes no dicionário pesquisa. No final, teremos um dicionário onde cada estado tem uma lista de
    objetos Relevancia associados a ele"""
    while True:
        estado = input("Informe o estado onde você reside (SIGLA): ").upper()
        if estado not in estados:
            print("Esse estado não existe no Brasil. Digite novamente.")
        else:
            break
    print("Sendo 1 o mais baixo e 5, classifique o nivel de relevância que você acha que a Inteligência artificial tem sobre os seguinte tópicos:")
    relevancia = Relevancia()
    relevancia.desemprego = get_valid_vote("Qual o grau de relevância para Desemprego e desigualdade (1-5)? ")
    relevancia.etica = get_valid_vote("Qual o grau de relevância para Questões éticas e morais (1-5)? ")
    relevancia.seguranca = get_valid_vote("Qual o grau de relevância para Segurança cibernética e privacidade (1-5)? ")
    relevancia.regulamentacao = get_valid_vote("Qual o grau de relevância para Controle e regulamentação (1-5)? ")
    relevancia.potencial = get_valid_vote("Qual o grau de relevância para Potencial desenvolvimento de IA superinteligente (1-5)? ")

    if estado in pesquisa:
        pesquisa[estado].append(relevancia)
    else:
        pesquisa[estado] = [relevancia]


def relatorio():
    """Essa função permite gerar um relatório das médias de relevância para diferentes aspectos de um estado específico
    com base nos dados armazenados no dicionário pesquisa. O relatório inclui a média de cada aspecto, destacando o
    aspecto com a maior média."""
    while True:
        estado = input("Informe o estado onde você reside (SIGLA): ").upper()
        if estado not in estados:
            print("Esse estado não existe no Brasil. Digite novamente.")
        else:
            break
    if estado in pesquisa:
        media_desemprego = sum([relevancia.desemprego for relevancia in pesquisa[estado]]) / len(pesquisa[estado])
        media_etica = sum([relevancia.etica for relevancia in pesquisa[estado]]) / len(pesquisa[estado])
        media_seguranca = sum([relevancia.seguranca for relevancia in pesquisa[estado]]) / len(pesquisa[estado])
        media_regulamentacao = sum([relevancia.regulamentacao for relevancia in pesquisa[estado]]) / len(pesquisa[estado])
        media_potencial = sum([relevancia.potencial for relevancia in pesquisa[estado]]) / len(pesquisa[estado])

        medias = {
            'Desemprego e Desigualdade': media_desemprego,
            'Questões Éticas e Morais': media_etica,
            'Segurança Cibernética e Privacidade': media_seguranca,
            'Controle e Regulamentação': media_regulamentacao,
            'IA Superinteligente': media_potencial
        }

        maior_media = max(medias, key=medias.get)
        print(f"Maior média: {maior_media} com {medias[maior_media]}")
        # Encontra o aspecto com a maior média usando a função max() com a opção key=medias.get Isso retorna a chave com
        # o maior valor no dicionário medias.

        medias_ordenadas = sorted(medias.items(), key=lambda x: x[1], reverse=True)
        # Ordena as médias do dicionário medias em ordem decrescente, com base nos valores, usando a função sorted() e a
        # opção key = lambda x: x[1].

        print(f"RELATÓRIO DO ESTADO: {estados[estado]}")
        print("--------------------------------")
        for media in medias_ordenadas:
            print(f"{media[0]}: {media[1]:.2f}")

        input("Pressione ENTER se deseja continuar.")

    else:
        print("Não há dados para o estado informado.")
