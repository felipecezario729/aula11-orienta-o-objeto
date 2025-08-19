class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1= Pessoa('Andre','Marque')
p2= Pessoa('Gilmar','Santos')
print(p1.nome)
print(p1.sobrenome)
print('===')
print(p2.nome)
print(p2.sobrenome)