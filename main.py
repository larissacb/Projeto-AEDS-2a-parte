from turma import Turma
from sala import Sala

#============================================================================================================================================
menu=False
aux=list()
turmas=list()
salas=list()

#============================================================================================================================================
def menu_inicial():
    print("======== Menu ========")
    print("1 - Imprimir turmas")
    print("2 - Ler um novo arquivo de demanda de salas")
    print("3 - Alocacao das salas conforme a demanda ja apresentada")
    print("0 - Sair")
    op = int(input("Informe a opcao desejada: "))
    return op

#============================================================================================================================================
def abre_arq_cursos(arq):
    #teste para verificacao de arquivos com nomes errados ou inexistentes
    try:
        fhand=open(arq)
    except:
        print("O arquivo com o nome informado nao pode ser localizado e/ou aberto")
        quit()

    for linha in fhand: #lendo cada linha do arquivo
        linha = linha.rstrip()
        aux = linha.split()  #quebro a linha em varias strings
        curso = aux[0]
        disciplina = aux[1]
        professor = aux[2]
        num_alunos = int(aux[3])
        turno = aux[4]
        obj1 = Turma(curso, disciplina, professor, num_alunos, turno)  # criando um objeto
        turmas.append(obj1)#adiciono o objeto que foi criado a lista de turmas
        
#============================================================================================================================================
def abre_arq_salas():
    salas1 = input("Informe o nome do arquivo com os dados das salas disponiveis no campus: ")
    #teste para verificacao de arquivos com nomes errados ou inexistentes
    try:
        fhand=open(salas1)
    except:
        print("O arquivo com o nome informado nao pode ser localizado e/ou aberto")
        quit()

    for linha in fhand: #lendo cada linha do arquivo
        linha = linha.rstrip()
        aux = linha.split()  # quebro a linha em varias strings
        sala=aux[0]
        lotacao=int(aux[1])
        obj2 = Sala(sala, lotacao) #criando um obejto do tipo Sala e adicionando o nome da sala e a sua lotacao
        salas.append(obj2)#adiciono o objeto que foi criado a lista de salas
#============================================================================================================================================
#antes de mais nada, informar o arquivo com as salas disponiveis no campus
abre_arq_salas()

menu=True
while (menu==True):
    op=menu_inicial() #chama a funcao do menu
    if (op==1): #Imprimir turmas
        for i in range(len(turmas)):  #percorrendo a lista com as turmas
            turmas[i].imprimir_inf()
    
    elif (op==2): #Ler um novo arquivo de demanda de salas
        arq=input("Informe o nome do arquivo de demanda de salas: ")
        abre_arq_cursos(arq)

    elif(op==3): #Alocacao das salas conforme a demanda ja apresentada
        print("Em construcao. Utilizar a busca tabu")

    elif (op==0): #Sair
        print("Saindo...")
        salas.clear() #apagando a lista com as salas do campus
        turmas.clear() #apagando a lista com as turmas
        break #quebra o loop do menu
        
    else: #Opcao invalida
        print("Opcao invalida!")
