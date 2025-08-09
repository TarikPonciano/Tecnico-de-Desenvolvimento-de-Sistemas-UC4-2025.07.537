# Crie um sistema de consumo de itens multimídia. Nesse sistema estão presentes Filmes, Livros e Músicas. Crie uma superclasse "Midia" que contém pelo menos 5 atributos comuns à qualque mídia e que possua pelo menos 3 métodos (operações que podem ser feitos com ele). Implemente as subclasses Filmes, Livros e Músicas e crie pelo menos 1 método e 1 atributo único para cada um.

class Midia:
    def __init__ (self, titulo, genero, ano_lancamento, formato, tamanho):
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.formato = formato
        self.tamanho = tamanho
    def remover_do_acervo(self):
        pass
    def renomear(self):
        pass
    def acessar(self):
        pass

class Livro(Midia):
    def __init__(self, titulo, genero, ano_lancamento, formato, tamanho, paginas):
        super().__init__(titulo, genero, ano_lancamento, formato, tamanho)
        self.paginas = paginas
    def passar_pagina(self):
        pass

class Musica(Midia):
    def __init__(self, titulo, genero, ano_lancamento, formato, tamanho, album):
        super().__init__(titulo, genero, ano_lancamento, formato, tamanho)
        self.album = album
    def aumentar_volume(self):
        pass

class Filme(Midia):
    def __init__(self, titulo, genero, ano_lancamento, formato, tamanho, resolucao):
        super().__init__(titulo, genero, ano_lancamento, formato, tamanho)
        self.resolucao = resolucao
    def fullscreen(self):
        pass
