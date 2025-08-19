class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome 
        self.peso = peso 
        self.idade = idade
    def comer(self):
       print('{self.nome} esta comendo')

a1 = Animal('girafa','35kg' , '10')     
a2 = Animal('gato', '2kg', '3')
a3 = Animal('Leão', '20','5') 
print(a1.nome, a1.peso,a1.idade)
print(a2.nome,a2.peso,a2.idade)
print(a3.nome,a3.peso,a3.idade)
