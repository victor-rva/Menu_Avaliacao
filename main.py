from constants import menu
from functions import realizar_avaliacao, relatorio

def main():
    while True:
        escolha = input(menu)
        if escolha == "0": break
        if escolha == "1": realizar_avaliacao()
        if escolha == "2": relatorio()


if __name__ == "__main__":
    main()
