import yagmail
import yaml
import logging
import os
import sys
import pyautogui
from datetime import datetime
from timeit import default_timer as timer
import ctypes
import keyboard
import openpyxl

pyautogui.FAILSAFE = False
ref_out = []
base_path = os.getcwd()
log_path = f'{base_path}/LOG'
email_path = f'{base_path}/EMAIL'
image_path = f'{base_path}/IMAGES'
print_path = f'{base_path}/PRINTS'
excel_path = f'{base_path}/EXCEL'
#user = 'integracao'
user = 'dclick'
password = 'arrobaint;321'
inv = 'INV'
nome_processo = 'RM.exe'
caminho_da_primeira_pasta = r'C:\\Totvs\\Remessa'
caminho_da_pasta = r'\\riofs\\dados\\Documentos Financeiro\\Contas a Pagar\\Remessas'
caminho_da_pasta_data = r'C:\\Projetos_Remessas\\Remessa_Pix'


clientes = ['006530', '004529', '009020', '009057', '006490', '004067', '003467', '004858', '005120', '005121', '006892', '008144', '005796']

with open('config.yaml', 'r', encoding='utf=8') as params:
    config = yaml.safe_load(params)

print(config)

email_login = config['email']['login']
email_password = config['email']['password']
email_receivers = config['email']['receivers']
email_receivers1 = config['email']['receivers_1']
log_level = config['logLevel']


yag = yagmail.SMTP(user=email_login, password=email_password)



# log configs
today = datetime.today().strftime('%d-%m-%Y')
log_file_name = datetime.now().strftime('%H_%M_%S')

if os.path.exists(f'{log_path}/{today}') == False:
    os.makedirs(f'{log_path}/{today}')
    
if  os.path.exists(f'{excel_path}/{today}') == False:
    os.makedirs(f'{excel_path}/{today}')

logging.basicConfig(level=log_level, datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s.%(msecs)03dZ;'
                               '%(module)s.%(funcName)s;'
                               '  %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(f'{log_path}/{today}/{log_file_name}.log'), mode='w', encoding='utf-8', delay=False),
                        logging.StreamHandler(sys.stdout)
                    ])

##  IMAGENS  ##
integracao_bancaria = f'{image_path}/integracao_bancaria.PNG'
boleto = f'{image_path}/boleto.PNG'
button_ok = f'{image_path}/button_ok.PNG'
button_ok_2 = f'{image_path}/button_ok_2.PNG'
filter_clear = f'{image_path}/filter_clean.PNG'
lancamentos = f'{image_path}/lancamentos.PNG'
forma_pag = f'{image_path}/forma_pagamento.PNG'
boleto_min = f'{image_path}/Boleto_min.PNG'
boleto_min_des = f'{image_path}/boleto_min_desbili.PNG'
exec_sucesso = f'{image_path}/exec_success.PNG'
boleto_min_hab = f'{image_path}/boleto_min_habili.PNG'
table_empty_img = f'{image_path}/table_empty.PNG'
concessionarias_img = f'{image_path}/concessionarias.PNG'
codigo_barra_invalido = f'{image_path}/cod_barra_invalido.PNG'
licencas_excedidas = f'{image_path}/licencas_excedidas.PNG'
dados_bancarios = f'{image_path}/dados_bancarios_referencia.PNG'
dados_bancarios_2 = f'{image_path}/dados_bancarios_referencia_2.PNG'
bordero = f'{image_path}/bordero.PNG'


forma_pag_ted_cip = f'{image_path}/forma_pag_ted_cip.PNG'
filter_pix = f'{image_path}/filter_pix.PNG'
forma_pag_pix = f'{image_path}/forma_pag_pix.PNG'
error_salvar_pix = f'{image_path}/error_mudanca_pix.PNG'
error_salvar_pix_cancel = f'{image_path}/error_salvar_pix_cancel.PNG'
atualizacao_bordero_excecao = f'{image_path}/atualizacao_bordero_excecao_tratada.PNG'
error_generico = f'{image_path}/erro_mudanca_pix_21-03-2024.PNG'
licencas_2 = f'{image_path}/ERRO 2024_03_26 16_13.PNG'
troca_coligada = f'{image_path}/troca_coligada.PNG'
