from abc import ABC, abstractmethod

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    @abstractmethod
    def realizar_emprestimo(self):
        pass

# Classe UsuarioComum (subclasse de Pessoa)
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.livros_emprestados = []

    def realizar_emprestimo(self, livro):
        if len(self.livros_emprestados) < 3 and livro.status == "disponível":
            self.livros_emprestados.append(livro)
            livro.status = "emprestado"
            print(f"Livro '{livro.titulo}' emprestado para {self.nome}.")
        else:
            print(f"Empréstimo não permitido. Limite de livros ou disponibilidade do livro.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.status = "disponível"
            print(f"Livro '{livro.titulo}' devolvido por {self.nome}.")
        else:
            print("Este livro não foi emprestado por você.")

# Classe Administrador (subclasse de Pessoa)
class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)

    def realizar_emprestimo(self, livro):
        print("Administrador não realiza empréstimos diretamente.")
    
    def cadastrar_livro(self, biblioteca, livro):
        biblioteca.adicionar_livro(livro)
        print(f"Livro '{livro.titulo}' cadastrado na biblioteca.")

# Classe abstrata ItemBiblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

    @abstractmethod
    def exibir_informacoes(self):
        pass

# Classe Livro (subclasse de ItemBiblioteca)
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor)
        self.ano_publicacao = ano_publicacao

    def exibir_informacoes(self):
        return f"'{self.titulo}' de {self.autor} ({self.ano_publicacao}) - Status: {self.status}"

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def exibir_livros_disponiveis(self):
        for livro in self.livros:
            if livro.status == "disponível":
                print(livro.exibir_informacoes())

    def exibir_usuarios_com_emprestimos(self):
        for usuario in self.usuarios:
            if usuario.livros_emprestados:
                livros_emprestados = [livro.titulo for livro in usuario.livros_emprestados]
                print(f"{usuario.nome} tem os seguintes livros emprestados: {', '.join(livros_emprestados)}")

# Exemplo de uso
biblioteca = Biblioteca()

# Criando livros e usuários
livro1 = Livro("Python para Iniciantes", "Autor A", 2020)
livro2 = Livro("Estruturas de Dados", "Autor B", 2019)

usuario1 = UsuarioComum("João", 25, "123")
administrador = Administrador("Carlos", 40, "456")

# Cadastrando na biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(administrador)

# Empréstimo de livro
usuario1.realizar_emprestimo(livro1)

# Exibindo livros disponíveis e usuários com empréstimos
biblioteca.exibir_livros_disponiveis()
biblioteca.exibir_usuarios_com_emprestimos()
