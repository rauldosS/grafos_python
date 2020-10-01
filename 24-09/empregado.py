class Empregado:
    num_empregados = 0
    
    # Contructor
    def __init__(self, nome):
        self.nome = nome
        
        Empregado.num_empregados += 1
    
    def __str__(self):
        return "Empregado: " + self.nome
    
empregado_1 = Empregado('Fulano')
empregado_1 = Empregado('Siclano')

print(empregado_1)
print("# empregados:", Empregado.num_empregados)