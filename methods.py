'''
def procurar (Lista_decontato):

digitouDireito = False
while not digitouDireito:
nome = input("Digite o nome completo do contato: ")
Lista_decontato = ondeEsta (nome, agd)

if nome not in Lista_decontato:
print ("Este contato não existe, tente novamente")


print (procurar(Lista_decontato))

return Lista_decontato
print (procurar(Lista_decontato))
'''