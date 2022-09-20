notas = []
alunos = []

def e_escola():
    novo_nome = input("Digite o nome do aluno: ")
    nova_nota = input("Digite a nota: ")
    alunos.append(novo_nome)
    notas.append(nova_nota)

def diario_classe():
    while True:
        e_escola()
        
        for i in range(len(notas)):
            print(i)
            print("Aluno: ", alunos[i+1])
            print("Nota: ", notas[i+1])
            print("Atualizado!")

            finalizar = input("Deseja finalizar? (s/n)")
            if finalizar == "s":
                break

diario_classe()