class Aluno:
    def __init__(self, codigo , nome , matricula):
        self.nome = nome
        self.codigo = codigo 
        self.matricula = matricula

    def __str__(self):
        texto = "Produto: " + self.nome 
        texto += "\nCodigo: " + str( self.codigo) 
        texto += "\nM " + self.cat.nom 
        return texto

class AlunoEnsinoMedio:
    def __init__(self, ano):
        self.ano = ano 

    def __str__(self):
        return
