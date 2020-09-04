class Empregado:
    # Magic/dunder method
    # constructor
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = nome + '.' + sobrenome + '@gmail.com'
        self.salario = salario

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)
        
    def __str__(self):
        return f'{self.nome_completo()} - {self.email}'
        
empregado_1 = Empregado('Raul', 'Moraes', 10000)
empregado_2 = Empregado('Beltrano', 'Moraes', 5000)
empregado_3 = Empregado('Raul', 'Moraes', 10000)

print(empregado_1)

# empregado_1.nome = 'Teste 1'
# empregado_2.telefone = '1234'

# print(Empregado.__dict__)
# print('Empregado 1:', empregado_1.__dict__)
# print('Empregado 2:', empregado_2.__dict__)