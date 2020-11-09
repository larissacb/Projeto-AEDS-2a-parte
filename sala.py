class Sala:
    def __init__(self, nome, lotacao):
        self.nome=nome
        self.lotacao=lotacao
        self.matriz_horarios=list()
        # a matiz de horarios tem 6 linhas, 8 colunas e armazena strings
        # cada linha representa um dia semana
        #a coluna representa um dos horarios
        self.matriz_horarios=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def getLotacao(self):
        return self.lotacao


        
        
        
        
        
