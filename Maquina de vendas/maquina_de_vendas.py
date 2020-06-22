print('Linguagens Formais e Automatos CCP 7A')
print('Rodrigo Luis Manzieri Oliveira - RGM 17467152\n')
print('Maquina de venda')
print('Cocacola custa $0.45\n')

print('Digite:\n\"quarter\" para inserir $0.25\n\"dime\" para inserir $0.10\n\"finalizar\"\n')
current_value = 0
while current_value < 0.45:
    option = input('Opcao: ')

    if option == 'dime':
        current_value += 0.101
    elif option == 'quarter':
        current_value += 0.25
    elif option == 'finalizar':
        exit
    else:
        option = input('Opcao invalida!\nDigite novamente a opcao: ')
    if current_value >= 0.45: break

if current_value >= 0.45: print ('Pegue sua cocacola')
input()