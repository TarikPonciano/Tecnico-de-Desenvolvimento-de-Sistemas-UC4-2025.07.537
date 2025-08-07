from Aluno import Aluno

alunos = []

while True:
    print("Digite as informações do aluno:")

    nome = input("Nome: ")

    matricula = input("Matricula: ")
    curso = input("Curso: ")

    try:
        novo_aluno = Aluno(nome, matricula, curso)
        alunos.append(novo_aluno)
    except Exception as e:
        print(f"Erro: {e}")

    op = input("Deseja adicionar outro aluno? (s/n): ")

    if op.lower() != 's':
        break

for aluno in alunos:
    print(aluno.exibir_dados())
