# criando uma lista 
# Ivan,Gustavo,Tarso,vitor,Gabriel,Rafael,Fabricio,
# Qual seria o print e 
# input para pedir nomes?
# nomes=input('Digite seu nome separado por uma virgula: ') .split(',')
# lista_de_nomes=['Ivan,''Gustavo','Tarso','vitor','Gabriel','Rafael','Fabricio']
# print(f'Lista de nomes:{nome}')
# nomes=[nome.split() for nome in nomes]
# print(nomes)
# print('\n Quais operações você quer fazer?')
# print("1- Adicionar um nome")
# print("2- Remover um nome ")
# print("3- Listar nomes ")
# print("4- sair")


def menu_principal():
    print('\n Quais operações você quer fazer?')
print("1- Adicionar um nome")
print("2- Remover um nome ")
print("3- Listar nomes ")
print("4- sair")


while True:
  opcao=input('Digite a opção desejada (1-4):')
  if opcao =='1':
    print(F"foi adicionado a lista. ")
    nome=input('Digite um nome:')
    print(f'O {nome} foi adicionado a lista')
   
  elif opcao  =='2':
   print('remover nomes'.lower())
   remover=input('Qual nome deseja remover da lista?')
   print(f'O nome {remover} foi retirado da lista')


  elif opcao =='3':
    print('listar nomes.')
    nomes=input('Digite os nomes que deseja listar:')
    print(f'Aqui está sua lista de nomes: {nomes} ')

else:
   print('você não escolheu uma opção')