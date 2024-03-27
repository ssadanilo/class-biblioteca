# Crie as classes Livro, Membro e Biblioteca para representar os elementos da biblioteca.

# A classe Livro deve conter atributos como título, autor, ID e status de empréstimo (disponível ou 
# emprestado).

# A classe Membro deve incluir atributos como nome, número de membro e histórico de livros emprestados.

# A classe Biblioteca deve manter um catálogo de livros disponíveis, um registro de membros e métodos para 
# operações como empréstimo, devolução e pesquisa de livros.

# Implemente métodos na classe Biblioteca para adicionar livros ao catálogo, adicionar membros à biblioteca,
# permitir empréstimo de livros por membros, registrar a devolução de livros e pesquisar livros por título, 
# autor ou ID.

# Desenvolva uma interface de linha de comando ou uma interface gráfica simples usando tkinter para permitir
# que os usuários interajam com a biblioteca. Esta interface deve oferecer funcionalidades como adicionar 
# livros, adicionar membros, emprestar e devolver livros, e pesquisar livros por diferentes critérios.
# O projeto será estruturado em classes e utilizará conceitos de programação orientada a objetos para criar
# uma aplicação de gerenciamento de biblioteca funcional e interativa.

# Criando a classe Livro
class Livro:
    def __init__(self, titulo, autor, ID, status_de_emprestimo):
        self.titulo = titulo
        self.autor = autor
        self.ID = ID
        self.status_de_emprestimo = status_de_emprestimo

# Criando a classe Membro
class Membro:
    def __init__(self, nome, numero_de_membro):
        self.nome = nome
        self.numero_de_membro = numero_de_membro
        self.historico_de_emprestimos = []

# Criando a classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros_disponiveis = [] # Lista de livros disponíveis na biblioteca
        self.registro_de_membros = [] # Lista de membros registrados na biblioteca

    def adicionar_livro(self, Livro): # Metodo para adicionar livros a biblioteca
        self.livros_disponiveis.append(Livro)
        print(f'O livro {Livro.titulo} foi adicionado com sucesso!')

    def adicionar_membro(self, membro): # Metodo para adicionar membros a biblioteca
        self.registro_de_membros.append(membro)
        print(f'O membro {membro.nome} foi adicionado com sucesso!')

    def emprestimo_de_livros(self, livro, membro): # Metodo para devolver livros a biblioteca
        if livro in self.livros_disponiveis:
            if livro.status_de_emprestimo == False: # Método padrão onde o status começa False
                livro.status_de_emprestimo = True
                membro.historico_de_emprestimos.append(livro)
                print(f'O livro {livro.titulo} agora é emprestado a {membro.nome}.')
            else:
                print(f'O livro {livro.titulo} já se encontra emprestado.')

        else:
            print(f'O livro {livro.titulo} não existe na biblioteca')     

    def registrar_devolucao(self, livro): # Metodo para registrar a devolução livros na biblioteca pelos usuários
        if livro in self.livros_disponiveis:
            if livro.status_de_emprestimo:
                livro.status_de_emprestimo = False
                print(f'O livro {livro.titulo} foi devolvido com sucesso.')
            else:
                print(f'O livro {livro.titulo} não estava emprestado.')
        else:
            print(f'O livro {livro.titulo} não existe na biblioteca')

    def pesquisar_livros(self, titulo='', autor='', ID=None): # Metodo para pesquisar livros na biblioteca
        livros_encontrados = [] # Lista para livros que forem encontrados em pesquisa
        for livro in self.livros_disponiveis: # Buscando todos os livros disponíveis com os resultados abaixo
            if (titulo.lower or livro.titulo.lower() == titulo.lower()) and \
               (autor.lower or livro.autor.lower() == autor.lower()) and \
               (ID or livro.ID == ID): # Pesquisa por título, autor e ID
                livros_encontrados.append(livro) # Salvado os livros pesquisados na lista de livros encontrados
        if livros_encontrados:
            for livro_encontrado in livros_encontrados: # apresentnado ao usuário os livros encontrados na sua pesquisa, e informando se está disponível ou não para empréstimo
                print(f'Livros encontrados: Título/{livro_encontrado.titulo} - Autor/{livro_encontrado.autor} - ID/{livro_encontrado.ID}.')
                print(f'Status de empréstimo: {"Disponível" if not livro_encontrado.status_de_emprestimo else "Emprestado"}')
        else:
            print(f'Nenhum livro encontrado com esses critérios de pesquisa.')

# Criando livros    
livro1 = Livro('Duna', 'Frank Herbert', 1, False )
livro2 = Livro('O último Reino', 'Bernard Cornwell', 2, False )
livro3 = Livro('Os Sete', 'André Vianco', 3, False)

# Criando membros
membro1 = Membro('Raimundo Nonato Tavares da Silva', 701)
membro2 = Membro('Edson Arantes do Nascimento', 702)

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros a biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Adicionando membros a biblioteca
biblioteca.adicionar_membro(membro1)
biblioteca.adicionar_membro(membro2)

# emprestado livros aos membros
biblioteca.emprestimo_de_livros(livro1, membro1)
biblioteca.emprestimo_de_livros(livro2, membro1)
biblioteca.emprestimo_de_livros(livro3, membro2)

# Registrando a devolução de livros por membros
biblioteca.registrar_devolucao(livro2)
biblioteca.registrar_devolucao(livro3)

# Pesquisando livros na biblioteca
biblioteca.pesquisar_livros('Duna','','')
biblioteca.pesquisar_livros('','Bernard Cornwell','')
biblioteca.pesquisar_livros('','','3')
