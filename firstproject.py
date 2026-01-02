#Para pegar a data automáticamente
from datetime import datetime
from fpdf import FPDF

data_hoje = datetime.now().strftime('%d/%m/%Y')

# Função para perguntar nota de sintoma

def perguntar_nota(sintoma):
    return input('Nota de 0 a 10 para {sintoma}: ')

# Função para resposta S ou N

def perguntar_sn(pergunta):
    while True:
        resposta = input(f'{pergunta} (S ou N): ').strip().upper()
        if resposta in ('S', 'N'):
            return resposta

        else:
            print('Resposta invalida!')



#Dicionário para armazenar as repostas
respostas  = {}

respostas['alimentos'] = input ('O que você comeu hoje? ')

respostas['gases'] = perguntar_sn('gases ')
respostas['nota_gases'] = perguntar_nota ('gases')

respostas['refluxo'] = perguntar_sn('refluxo ')
respostas['nota_refluxo'] = perguntar_nota ('refluxo')

respostas['barriga inchada'] = perguntar_sn('barriga inchada ')
respostas['nota_barriga_inchada']= perguntar_nota ('barriga_inchada')

respostas['queimação'] = perguntar_sn('queimação ')
respostas['nota_queimação'] = perguntar_nota ('queimação')

respostas['liquidos'] = perguntar_sn('Incluiu líquidos nas refeições? ')
respostas['nota_líquidos'] = perguntar_nota ('líquidos')

respostas['evacuações'] = input('Número de evacuações no dia: ')
respostas['água'] = input('Quantidade de água ao longo do dia (copos/garrafas): ')

print(respostas)



#Classe pdf

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0,10, 'Relatório Diário dos Desconfortos', align='C')
        self.ln(10)



    def add_respostas (self, respostas):
        self.set_font('Arial', '', 12)
        for chave, valor in respostas.items():
            chave_formatada= chave.replace('_',' ').capitalize()
            self.multi_cell(0,8, f'{chave_formatada}: {valor}')
            self.ln(1)



# Criar o PDF

pdf = PDF()
pdf.add_page()
pdf.add_respostas(respostas)

# Salvar o arquivo

pdf.output('relatório_desconfortos.pdf')
