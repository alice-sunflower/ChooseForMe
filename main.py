#Criar um script que responda qualquer pergunta que for feita a ele. 

#Importar do módulo "RANDOM" a função "CHOICE" para escolher uma das strings dentro da lista "RESPOSTAS"
from random import choice

#Criar uma lista "RESPOSTAS" para poder usá-las quando o usuário fizer uma pergunta
respostas = ['Sim', 'Não', 'Sim!', 'Não!', 'Acho que sim...', 'Acho que não...', 'Claro que sim!', 'Claro que não!', 'De maneira alguma', 'Credo.', 'Mete o loco e foda-se']
rejeitados = ['?', ' ', '!', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Loop que pode ser quebrado pelo usuário
ok = True
while ok:
    pergunta = str(input('O que deseja perguntar? ')).replace(' ', '').replace('?', '')
    for x in rejeitados:
        pergunta.replace(x, '')
    if pergunta.isalpha() == True:
        print(choice(respostas))
    else:
        print('Faça uma pergunta!')
    while ok:
        opcao_fim = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao_fim in 'SN':
            if opcao_fim == 'S':
                break
            elif opcao_fim == 'N':
                ok = False

print('Volte sempre!')
