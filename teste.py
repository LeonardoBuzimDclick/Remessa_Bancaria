import pygetwindow as gw
import pyautogui
import time
import re
from clicknium import clicknium as cc
from SUBPROGRAMS.parameters import *
from clicknium import locator, ui
from clicknium import clicknium as cc
import time
import subprocess
import pyautogui
from datetime import datetime, timedelta
import re
import pygetwindow as gw
import pyperclip
from SUBPROGRAMS.functions import *





'''# Função para verificar a última letra do padrão no arquivo
def verificar_ultima_letra(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            ultima_linha = linhas[-1].strip()
            return ultima_linha[-5]  # Última letra do padrão
        else:
            return None  # Se o arquivo estiver vazio

# Função para adicionar a próxima linha com o padrão correto
def adicionar_proximo_padrao(nome_arquivo):
    padrao = 'B202624'
    ultima_letra = verificar_ultima_letra(nome_arquivo)
    if ultima_letra:
        proxima_letra = chr(ord(ultima_letra) + 1)
        novo_padrao = f'\n{padrao}{proxima_letra}.txt'
    else:
        novo_padrao = f'\n{padrao}A.txt'
    
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(novo_padrao)
# Nome do arquivo
nome_arquivo = r"C:\\Projetos_Remessas\\Remessa_Pix\\controle_nome.txt"

# Adicionar o próximo padrão no arquivo
adicionar_proximo_padrao(nome_arquivo)'''

'''hora = datetime.now().time()
hora_atual = hora.hour
logging.debug(f'VERIFICANDO A HORA ATUAL {hora_atual}')

hoje = datetime.now()
logging.debug(f'hoje -  {hoje}')
dia_semana_hoje = hoje.weekday()  # Retorna um número entre 0 (segunda) e 6 (domingo)

if dia_semana_hoje in [2, 3, 4, 5, 6]:  # Quarta, quinta, sexta, sabado, domingo
    data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
    data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
elif dia_semana_hoje in [0]:  # Segunda
    data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
    data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
elif dia_semana_hoje in [1] and hora_atual < 12:  # Terça antes de meio dia
    data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
    data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
elif dia_semana_hoje in [1] and hora_atual >= 12:  # Terça depois de meio dia
    data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
    data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
else:
    # Lidar com outros dias da semana conforme necessário
    data_inicio = data_fim = None'''





'''data_hora = datetime.now().strftime('%Y-%m-%d %H:%M')
ref_processadas = ['985417', '123456', '789012']

# Especificar o caminho para a pasta onde você deseja salvar o arquivo
caminho_pasta_ref = r'C:\\Projetos_Remessas\\Remessa_Bancaria\\VariaveisControle'

# Verificar se o caminho da pasta existe, se não, criar
if not os.path.exists(caminho_pasta_ref):
    os.makedirs(caminho_pasta_ref)

# Caminho completo para o arquivo
caminho_arquivo = os.path.join(caminho_pasta_ref, 'ref_proc_form_pag_branco.txt')

# Abrir o arquivo em modo de escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrever a data e hora no arquivo
    arquivo.write(data_hora)
    # Escrever as referências no arquivo, separadas por espaços
    arquivo.write(' ' + ' '.join(ref_processadas))


# Verificar se o arquivo existe
if os.path.exists(caminho_pasta_ref):
    # Abrir o arquivo em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        # Ler a linha do arquivo
        linha = arquivo.readline().strip()  # Remove espaços em branco no início e no final da linha
        # Separar a linha em data/hora e referências
        partes = linha.split()
        data_hora_recuperada = partes[0]
        referencias_recuperadas = partes[1:]
else:
    print("O arquivo especificado não existe.")

print("Data e hora recuperadas:", data_hora_recuperada)
print("Referências recuperadas:", referencias_recuperadas)

def rename_variavel_controle():

    caminho_pasta_ref = r'C:\\Projetos_Remessas\\Remessa_Bancaria\\VariaveisControle'

    dt_inicial_format = inicio.strftime("%d-%m-%Y")
    dt_final_format = fim.strftime("%d-%m-%Y")
    logging.debug('CLICK - SELECIONA A DATA DE QUARTA FEIRA E DA PROXIMA TERÇA')
    logging.debug(f'QUARTA-FEIRA: {dt_inicial_format}')
    logging.debug(f'TERCA-FEIRA: {dt_final_format}')

    data_inicial_param = inicio.strftime("%d")
    data_final_param = fim.strftime("%d")
    data_ano_param = fim.strftime("%Y")
    dois_digitos_ano = str(data_ano_param)[-2:]

    # Liste todos os arquivos na pasta
    arquivos = os.listdir(caminho_pasta_ref)

    # Encontre a última letra usada
    arquivos_com_padrao = [arquivo[-5] for arquivo in arquivos if arquivo.startswith(f'B{data_inicial_param}{data_final_param}{dois_digitos_ano}') and arquivo.endswith('.txt')]
    print('ARQUIVO COM PARAO: ', arquivos_com_padrao)

    if arquivos_com_padrao:
        
        # Novo nome do arquivo
        novo_nome = (f'B{data_inicial_param}{data_final_param}{dois_digitos_ano}.txt')
        logging.debug(f'NOME ARQUIVO: B{data_inicial_param}{data_final_param}{dois_digitos_ano}.txt')'''

"""for i in range (3):

    cont = 0

    while cont <= 20:

        bordero_click = waitForImage(image = bordero, timeout=60, name = 'IMAGEM BORDERO')
        if bordero_click is not None:
            time.sleep(2)
            pyautogui.click(bordero_click)
            logging.debug('IMAGEM BORDERO CLICADA.')

        licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
        if licencas is not None:
            logging.debug('LICENCAS EXCEDIDAS')
            logging.debug(f'TENTANDO NOVAMENTE - {cont+1}')
            pyautogui.hotkey(f'esc')
            if cont == 50:
                logging.debug('ENVIANDO EMAIL DE ERRO')
                texto_msg = 'LICENCAS EXCEDIDAS'
                emailErro(texto_msg)
                end_RM()
            cont += 1
            time.sleep(20)

        else:
            break

        '''licencas2 = waitForImage(image = licencas_2, timeout=2, name = 'LICENCE SERVER')
        if licencas2 is not None:
            time.sleep(2)
            for i in range(5):
                pyautogui.press('tab')
                time.sleep(1)
                
            pyautogui.press('enter')'''

    filtro_movimentacao = cc.wait_appear(locator.rm.titlebar_titlebar, wait_timeout=120)
    if filtro_movimentacao is not None:
        logging.debug('ENCONTROU O FILTRO DA MOVIMENTAÇÃO BANCÁRIA')
        break

filtro_movimentacao.click()
logging.debug('CLICA NA ABA SUPERIOR DO FILTRO')

time.sleep(6)
for i in range(2):
    pyautogui.press('down')
    time.sleep(0.5)
'''pyautogui.write('hoje')
time.sleep(1)'''
pyautogui.press('enter')
logging.debug('SELECIONA O FILTRO HOJE')"""


'''click_filter = cc.wait_appear(locator.rm.titlebar_titlebar4, wait_timeout=120)
if click_filter is not None:
    click_filter.click()
    time.sleep(2)
    pyautogui.hotkey('esc')

pyautogui.hotkey('ctrl', 'w')
time.sleep(2)
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)
pyautogui.hotkey('ctrl', 'w')'''


'''import requests
try:
    response = requests.get('https://www.google.com')
    print(response.status_code)
except Exception as e:
    print(e)'''

'''menuitem_inclusao_bordero = cc.wait_appear(locator.rm.button_bordero_inclusao_trespontos, wait_timeout=60)
menuitem_inclusao_bordero.click()
logging.debug('CLICA EM CONVÊNIO TRÊS PONTINHOS')

combo_sispag = cc.wait_appear(locator.rm.combobox_sispag, wait_timeout=15)
combo_sispag.click()
logging.debug('CLICA EM COMBOBOX PARA SELECIONAR O ID DO CONVÊNIO')

select_convenio = cc.wait_appear(locator.rm.listitem_id_convenio, wait_timeout=15)
select_convenio.click()
logging.debug('CLICA EM ID DO CONVÊNIO')

time.sleep(2)
pyautogui.press('tab')
logging.debug('APERTA TAB PARA ESCREVER O ID')

time.sleep(2)
pyautogui.write('7')
logging.debug('ESCREVE O ID 7')

time.sleep(2)
pyautogui.press('enter')
logging.debug('APERTA ENTER PARA SELECIONAR O ID 7 - SISPAG FORNECEDOR')

time.sleep(2)
pyautogui.press('enter')
logging.debug('APERTA ENTER PARA ESCOLHER O ID 7 - SISPAG FORNECEDOR')
time.sleep(2)'''

#rename_arq()
'''def excel():
    #global workbook

    logging.info('Criando EXCEL')

    workbook = openpyxl.Workbook()

    sheet = workbook.active
    #sheet = workbook.create_sheet("Liq Cambio - Processados")
    sheet.title = 'Referencia - Data Prev Baixa'
    logging.info('Referencia - Data Prev Baixa')

    sheet["A1"] = "Referencia"
    sheet["B1"] = "Data Prev Baixa"
    
    for linha in lista_ref_data:
    
        row_index = 1
        while sheet[f'A{row_index}'].value is not None:
            row_index += 1
        
        sheet[f'A{row_index}'] = linha["referencia"]
        sheet[f'B{row_index}'] = linha["data"]
    
    workbook.save(f'{excel_path}/{today}/teste.xlsx') 
    
    logging.info('EXCEL Criado')
    
    
    
    
    
    
lista_ref_data = []
for i in range (3):
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    ref_atual_string = pyperclip.paste()
    logging.debug(f'REF. LANÇAMENTO: {ref_atual_string}')
    #logging.debug(f'REF. LANÇAMENTO TIPO: {type(ref_atual_string)}')

    for i in range(7):
        time.sleep(0.3)
        pyautogui.press('right')

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    data_prev_baixa = pyperclip.paste()
    logging.debug(f'DATA PREVISÃO DE BAIXA: {data_prev_baixa}')

    for i in range(7):
        time.sleep(0.3)
        pyautogui.press('left')
        
    ref_data = {
                'referencia': ref_atual_string,
                'data': data_prev_baixa
                }
            
    logging.info(ref_data)
    lista_ref_data.append(ref_data)

    pyautogui.hotkey('down')
    
excel(lista_ref_data)'''


bordero_click = waitForImage(image = bordero, timeout=60, name = 'IMAGEM BORDERO')
if bordero_click is not None:
    time.sleep(2)
    pyautogui.click(bordero_click)
    logging.debug('IMAGEM BORDERO CLICADA.')