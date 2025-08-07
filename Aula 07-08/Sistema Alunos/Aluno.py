class Aluno:
    def __init__(self):
        if nome == "" or not nome:
            print("Nome inválido. Por favor, insira um nome válido.")
            raise ValueError("Nome inválido")

        self.nome = ""
        self.matricula = ""
        self.curso = curso

    def exibir_dados(self):
        return f'''
Informações do Aluno:
Nome: {self.nome}
Matrícula: {self.matricula}
Curso: {self.curso}
'''
    