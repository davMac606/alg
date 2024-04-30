
def apresenteSe():
    print('+-------------------------------------------------------------+\n\
           |                                                             |\n\
           | AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |\n\
           |                                                             |\n\
           |                                                             |\n\
           | Versão 1.0 de 12/abril/2024                                 |\n\
           |                                                             |\n\
           +-------------------------------------------------------------+')

def text (solicitacao, mensagem, validate):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in validate:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def chosen(mnu):
    print ()

    opcoesValidas=[]
    pos=0
    while pos<len(mnu):
        print (pos +1,') ',mnu[pos],sep='')
        opcoesValidas.append(str(pos + 1))
        pos += 1

    print()
    return text('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta (nom,agd):
    inicio= 0
    final = len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')




def procurar (agd):

    digitouDireito = False
    while not digitouDireito:

        nome = input("Digite o nome completo do contato: ")
        Lista_decontato = ondeEsta (nome, agd)
        achou = Lista_decontato [0]
        posicao = Lista_decontato [1]

    if nome not in Lista_decontato:
        print ("Este contato não existe, tente novamente")
    
    else:
    
        print('Aniversario:',agd[posicao][1])
        print('Endereco...:',agd[posicao][2])
        print('Telefone...:',agd[posicao][3])
        print('Celular....:',agd[posicao][4])
        print('e-mail.....:',agd[posicao][5])
        
        digitouDireito= True

    


    print (procurar(Lista_decontato))
    return Lista_decontato
    print (procurar(Lista_decontato))


def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

def atualizar():
    print("Não implementado.")

def listar():
    print("Não implementado.")
# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')


























#omo cu cabeludo
def text(inputText, mensagem, validate):
    digitouDireito=False
    while not digitouDireito:
        txt=input(inputText)

        if txt not in validate:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def chosen(mnu):
    print ()

    opcoesValidas=[]
    pos=0
    while pos<len(mnu):
        print (pos+1,') ',mnu[pos],sep='')
        opcoesValidas.append(str(pos+1))
        pos+=1

    print()
    return text('Qual é a sua opção? ', 'Opção inválida. Por favor, tente novamente.', opcoesValidas)

def pos(nom,agd):
    ini=0
    final =len(agd)-1
    
    while ini<=final:
        meio=(ini+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]


def create (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=pos(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario= input('Aniversário: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    celular = input('Celular: ')
    email = input('e-mail: ')
    contato=[nome,aniversario,endereco,telefone,celular,email]
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')
    
    
def procura(agd):
    nome=input('Nome a ser procurado: ')
    resposta=pos(nome,agd)
    achou = resposta[0]
    posicao = resposta[1]
    
    if achou:
        print('Nome:',agd[posicao][0])
        print('Aniversário:',agd[posicao][1])
        print('Endereço:',agd[posicao][2])
        print('Telefone:',agd[posicao][3])
        print('Celular:',agd[posicao][4])
        print('e-mail:',agd[posicao][5])
    else:
        print('Nome não encontrado!')
