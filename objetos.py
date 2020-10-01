class Empregado:
    # Magic/dunder method
    # constructor
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = nome + '.' + sobrenome + '@gmail.com'
        self.salario = salario
        
        Empregado.num_empregados += 1

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.porcetagem_aumento
        
    def __str__(self):
        return f'{self.nome_completo()} - {self.email}'
        
emp_1 = Empregado('Fulano', 'Silva', 10000)
emp_2 = Empregado('Boltrano', 'Silva', 5000)

print('Total de empregados:', Empregado.num_empregados)
# empregado_1.nome = 'Teste 1'
# empregado_2.telefone = '1234'

# print(Empregado.__dict__)
# print('Empregado 1:', empregado_1.__dict__)
# print('Empregado 2:', empregado_2.__dict__)