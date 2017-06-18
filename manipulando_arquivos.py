
import random
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# abrir para leitura
f = open('/my_path/my_file.txt', 'r')

# trasnforma o aquivo em uma string para leitura
file_data = f.read()

# TODO: sua função aqui


# Ao final liberar o recurso
f.close()

# abrir para escrita
f = open('/my_path/my_file.txt', 'w')
f.write("Hello World!")
f.close()


# Python gerencia o fechamento automatico do arquivo se usar 'with'.
with open('/my_path/my_file.txt', 'r') as f:
    file_data = f.read()


def create_cast_list(filename):
    cast_list = []
    # abrir um arquivo e recuperar apenas os primeiros dados até encontrar uma
    # virgula ','.
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    return cast_list


print(create_cast_list("flying_circus_cast.txt"))

# ** Modulos uteis **8
# csv: muito conveniente para ler e escrever arquivos csv
# collections: extensões úteis dos tipos de dados habituais,
# 			   incluindo OrderedDict, defaultdict e namedtuple
# random: gera números pseudo-aleatórios, embaralha sequências
# 			   aleatoriamente e escolhe itens aleatórios
# string: mais funções em strings. Este módulo também contém
# 		  	   coleções úteis de letras como string.digits
# 		  	   (uma string contendo todos os caracteres com dígitos válidos).
# re: padronização em strings através de expressões regulares
# math: algumas funções matemáticas padrão
# os: interagindo com sistemas operacionais
# os.path: submódulo de os para manipular nomes de caminho
# sys: trabalhar diretamente com o interpretador Python
# json: bom para ler e escrever arquivos json (bom para o trabalho na web)

word_list = []


def generate_password():
    return str().join(random.sample(word_list, 3))


def generator_password():
    return random.choice(word_list) + \
        random.choice(word_list) + random.choice(word_list)


# ** MODULOS DE TERCEIROS UTEIS **
# IPython - Um interpretador melhor interativo de Python
# requests - Fornece métodos fáceis de usar para fazer solicitações na web.
# Flask - Uma estrutura leve para fazer aplicações web e APIs.
# Django - Uma estrutura com mais recurso para fazer aplicações web.
# 			O Django é particularmente bom para projetar, conteúdo pesado,
# 			aplicações web.
# Beautiful Soup - Usado para analisar HTML e extrair informações dele.
# 			Ótimo para web scraping.
# pytest - Estende Python construído em asserções e módulo de teste de unidade.
# PyYAML - Para ler e escrever arquivos YAML.
# NumPy - O pacote fundamental para computação científica com Python.
# 			Contém, entre outras coisas, um poderoso objeto de matriz N-dimensional
# 			e capacidades úteis de álgebra linear.
# pandas - Uma biblioteca contendo alto desempenho, estruturas de dados
# 			e ferramentas de análise de dados. Em particular,
# 			pandas fornece dataframes!
# matplotlib - Uma biblioteca 2D de plotagem que produz qualidade de publicação
# 			de figuras em uma variedade de formatos impressos e ambientes interativos.
# ggplot - Outra biblioteca de plotagem 2D, baseada na biblioteca ggplot2 de R.
# Pillow - Uma biblioteca de imagens Python que adiciona recursos
# 			de processamento de imagem ao seu intérprete Python.
# pyglet - Um framework de aplicação multiplataforma destinado ao
# 			desenvolvimento de jogos.
# Pygame - Um conjunto de módulos Python projetado para escrever jogos.
# pytz - World Timezone Definições para Python
