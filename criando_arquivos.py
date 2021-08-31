import shutil

diretorio = 'J:/Estudos/DATA-ENGENIER/'

def escrever_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

def media_nota(nome_arquivo):
    arquivo=open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_medias=[]
    for i in aluno_nota:
        lista_nota = i.split(',')
        aluno = lista_nota[0]
        notas =lista_nota[1:5]
        media =lambda nota: sum([float(i) for i in nota])/4
        lista_medias.append({aluno:media(notas)})
    return lista_medias

def copia(nome_arquivo):
    shutil.copy(nome_arquivo,diretorio)

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,diretorio)

if __name__ == '__main__':
   lista = media_nota('J:/Estudos/DATA-ENGENIER/notas.txt')
   for i in lista :
        dados_aluno=str(i)
        dados_aluno=(dados_aluno.replace("{'",''))
        dados_aluno = (dados_aluno.replace("':", ','))
        dados_aluno = (dados_aluno.replace("}", '\n'))
        atualizar_arquivo('J:/Estudos/DATA-ENGENIER/medias_aluno.txt',dados_aluno)
print('Dados inseridos')
