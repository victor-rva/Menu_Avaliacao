# README.md

## Sistema de Avaliação de Relevância em Inteligência Artificial

Este programa em Python foi desenvolvido para coletar e analisar avaliações da relevância de diferentes aspectos relacionados à Inteligência Artificial (IA) em diversos estados brasileiros. O código utiliza uma classe chamada `Relevancia` para representar as avaliações, e os dados são armazenados em um dicionário chamado `pesquisa`. O usuário pode realizar avaliações e gerar relatórios com médias de relevância para diferentes tópicos.

### Funcionalidades Principais

1. **Realizar Avaliação (`realizar_avaliacao`):**
   - Permite ao usuário avaliar a relevância de diferentes aspectos da IA, como desemprego, ética, segurança cibernética, regulamentação e potencial de desenvolvimento de IA superinteligente.
   - Associa as avaliações ao estado correspondente no dicionário `pesquisa`.

2. **Gerar Relatório (`relatorio`):**
   - Gera um relatório das médias de relevância para cada aspecto em um estado específico.
   - Destaca o aspecto com a maior média.
   - Apresenta as médias ordenadas em ordem decrescente.

3. **Menu Principal (`main`):**
   - Fornecer um menu simples para interação do usuário, permitindo a escolha entre finalizar o programa, realizar avaliação ou gerar relatório.

### Como Usar

1. **Execução:**
   - Execute o programa Python.
   - Escolha as opções do menu para realizar avaliações ou gerar relatórios.

2. **Avaliação:**
   - Forneça o estado (SIGLA) onde reside.
   - Classifique de 1 a 5 o nível de relevância para diferentes aspectos da IA.
   - As avaliações serão associadas ao estado correspondente no dicionário `pesquisa`.

3. **Relatório:**
   - Informe o estado (SIGLA) para o qual deseja gerar o relatório.
   - O relatório exibirá as médias de relevância para cada aspecto, destacando o de maior média.

### Dados Utilizados

- Estados e suas siglas são definidos no dicionário `estados`.
- As avaliações são armazenadas no dicionário `pesquisa`, associando cada estado a uma lista de objetos `Relevancia`.

### Requisitos

- Python 3.x

### Desenvolvedor

- Nome: [Seu Nome]
- Contato: [Seu E-mail]
 
