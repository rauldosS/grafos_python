# Comentário de uma linha

valor = 10
print('valor:', valor, end='')
print('porcentagem: ', valor, '%', sep='')

baseline = {'music': 'bach', 'art': 'rembrandt'}
print(type(baseline))

nome = 'raul'
idade = 20
salario = 200
print('nome: %s idade: %d salaório: R$ %.2f' % (nome, idade, salario))

idade = int(input('Digite sua idade:'))
print('Você nasceu em ', 2020-idade)