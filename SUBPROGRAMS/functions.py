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
import shutil

def bot_text_art():
    logging.info("    ____   ")
    logging.info("   [____]    ")
    logging.info(" |=]()()[=|  ")
    logging.info("   _\==/__    _____    ____     _        _____    ___   _  __")
    logging.info(" |__|   |_|  |  _  \  / ___|   | |      |_   _| / ___| | |/ /")
    logging.info(" |_|_/\_|_|  | |  | | | |      | |        | |   | |    | ' / ")
    logging.info(" | | __ | |  | |  | | | |      | |        | |   | |    |  <  ")
    logging.info(" |_|[  ]|_|  | |__| | | |____  | |____   _| |_  | |__  | . \ ")
    logging.info(" \_|_||_|_/  |_____/   \_____| |______| |_____| \ ___| |_|\_\\")
    logging.info("   |_||_|                                                     ")
    logging.info("   | ||_|_   ")
    logging.info(" |___||___|  ")	
    logging.info("             ")

def encerrar_processo_windows(nome_processo):
    try:
        # Executar o comando taskkill para encerrar o processo pelo nome
        subprocess.run(['taskkill', '/f', '/im', nome_processo], check=True)
        print(f'Processo {nome_processo} encerrado forçosamente.')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao encerrar o processo {nome_processo}: {e}')


def show_exception_and_exit(exc_type, exc_value, tb):

    # https:/www.youtube.com/watch?v=8MjfalI4AO8
    # traceback.print_exception(exc_type, exc_value, tb)
    logging.error(exc_value, exc_info=(exc_type, exc_value, tb))

    result = datetime.now().strftime('%Y_%m_%d %H_%M')
    erro_print = f'ERRO {result}'

    screenshot = pyautogui.screenshot()
    screenshot.save(f"{print_path}\\{erro_print}.png")
    logging.debug(f'PRINT SALVO')

    #processo_inicio.terminate()
    encerrar_processo_windows(nome_processo)
    logging.debug(f'RM FECHADO')

    with open(f'{email_path}/emailError.html', 'r', encoding='utf-8') as fileError:
        templateError = fileError.read()
        htmlError = templateError.format(mensagem=exc_value)
        
    yag.send(to=email_receivers1.split(','), subject=f"ERRO - BOT REMESSAS BANCÁRIA",
    contents=htmlError,
    attachments=[f'{log_path}/{today}/{log_file_name}.log',f'{print_path}/{erro_print}.png'])
    logging.debug(f'EMAIL EXCEÇÃO ENVIADO')
    
    #logging.debug(f'ERRO - {exc_type} / {exc_value}')

    sys.exit(-1)

def open_RM():

    global processo_inicio
    # Substitua 'nome_do_programa' pelo nome ou caminho do programa que você deseja abrir
    programa = 'C:\Totvs\RM.NET\RM.exe'

    # Tente abrir o programa
    try:
        processo_inicio = subprocess.Popen(programa)
        logging.debug('OPEN PROGRAM RM')
    except FileNotFoundError:
        logging.debug('PROGRAM NOT FOUND')
    except Exception as e:
        logging.debug(f'ERROR WHEN OPENING PROGRAM RM {e}')

def loggin_RM():
    logging.debug('BUSCANDO LOGGIN RM')

    cc.wait_appear(locator.rm.pane_picturebox1, wait_timeout=900)

    user_rm = cc.wait_appear(locator.rm.user_field, wait_timeout=30)
    user_rm.double_click()
    user_rm.send_hotkey(f'{user}')
    logging.debug('ENTER USER_NAME')
    pass_rm = cc.wait_appear(locator.rm.pass_field, wait_timeout=30)
    pass_rm.click()
    time.sleep(3)
    pyautogui.typewrite(f'{password}')
    logging.debug('ENTER PASSWORD')
    click_button = cc.wait_appear(locator.rm.button_entrar, wait_timeout=30)
    click_button.click()
    logging.debug('ENTER RM')

    '''for i in range(3):
    #try:
        click_filter = cc.wait_appear(locator.rm.titlebar_titlebar4, wait_timeout=30)
        if click_filter is not None:
            click_filter.click()
            time.sleep(2)
            pyautogui.hotkey('esc')
        
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
        
            click_filter = cc.wait_appear(locator.rm.titlebar_titlebar3, wait_timeout=30)
            if click_filter is not None:
                click_filter.click()
                time.sleep(2)
                pyautogui.hotkey('esc')
            
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')

            break
        
        else:
            click_filter = cc.wait_appear(locator.rm.titlebar_titlebar3, wait_timeout=30)
            if click_filter is not None:
                click_filter.click()
                time.sleep(2)
                pyautogui.hotkey('esc')
            
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
            
                click_filter = cc.wait_appear(locator.rm.titlebar_titlebar4, wait_timeout=30)
                if click_filter is not None:
                    click_filter.click()
                    time.sleep(2)
                    pyautogui.hotkey('esc')
                
                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'w')

                break'''
    

def enter_coligada():

    click_context = cc.wait_appear(locator.rm.click_contexto, wait_timeout=300)
    click_context.click()
    logging.debug('CLICK CONTEXTO')
    click_alterar_contexto = cc.wait_appear(locator.rm.menuitem_alterar_contexto_do_módulo, wait_timeout=30)
    click_alterar_contexto.click()
    logging.debug('CLICK ALTERAR MODULO DO CONTEXTO')
    click_colig_cod = cc.wait_appear(locator.rm.edit_coligada_code, wait_timeout=60)
    click_colig_cod.click()
    click_colig_cod.set_text('1')
    logging.debug('INSERE O COLIGADA CODE = 1')
    pyautogui.press('tab')
    logging.debug('APERTA TAB PARA PREENCHER O CAMPO COM A STRING: OCEANICA ENGENHARIA E CONSULTORIA S.A.')
    click_avancar_final = cc.wait_appear(locator.rm.button_bavancar1, wait_timeout=15)
    click_avancar_final.click()
    logging.debug('CLICK AVANÇAR NOVAMENTE')
    click_concluir = cc.wait_appear(locator.rm.button_concluir, wait_timeout=15)
    click_concluir.click()
    logging.debug('CLICK CONCLUIR')

    troca = waitForImage(image = troca_coligada, timeout=20, name = 'TROCA COLIGADA')
    if troca is not None:
        logging.info('TROCA COLIGADA')
        pyautogui.click(troca)
        time.sleep(1)
        pyautogui.hotkey(f'enter')

    click_concluir = cc.wait_disappear(locator.rm.button_concluir, wait_timeout=120)
    logging.debug('POP UP COLIGADA DESAPARECER')

def check_movimentacao_bancaria():

    linha_totvs = cc.wait_appear(locator.rm.linha_rm, wait_timeout=120)
    linha_totvs.click()
    logging.debug('CLICK - TOTVS - LINHA RM')
    back_office = cc.wait_appear(locator.rm.back_office, wait_timeout=15)
    back_office.click()
    logging.debug('CLICK - BACK OFFICE')
    gestao_financeira = cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=15)
    gestao_financeira.click()
    logging.debug('CLICK - GESTAO FINANCEIRA')

    movimentacao_bancaria()
    processo_pagamento()

def enter_contas_a_pagar():

    linha_totvs = cc.wait_appear(locator.rm.linha_rm, wait_timeout=120)
    linha_totvs.click()
    logging.debug('CLICK - TOTVS - LINHA RM')
    back_office = cc.wait_appear(locator.rm.back_office, wait_timeout=30)
    back_office.click()
    logging.debug('CLICK - BACK OFFICE')
    gestao_financeira = cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=30)
    gestao_financeira.click()
    logging.debug('CLICK - GESTAO FINANCEIRA')

    contas_pagar = cc.wait_appear(locator.rm.contas_pagar, wait_timeout=120)
    contas_pagar.click()
    logging.debug('CLICK - CONTAS A PAGAR')

    cont = 0
    while cont <= 50:

        select_lancamentos = waitForImage(image = lancamentos, timeout=10, name = 'LANÇAMENTOS')
        if select_lancamentos is not None:
            time.sleep(2)
            pyautogui.click(select_lancamentos)
            logging.debug('CLICA EM LANÇAMENTOS')
            time.sleep(5)

        licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
        if licencas is not None:
            logging.debug('LICENCAS EXCEDIDAS')
            logging.debug(f'TENTANDO NOVAMENTE - {cont+1}')
            pyautogui.hotkey(f'esc')
            if cont == 50:
                logging.debug('ENVIANDO EMAIL DE ERRO')
                emailErro() 
                end_RM()
                sys.exit()
            cont += 1
            time.sleep(15)
        
        else:
            break




def data_filter():

    global inicio, fim

    inicio, fim = obter_intervalo_data()

    if inicio and fim:
        logging.debug(f"DATA INICIO {inicio.strftime('%d-%m-%Y')}")
        logging.debug(f"DATA FIM {fim.strftime('%d-%m-%Y')}")
    else:
        logging.debug('NÃO FOI PROGRAMADO PARA RODAR NO FINAL DE SEMANA')
        end_RM()

    dt_inicial_format = inicio.strftime("%d-%m-%Y")
    dt_final_format = fim.strftime("%d-%m-%Y")
    logging.debug('CLICK - SELECIONA A DATA DE QUARTA FEIRA E DA PROXIMA TERÇA')
    logging.debug(f'QUARTA-FEIRA: {dt_inicial_format}')
    logging.debug(f'TERCA-FEIRA: {dt_final_format}')
    #selecionando o filtro
    

    select_filter = cc.wait_appear(locator.rm.select_filter, wait_timeout=60)
    select_filter.click()
    time.sleep(2)
    filter_global = cc.wait_appear(locator.rm.group_filtros_globais, wait_timeout=60)
    filter_global.click()
    time.sleep(5)
    #filter_global.set_text('REMESSA BANCÁRIA')
    #pyautogui.write('REMESSA BANCÁRIA', interval=0.6)
    keyboard.write('REMESSA BANCÁRIA', delay=0.5)
    logging.debug('REMESSA BANCÁRIA - FILTRO DIGITADO')

    execute = cc.wait_appear(locator.rm.button_exec_filtro, wait_timeout=15)
    execute.click()
    logging.debug('CLICK - BOTAO DE SELECAO DE FILTRO')

    start_dt = cc.wait_appear(locator.rm.dt_inicial_filtro, wait_timeout=15)
    start_dt.double_click()
    time.sleep(2)
    start_dt.send_hotkey(f'{dt_inicial_format}')
    #start_dt.send_hotkey('06/11/2023')
    logging.debug(f'INSERE - DATA DE QUARTA-FEIRA: {dt_inicial_format}')

    end_dt = cc.wait_appear(locator.rm.dt_final_filtro, wait_timeout=15)
    end_dt.double_click()
    time.sleep(2)
    end_dt.send_hotkey(f'{dt_final_format}')
    #end_dt.send_hotkey('06/11/2023')
    logging.debug(f'INSERE - DATA DA PROX TERCA-FEIRA: {dt_final_format}')

    select_filter = cc.wait_appear(locator.rm.button_ok_filtro, wait_timeout=15)
    select_filter.click()
    logging.debug('CLICK - BOTAO DE EXECUTAR O FILTRO')
    time.sleep(5)

def filter_clean():

    for i in range (3):
        try:
            clear_filter_x = waitForImage(image = filter_clear, timeout=15, name = 'FILTER CLEAN')
            if clear_filter_x is not None:
                time.sleep(2)
                pyautogui.click(clear_filter_x)
                logging.debug('CLICA NO BOTÃO X DO LIMPA FILTRO')

        except:
            pass

def select_tipo_documento():

    time.sleep(10)

    tipo_doc = cc.wait_appear(locator.rm.header_tipo_de_documento, wait_timeout=600)
    colunm_name = tipo_doc.get_text()
    logging.debug(f'NOME DA COLUNA: {colunm_name}')
    
    tipo_doc_hover = cc.wait_appear(locator.rm.header_tipo_de_documento, wait_timeout=15)
    tipo_doc_hover.hover(4)
    logging.debug(f'HOVER NOME DA COLUNA: {colunm_name}')

    # BUSCANDO O FILTRO A PARTIR DA POSIÇÃO DO ELEMENTO
    posição = tipo_doc_hover.get_position()
    x, y = posição.Right - 5 , posição.Top + 5
    pyautogui.moveTo(x,y)
    pyautogui.click()

    pyautogui.press('down')

    pyautogui.typewrite('(Personalizar)')
    pyautogui.press('enter')
    logging.debug('CLICA NO FILTRO PERSONALIZAR')

    into_filter_personalizar = cc.wait_appear(locator.rm.listitem_filter_type, wait_timeout=15)
    into_filter_personalizar.click()
    logging.debug('CLICA PARA SELECIONAR OPÇÕES DO FILTRO')

    time.sleep(2)
    pyautogui.write('Não é igual a')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('Ctrl', 'a')
    pyautogui.write(F'{inv}')
    logging.debug('FILTRO "NÃO É IGUAL A INV" DEFINIDO')

    button_not_inv = cc.wait_appear(locator.rm.button_confirmar_not_inv, wait_timeout=15)
    button_not_inv.click()
    logging.debug('CLICK BUTTON CONFIRMAR FILTRO')

    time.sleep(5)


def desmark_filter():

    for i in range(3):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=150)
            check_lancamentos_receber.click()
            logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 3:
                check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=150)
                check_lancamentos_receber.click()
                logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')
            

    check_lancamentos_baixados = cc.wait_appear(locator.rm.checkbox_lançamentos_baixados, wait_timeout=15)
    check_lancamentos_baixados.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS BAIXADOS')

    check_lancamentos_cancelados = cc.wait_appear(locator.rm.checkbox_lançamentos_cancelados, wait_timeout=15)
    check_lancamentos_cancelados.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS CANCELADOS')

    check_lancamentos_faturados = cc.wait_appear(locator.rm.checkbox_lançamentos_faturados, wait_timeout=15)
    check_lancamentos_faturados.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS FATURADOS')

    filter_refresh = cc.wait_appear(locator.rm.button_atualiza_filtro, wait_timeout=15)
    filter_refresh.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS FATURADOS')

    time.sleep(5)

def filter_IPTE():

    logging.debug('VERIFICANDO O COD DO CLIENTE EM CADA REGISTRO')
    select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)

    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(100)
        logging.info('MOVIDO PRA CIMA 100 VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')

        select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)    
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')

    time.sleep(1)

    for i in range(150):
        time.sleep(0.01)
        pyautogui.hotkey('right')


    filter_IPTE = cc.wait_appear(locator.rm.header_linha_digitável_ipte, wait_timeout=15)
    filter_IPTE.hover(5)
    logging.debug('HOVER FILTER')


    posição = filter_IPTE.get_position()
    x, y = posição.Right - 5 , posição.Top + 5
    pyautogui.moveTo(x,y)
    pyautogui.click()

    logging.debug('CLICK FILTER')
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.typewrite('(Não brancos)')
    time.sleep(1)
    pyautogui.press('enter')
    logging.debug('CLICA NO FILTRO PERSONALIZAR')
    time.sleep(5)

    caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)

    if caixa_selecao is not None:
        logging.debug('TABELA CONTÉM REGISTROS')
        pass

    else:

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(100)
        logging.info('MOVIDO PRA CIMA 100 VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        if caixa_selecao is None:
            cc.mouse.scroll(100)
            logging.info('MOVIDO PRA CIMA MAIS 100 VEZES')
            caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
            if caixa_selecao is None:
                logging.debug('TABELA NÃO CONTÉM REGISTROS')
                return


    caixa_selecao.click()
    time.sleep(1)
    caixa_selecao.click()

    time.sleep(1)
    pyautogui.hotkey('right')


def check_table_record():

    global rows_int
    rows_int = 0

    logging.debug('VERIFICANDO SE A TABELA ESTÁ VAZIA')

    texto = cc.wait_appear(locator.rm.button_12, wait_timeout=120)
    txt_extraido = texto.get_text()
    logging.debug(f'Texto extraido{txt_extraido}')
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.debug(f'Count {count}')
    logging.debug(f'Type {type(count)}')
    rows_int = count

    if rows_int == 0:
        logging.debug('SEM REGISTROS')
        time.sleep(2)
        return True
 
    else:
        logging.debug('TABELA CONTÉM REGISTROS')
        return False

        

    '''time.sleep(5)
    pyautogui.hotkey('Ctrl', 'g')
    time.sleep(2)

    numero_registros = cc.wait_appear(locator.rm.text_para_este_processo_é_necessário_que_existam_registros, wait_timeout=15)
    txt_table = numero_registros.get_text()
    logging.debug(f'{txt_table}')
    time.sleep(2)
    

    if txt_table == 'Para este processo é necessário que existam registros na visão.':
        time.sleep(2)
        logging.debug('SEM REMESSAS BANCARIA')
        rm_nao = cc.wait_appear(locator.rm.titlebar_titlebar_rm, wait_timeout=15)
        rm_nao.click()
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)
        return True
    else:
        number_rows = re.findall(r'\b(\d+)\b', txt_table)
        logging.debug(f'TIPO: {type(number_rows)}')
        rows_int = int(number_rows[0])
        logging.debug(f'NUMERO DE TUPLAS: {rows_int}')
        logging.debug('TABELA CONTÉM REGISTROS')      
        click_nao = cc.wait_appear(locator.rm.button_não, wait_timeout=15)
        click_nao.set_focus()
        time.sleep(3)
        pyautogui.hotkey('alt', 'n')
        logging.debug('CLICK NÃO')
        time.sleep(5)
        return False '''
    

def check_payment_type():
    global lista_ref_data


    logging.debug('VERIFICANDO O COD DO CLIENTE EM CADA REGISTRO')
    select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)

    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(rows_int)
        logging.info(f'MOVIDO PRA CIMA {rows_int} VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')

        select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)    
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')

    count_reg = 0
    lista_ref_data= []
    for i in range(rows_int):

        count_reg += 1

        logging.debug(f'CONTAGEM: {count_reg}')

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

        pyautogui.hotkey('ctrl', 'enter')
        logging.debug('ENTRANDO NO REGISTRO')
        time.sleep(4)

        select_integracao_bancaria = waitForImage(image = integracao_bancaria, timeout=60, name = 'INTEGRAÇÃO BANCÁRIA')
        if select_integracao_bancaria is not None:
            time.sleep(2)
            pyautogui.click(select_integracao_bancaria)
            logging.debug('CLICA EM INTEGRAÇÃO BANCÁRIA')

        logging.debug('VERIFICANDO INFORMAÇÕES')

        time.sleep(3)
        
        dados_banc = waitForImage(image = dados_bancarios, timeout=20, name = 'DADOS BANCARIOS')
        if dados_banc is not None:
            x, y = dados_banc.left - 130 , dados_banc.top + dados_banc.height // 2 
            pyautogui.click(x, y)
            logging.debug('DADOS BANCARIOS')

        else: 
            dados_banc2 = waitForImage(image = dados_bancarios_2, timeout=20, name = 'DADOS BANCARIOS 2')
            if dados_banc2 is not None:
                x, y = dados_banc2.left - 130 , dados_banc2.top + dados_banc2.height // 2 
                pyautogui.click(x, y)
                logging.debug('CLICK EM INTEGRAÇÃO BANCÁRIA')

        time.sleep(10)

        logging.debug('ENTROU DADOS BANCÁRIOS')

        pyautogui.press('tab')
        logging.debug('APERTA TAB')
        time.sleep(2)
        pyautogui.write('BOLETO')
        logging.debug('ESCREVE BOLETO')

        '''payment_form = waitForImage(image = forma_pag, timeout=15, name = 'FORMA DE PAGAMENTO')
        if payment_form is not None:
            time.sleep(2)
            logging.debug('FORMA DE PAGAMENTO: TITULO DE COBRANÇA (BOLETO)')
            time.sleep(2)
        else:
            logging.debug('FORMA DE PAGAMENTO NÃO É BOLETO')
            
            for i in range(4):
                time.sleep(0.3)
                pyautogui.press('tab')

            for i in range(21):
                time.sleep(0.3)
                pyautogui.press('down')

            for i in range(17):
                time.sleep(0.3)
                pyautogui.press('up')'''

        
        click_ok()
        time.sleep(2)
        click_ok()

        pyautogui.hotkey('ctrl', 'space')
        logging.debug(f'INCLUIDOS: {ref_atual_string} REFERENCIAS NO PROCESSAMENTO')

        if count_reg == 150 or count_reg == rows_int: ###
        #if count_reg == 5 or count_reg == rows_int:
            logging.debug(f'FORAM INCLUIDOS: {count_reg} REFERENCIAS NO PROCESSAMENTO')
            break
        
        time.sleep(2)
        pyautogui.press('down')
        logging.debug('PASSANDO PARA PRÓXIMO REGISTRO')
        time.sleep(2)

        '''
        windows = gw.getWindowsWithTitle(title='TOTVS Linha RM - Construção e Projetos  Alias: CorporeRM | 1-OCEANICA ENGENHARIA E CONSULTORIA S.A.')
        print(windows)
        if windows:
            window=windows[0]
            window.activate()
            window.maximize()
        '''


def process_lancamentos():

    if len(ref_out) == rows_int:
        logging.debug('TODOS OS REGISTROS FORAM DESMARCADOS, LIMPA O VETOR REF_OUT')
        ref_out.clear()
        return True

    time.sleep(2)
    pyautogui.hotkey('Ctrl', 'g')
    time.sleep(2)

    click_combo = cc.wait_appear(locator.rm.combobox_lancamento, wait_timeout=120)
    click_combo.click()
    logging.debug('CLICA PARA APARECER CONTA/CAIXA')

    select_conta_caixa = cc.wait_appear(locator.rm.listitem_contacaixa, wait_timeout=15)
    select_conta_caixa.click()
    logging.debug('SELECIONA CONTA/CAIXA')
    
    select_conta_caixa = cc.wait_appear(locator.rm.button_contavalor, wait_timeout=15)
    select_conta_caixa.click()
    logging.debug('CLICA NO BOTÃO [...]')

    select_caixa_selecao = cc.wait_appear(locator.rm.combobox_cbxsearch, wait_timeout=15) #### INICIO ADIÇÃO
    select_caixa_selecao.click()
    logging.debug('CLICA NA CAIXA DE SELEÇÃO')

    select_codigo = cc.wait_appear(locator.rm.listitem_código, wait_timeout=15)
    select_codigo.click()
    logging.debug('CLICA EM CODIGO')

    time.sleep(3)
    pyautogui.hotkey('tab')
    time.sleep(2)

    #pyautogui.write('%3212') 
    keyboard.write('13001867-9') #### FIM ADIÇÃO
    logging.debug('CLICA NO CAMPO PESQUISA E DIGITA: %3212')

    filter_search = cc.wait_appear(locator.rm.button_btnfilter, wait_timeout=15)
    filter_search.click()
    logging.debug('CLICA NO BOTÃO DO FILTRO')

    btn_ok_contacaixa = cc.wait_appear(locator.rm.button_ok_contacaixa, wait_timeout=15)
    btn_ok_contacaixa.click()
    logging.debug('CLICA NO BOTÃO OK')

    btn_executar = cc.wait_appear(locator.rm.button_executar, wait_timeout=15)
    btn_executar.click()
    logging.debug('CLICA NO BOTÃO EXECUTAR')

    cc.wait_appear(locator.rm.button_exec_fechar, wait_timeout=1200)

    exec_success_process = waitForImage(image = exec_sucesso, timeout=15, name = 'PRESS BUTTON OK')
    if exec_success_process is not None:
        time.sleep(2)
        logging.debug('O PROCESSAMENTO FOI EXECUTADO COM SUCESSO.')
        time.sleep(2)
        txt_log_erro = cc.wait_appear(locator.rm.edit_textboxmsg, wait_timeout=60)
        txt_log_erro.click()
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        txt_log = pyperclip.paste()
        logging.debug(f'LOG: {txt_log}')
        btn_exec_fechar = cc.wait_appear(locator.rm.button_exec_fechar, wait_timeout=15)
        btn_exec_fechar.click()
        logging.debug('CLICK EM FECHAR.')
        #time.sleep(120)
        time.sleep(20)
        proccess_bordero()
    else:
        logging.debug('LANÇAMENTO COM ERRO')
        time.sleep(2)
        txt_log_erro = cc.wait_appear(locator.rm.edit_textboxmsg, wait_timeout=60)
        txt_log_erro.click()
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        txt_log = pyperclip.paste()
        logging.debug(f'ERRO: {txt_log}')

        # Padrão de expressão regular para encontrar números de referência
        padrao = r'1-(\d+):'
        # Encontrar todas as correspondências usando a expressão regular
        correspondencias = re.findall(padrao, txt_log)
        logging.debug(f'CORRESPONDENCIA {correspondencias}')
        num_de_ref = []
        # Converte os números de referência para inteiros e os adiciona a um vetor
        num_de_ref = [numero for numero in correspondencias]
        logging.debug(f'NUMERO DE REFERENCIAS QUE SERÃO TIRADOS DA REMESSA {num_de_ref}')
        #emailErro() 
        btn_exec_fechar = cc.wait_appear(locator.rm.button_exec_fechar, wait_timeout=15)
        btn_exec_fechar.click()
        logging.debug('CLICK EM FECHAR.')

        #Ancora para tabela voltar a aparecer
        cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=1200)

        if len(num_de_ref) == rows_int:
            logging.debug('NUMERO DE REFERENCIAS QUE SERAO TIRADOS IGUAL AO NUMERO DE REGISTROS')
            logging.debug('PASSAR PARA O PRÓXIMO LANCAMENTO')

        else:
            logging.debug('NUMERO DE REFERENCIAS QUE SERAO TIRADOS DIFERENTE DO NUMERO DE REGISTROS')
            remove_send(num_de_ref)
            process_lancamentos()
            logging.debug('PASSAR PARA MOVIMENTAÇÃO BANCÁRIA')
            
    return True


def remove_send(num_de_ref):

    #cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=600)

    for i in range(3):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=150)
            #check_lancamentos_receber.click()
            logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 3:
                check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=150)
                #check_lancamentos_receber.click()
                logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')

    time.sleep(5)

    for i in range (rows_int):
        pyautogui.press('up')

    time.sleep(5)

    select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=100)
    
    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(rows_int)
        logging.info(f'MOVIDO PRA CIMA {rows_int} VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')

        select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)    
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    
    count_register = 0

    for i in range (rows_int):

        time.sleep(5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        ref_num_atual = pyperclip.paste()
        logging.debug(f'ref_num_atual: {ref_num_atual}')
        logging.debug(f'num_de_ref: {num_de_ref}')
        time.sleep(2)
        

        if ref_num_atual in num_de_ref:
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'space')
            logging.debug(f'Retirando a referencia: {ref_num_atual}')
            ref_out.append(ref_num_atual)
            count_register += 1
            if count_register == len(num_de_ref):
                logging.debug(f'SAINDO DO REMOVE_SEND E LIMPANDO O VETOR num_de_ref')
                break
        
        time.sleep(5)
        pyautogui.press('down')

def proccess_bordero():

    cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=1200)

    time.sleep(5)
    pyautogui.hotkey('Ctrl', 'p')
    logging.debug('ctrl+p')
    time.sleep(2)
    pyautogui.press('down')
    logging.debug('down')
    time.sleep(2)
    pyautogui.press('down')
    logging.debug('down')
    time.sleep(2)
    pyautogui.press('right')
    logging.debug('right')
    time.sleep(2)
    pyautogui.press('enter')
    logging.debug('enter')
    time.sleep(2)
    logging.debug('SELECIONAR INCLUSÃO DE BORDERO')

    atualizacao_bordero = waitForImage(image = atualizacao_bordero_excecao, timeout=20, name = 'PRESS BUTON SIM')
    if atualizacao_bordero is not None:
        pyautogui.click(atualizacao_bordero)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
    
    mark_register = cc.wait_appear(locator.rm.text_para_este_processo_é_necessário_que_existam_registros, wait_timeout=60)
    if mark_register is not None:
        logging.debug('NECESSITA DE REGISTROS MARCADO.')
        time.sleep(2)
        pyautogui.press('enter')
    
    else:
        '''menuitem_inclusao_bordero = cc.wait_appear(locator.rm.button_bordero_inclusao_trespontos, wait_timeout=60) ### RETIRADO INICIO
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
        time.sleep(2)''' ### RETIRADO FIM

        exec_bordero = cc.wait_appear(locator.rm.button_exec_bordero, wait_timeout=60)
        exec_bordero.click()
        logging.debug('CLICA EM EXECUTAR NA INCLUSÃO DO BORDÊRO')

        cc.wait_appear(locator.rm.button_bordero_fechar, wait_timeout=600)

        exec_success_process = waitForImage(image = exec_sucesso, timeout=5, name = 'PRESS BUTTON OK')
        if exec_success_process is not None:
            time.sleep(2)
            logging.debug('O PROCESSAMENTO DO BORDERO FOI EXECUTADO COM SUCESSO.')
            time.sleep(2)
            log_bordero = cc.wait_appear(locator.rm.edit_log_bordero, wait_timeout=15)
            txt_log_bordero = log_bordero.get_text()
            logging.debug('COPIA O LOG DO PROCESSAMENTO DO BORDERO')
            logging.debug(f'{txt_log_bordero}')
            time.sleep(2)
            btn_exec_fechar = cc.wait_appear(locator.rm.button_bordero_fechar, wait_timeout=15)
            btn_exec_fechar.click()
            logging.debug('CLICK EM FECHAR.')
            time.sleep(2)
        else:
            logging.debug('O PROCESSAMENTO DO BORDERO FOI EXECUTADO COM ERRO.')
            message_erro = cc.wait_appear(locator.rm.edit_textboxlog, wait_timeout=15)
            message_erro.click()
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(2)
            txt_log = pyperclip.paste()
            logging.debug(f'ERRO: {txt_log}')
            btn_exec_fechar = cc.wait_appear(locator.rm.button_bordero_fechar, wait_timeout=15)
            btn_exec_fechar.click()
            logging.debug('CLICK EM FECHAR.')
            texto_msg = (f'ERRO EM INCLUSÃO DE BORDERO. \n LOG:\n {txt_log}')
            emailErro(texto_msg)

            # Padrão de expressão regular para encontrar números de referência
            padrao = r'1-(\d+)'
            # Encontrar todas as correspondências usando a expressão regular
            correspondencias = re.findall(padrao, txt_log)
            logging.debug(f'CORRESPONDENCIA {correspondencias}')
            # Converte os números de referência para inteiros e os adiciona a um vetor
            num_de_ref = []
            num_de_ref = [numero for numero in correspondencias]
            
            if num_de_ref != []:
                logging.debug(f'NUMERO DE REFERENCIAS QUE SERÃO TIRADOS DA REMESSA {num_de_ref}')
                logging.debug(f'CHAMANDO A FUNÇÃO REMOVE_SEND')
                remove_send(num_de_ref)
                proccess_bordero()

            else:
                texto_msg = txt_log
                emailErro(texto_msg)

            


def select_all_func():

    time.sleep(2)
    select_all = cc.wait_appear(locator.rm.header_x, wait_timeout=60)
    select_all.click()
    logging.debug('SELECIONA TODOS OS REGISTROS')

def movimentacao_bancaria():

    '''movi_bancaria = cc.wait_appear(locator.rm.tabitem_movimentacoes_bancarias, wait_timeout=600)
    movi_bancaria.click()
    logging.debug('CLICA NA ABA MOVIMENTAÇÃO BANCARIA')'''

    for i in range(3):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            movi_bancaria = cc.wait_appear(locator.rm.tabitem_movimentacoes_bancarias, wait_timeout=150)
            movi_bancaria.click()
            logging.debug('CLICA NA ABA MOVIMENTAÇÃO BANCARIA')
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 7:
                movi_bancaria = cc.wait_appear(locator.rm.tabitem_movimentacoes_bancarias, wait_timeout=150)
                movi_bancaria.click()
                logging.debug('CLICA NA ABA MOVIMENTAÇÃO BANCARIA')

    for i in range (3):

        cont = 0

        while cont <= 30:

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
                if cont == 30:
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
    logging.debug('SELECIONA O FILTRO HOJE')

    time.sleep(5)

    filter_clean()

    select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_row0, wait_timeout=15)
    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA MOVIMENTAÇÃO BANCÁRIA') 

    else:
        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(200)

    select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_row0, wait_timeout=15)
    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA MOVIMENTAÇÃO BANCÁRIA')   

        for i in range(12):
            pyautogui.hotkey('right')
        logging.debug('12 PASSOS PARA DIREITA NA TABELA >>')

        filter_status_remessa = cc.wait_appear(locator.rm.header_status_da_remessa_pagamento, wait_timeout=15)
        filter_status_remessa.hover(5)
        logging.debug('HOVER FILTER')

        # BUSCANDO O FILTRO A PARTIR DA POSIÇÃO DO ELEMENTO
        posição = filter_status_remessa.get_position()
        x, y = posição.Right - 5 , posição.Top + 5
        pyautogui.moveTo(x,y)
        pyautogui.click()

        logging.debug('CLICK FILTER')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.typewrite('(Personalizar)')
        time.sleep(1)
        pyautogui.press('enter')
        logging.debug('CLICA NO FILTRO  STATUS DA REMESSA')
        time.sleep(2)
        pyautogui.press('tab')
        logging.debug('APERTA TAB PARA ESCREVER O FILTRO')
        time.sleep(2)
        pyautogui.write('Pendente')
        logging.debug('ESCREVE PENDENTE NO FILTRO')
        time.sleep(2)
        pyautogui.press('enter')
        logging.debug('APERTA ENTER PARA SELECIONAR OS PENDENTES')
        time.sleep(5)

        select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
        if select_first_row is not None:
            select_all = cc.wait_appear(locator.rm.header_x_bordero, wait_timeout=30)
            select_all.click()
            logging.debug('SELECIONA TODAS AS TUPLAS COM STATUS PENDENTE')

            time.sleep(2)
            pyautogui.hotkey('Ctrl', 'p')
            logging.debug('CLICA EM PROCESSOS')
            time.sleep(2)
            pyautogui.hotkey('down')
            logging.debug('APERTA PARA BAIXO')
            time.sleep(2)
            pyautogui.hotkey('ENTER')
            logging.debug('APERTA ENTER')
            time.sleep(2)

            exec_bordero_autorizacao = cc.wait_appear(locator.rm.button_exec_autorizacao, wait_timeout=60)
            exec_bordero_autorizacao.click()
            logging.debug('CLICK EM EXECUTAR BORDERO DE PAGAMENTO')

            cc.wait_appear(locator.rm.button_fechar_bordero, wait_timeout=600)

            exec_success_process = waitForImage(image = exec_sucesso, timeout=15, name = 'PRESS BUTTON OK')
            if exec_success_process is not None:
                logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM SUCESSO.')
            else:
                logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM ERRO FAVOR VERIFICAR.')
            
            btn_exec_fechar = cc.wait_appear(locator.rm.button_fechar_bordero, wait_timeout=60)
            btn_exec_fechar.click()
            logging.debug('CLICK EM FECHAR.')

        else:
            logging.debug('SEM PROCESSAMENTO DE BORDERO PENDENTE')

    else:
        logging.debug('SEM PROCESSAMENTO DE BORDERO')


def processo_pagamento():

    time.sleep(10)

    filter_clean()

    select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA MOVIMENTAÇÃO BANCÁRIA')

        filter_status_remessa = cc.wait_appear(locator.rm.header_status_da_remessa_pagamento, wait_timeout=300)
        filter_status_remessa.hover(5)
        logging.debug('HOVER FILTER')

        # BUSCANDO O FILTRO A PARTIR DA POSIÇÃO DO ELEMENTO
        posição = filter_status_remessa.get_position()
        x, y = posição.Right - 5 , posição.Top + 5
        pyautogui.moveTo(x,y)
        pyautogui.click()

        logging.debug('CLICK FILTER')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.typewrite('(Personalizar)')
        time.sleep(1)
        pyautogui.press('enter')
        logging.debug('CLICA NO FILTRO  STATUS DA REMESSA')
        time.sleep(2)
        pyautogui.press('tab')
        logging.debug('APERTA TAB PARA ESCREVER O FILTRO')
        time.sleep(2)
        pyautogui.write('Autorizado')
        logging.debug('ESCREVE AUTORIZADO NO FILTRO')
        time.sleep(2)
        pyautogui.press('enter')
        logging.debug('APERTA ENTER PARA SELECIONAR OS AUTORIZADOS')
        time.sleep(5)

        select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
        if select_first_row is not None:

            for i in range(6):
                pyautogui.hotkey('left')
            logging.debug('6 PASSOS PARA ESQUERDA NA TABELA <<')

            for i in range(10):
                pyautogui.hotkey('up')
            logging.debug('10 PASSOS PARA cima NA TABELA <<')

            check_user_bot()
        else:
            logging.debug('SEM REMESSA DE BORDERO AUTORIZADO')
    
    else:
        select_first_row2 = cc.wait_appear(locator.rm.dataitem_coligada_row0, wait_timeout=15)
        if select_first_row2 is not None:
            select_first_row2.click()

            for i in range(12):
                pyautogui.hotkey('right')
            logging.debug('12 PASSOS PARA ESQUERDA NA TABELA >>')

            filter_status_remessa = cc.wait_appear(locator.rm.header_status_da_remessa_pagamento, wait_timeout=300)
            filter_status_remessa.hover(5)
            logging.debug('HOVER FILTER')

            # BUSCANDO O FILTRO A PARTIR DA POSIÇÃO DO ELEMENTO
            posição = filter_status_remessa.get_position()
            x, y = posição.Right - 5 , posição.Top + 5
            pyautogui.moveTo(x,y)
            pyautogui.click()

            logging.debug('CLICK FILTER')
            time.sleep(2)
            pyautogui.press('down')
            time.sleep(1)
            pyautogui.typewrite('(Personalizar)')
            time.sleep(1)
            pyautogui.press('enter')
            logging.debug('CLICA NO FILTRO  STATUS DA REMESSA')
            time.sleep(2)
            pyautogui.press('tab')
            logging.debug('APERTA TAB PARA ESCREVER O FILTRO')
            time.sleep(2)
            pyautogui.write('Autorizado')
            logging.debug('ESCREVE AUTORIZADO NO FILTRO')
            time.sleep(2)
            pyautogui.press('enter')
            logging.debug('APERTA ENTER PARA SELECIONAR OS AUTORIZADOS')
            time.sleep(5)

            select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
            if select_first_row is not None:

                for i in range(6):
                    pyautogui.hotkey('left')
                logging.debug('6 PASSOS PARA ESQUERDA NA TABELA <<')

                check_user_bot()
            else:
                logging.debug('SEM REMESSA DE BORDERO AUTORIZADO')

        else:
            logging.debug('SEM REMESSA DE BORDERO AUTORIZADO')
    
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    logging.debug('FECHA ABA MOVIMENTAÇÕES BANCÁRIAS')

       



def check_user_bot():

    texto = cc.wait_appear(locator.rm.button_1102, wait_timeout=15)
    txt_extraido = texto.get_text()
    logging.debug(f'Texto extraido{txt_extraido}')
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.debug(f'Count {count}')
    logging.debug(f'Type {type(count)}')

    for processo in range(count):

        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        logging.debug('CHECK USER BOT 1')

        time.sleep(2)
        usuario = pyperclip.paste()
        logging.debug(f'{usuario}')

        if usuario == 'dclick':

            time.sleep(2)

            for i in range(7):
                pyautogui.hotkey('right')
            logging.debug('7 PASSOS PARA DIREITA NA TABELA >>')

            time.sleep(2)
            pyautogui.hotkey('ctrl', 'c')

            time.sleep(2)
            bot = pyperclip.paste()
            logging.debug(f'{bot}')

            # Usando expressão regular para encontrar o nome SISPAG
            #padrao = r'\bSISPAG\b' ###
            padrao = r'\b033\b'
            match = re.search(padrao, bot)

            if match:
                #logging.debug("NOME SISPAG ENCONTRADO") ###
                logging.debug("033 ENCONTRADO")
                pyautogui.hotkey('ctrl', 'space')
                time.sleep(2)
                pyautogui.hotkey('Ctrl', 'p')
                logging.debug('CLICA EM PROCESSOS')
                time.sleep(2)

                pyautogui.press('down')
                logging.debug('APERTA PARA BAIXO 1')
                time.sleep(2)

                pyautogui.press('down')
                logging.debug('APERTA PARA BAIXO 2')
                time.sleep(2)

                pyautogui.press('down')
                logging.debug('APERTA PARA BAIXO 3')
                time.sleep(2)

                pyautogui.press('ENTER')
                logging.debug('APERTA ENTER')
                time.sleep(2)

                remessas_avancar = cc.wait_appear(locator.rm.button_processo_avancar, wait_timeout=15)
                remessas_avancar.click()
                logging.debug('CLICA EM REMESSAS DE PAGAMENTO')

                time.sleep(2)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
                #pyautogui.write('341')
                pyautogui.write('033') ####
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)

                remessas_avancar2 = cc.wait_appear(locator.rm.button_remssas_avancar_2, wait_timeout=15)
                remessas_avancar2.click()
                logging.debug('CLICA EM AVANÇAR')

                desmark_salvar_arq = cc.wait_appear(locator.rm.checkbox_desmarcar, wait_timeout=15)
                desmark_salvar_arq.click()
                logging.debug('DESMARCA CHECKBOX PARA SALVAR ARQUIVO DE REMESSA')    

                avancar_3 = cc.wait_appear(locator.rm.button_remessas_avancar_3, wait_timeout=15)
                avancar_3.click()
                logging.debug('CLICA EM AVANCAR PARA CONCLUIR')

                execute_processo_pagamento = cc.wait_appear(locator.rm.button_exec_processo_pag, wait_timeout=15)
                execute_processo_pagamento.double_click()
                logging.debug('CLICA EM EXECUTAR')

                exec_success_process = waitForImage(image = exec_sucesso, timeout=300, name = 'PRESS BUTTON OK')
                if exec_success_process is not None:
                    time.sleep(2)
                    logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM SUCESSO.')
                    time.sleep(2)
                    processo_pagamento = cc.wait_appear(locator.rm.edit_textboxlog_autorizado_bordero, wait_timeout=15)
                    processo_log = processo_pagamento.get_text()
                    processo_pagamento.set_focus()
                    logging.debug(f'{processo_log}')
                    time.sleep(2)
                    pyautogui.hotkey('tab')
                    time.sleep(2)
                    pyautogui.hotkey('enter')
                    time.sleep(2)
                    logging.debug('ENTER EM FECHAR.')
                    time.sleep(2)
                    rename_arq()
                
                else:
                    time.sleep(2)
                    logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM ERRO.')
                    time.sleep(2)
                    logging.debug('CLICA EM EXECUTAR')
                    for i in range(7):
                        pyautogui.hotkey('tab')
                        time.sleep(0.5)
                    logging.debug('7 TABs ATE SELECIONAR FECHAR')

                    pyautogui.hotkey('enter')
                    logging.debug('ENTER EM FECHAR.')
                    texto_msg = 'O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM ERRO.'
                    emailErro(texto_msg)

                break

            else:
                #logging.debug("Nome SISPAG não encontrado na string.")
                logging.debug("033 não encontrado na string.") ####
                for i in range(7):
                    pyautogui.hotkey('left')
                logging.debug('7 PASSOS PARA ESQUERDA NA TABELA <<')
                pyautogui.press('down')
                logging.debug(f'COUNT1: {processo}')


        else:
            logging.debug('O USUÁRIO NÃO É INTEGRAÇÃO PARA ESSA REMESSA PARA PARA DE BAIXO')
            pyautogui.press('down')
            logging.debug(f'COUNT1: {processo}')

    if processo == count:
        #logging.debug('NÃO FOI ENCONTRADO O USUÁRIO INTEGRAÇÃO E O NOME DO ARQUIVO SISPAG')
        logging.debug('NÃO FOI ENCONTRADO O USUÁRIO INTEGRAÇÃO E O NOME DO ARQUIVO 033')


def filter_forma_pagamento():

    row_select = cc.wait_appear(locator.rm.dataitem_imagem_natureza_row0, wait_timeout=60)
    if row_select is not None:
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
        row_select.click()
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        cc.mouse.scroll(100)
        logging.info('MOVIDO PRA CIMA 100 VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        if caixa_selecao is not None:
            caixa_selecao.click()
            time.sleep(1)
            caixa_selecao.click()
            time.sleep(1)
            pyautogui.hotkey('right')

            select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)    
            select_first_row.click()
            logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
        else:
            return
    
    logging.debug('CLICK NA PRIMEIRA LINHA E COLUNA DA TABELA')
    #162
    #for i in range(13):
    for i in range(160):
        pyautogui.hotkey('right')
    logging.debug('160 PASSOS PARA DIREITA NA TABELA >>')

    '''for i in range(6):
        pyautogui.hotkey('left')
    logging.debug('6 PASSOS PARA ESQUERDA NA TABELA >>')'''
    
    forma_pag_hover = cc.wait_appear(locator.rm.header_forma_de_pagamento_eletrônica, wait_timeout=15)
    forma_pag_hover.hover(4)
    logging.debug(f'HOVER NOME DA COLUNA FORMA DE PAGAMENTO')
        
    posição = forma_pag_hover.get_position()
    x, y = posição.Right - 5 , posição.Top + 5
    pyautogui.moveTo(x,y)
    pyautogui.click()

    logging.debug('CLICA PARA APARECER O FILTRO PERSONALIZAR')

    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)

    pyautogui.typewrite('(Personalizar)')
    time.sleep(1)
    pyautogui.press('enter')
    logging.debug('CLICA NO FILTRO PERSONALIZAR')

    time.sleep(1)
    pyautogui.typewrite('Igual a')

    time.sleep(1)
    pyautogui.press('tab')

    time.sleep(1)
    pyautogui.typewrite('TED CIP')

    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

    texto = cc.wait_appear(locator.rm.button_12, wait_timeout=120)
    txt_extraido = texto.get_text()
    logging.debug(f'Texto extraido{txt_extraido}')
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.debug(f'Count {count}')
    logging.debug(f'Type {type(count)}')
    rows_int = count

    if rows_int == 0:
        logging.debug('SEM REGISTROS')
        time.sleep(2)
 
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(rows_int)
        logging.info(f'MOVIDO PRA CIMA {rows_int} VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')


    '''time.sleep(2)
    pyautogui.hotkey('Ctrl', 'g')
    time.sleep(1)

    numero_registros = cc.wait_appear(locator.rm.text_para_este_processo_é_necessário_que_existam_registros, wait_timeout=15)
    txt_table = numero_registros.get_text()
    logging.debug(f'{txt_table}')
    time.sleep(2)

    if txt_table == 'Para este processo é necessário que existam registros na visão.':
        time.sleep(2)
        logging.debug('SEM REMESSAS BANCARIA')
        time.sleep(2)
        rm_nao = cc.wait_appear(locator.rm.titlebar_titlebar_rm, wait_timeout=15)
        rm_nao.click()
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

    else:
        time.sleep(3)
        logging.debug('TABELA CONTÉM REGISTROS')      
        click_nao = cc.wait_appear(locator.rm.button_não, wait_timeout=15)
        click_nao.set_focus()
        time.sleep(3)
        pyautogui.hotkey('alt', 'n')
        logging.debug('CLICK NÃO')
        time.sleep(5)

        number_rows = re.findall(r'\b(\d+)\b', txt_table)
        logging.debug(f'TIPO: {type(number_rows)}')
        rows_int = int(number_rows[0])
        logging.debug(f'NUMERO DE TUPLAS: {rows_int}')

        click_up = cc.wait_appear(locator.rm.button_uma_linha_para_cima, wait_timeout=15)

        for i in range (rows_int):
            click_up.click()

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')'''
    

def filter_forma_pagamento_branco():

    largura_tela, altura_tela = pyautogui.size()
    meio_x = largura_tela // 2
    meio_y = altura_tela // 2

    pyautogui.moveTo(meio_x, meio_y)
    time.sleep(1)
    cc.mouse.scroll(10)
    logging.info('MOVIDO PRA CIMA 10 VEZES')

    row_select = cc.wait_appear(locator.rm.dataitem_imagem_natureza_row0, wait_timeout=15)
    row_select.click()
    logging.debug('CLICK NA PRIMEIRA LINHA E COLUNA DA TABELA')
    #162
    
    #for i in range(13):
    for i in range(160):
        pyautogui.hotkey('right')
    logging.debug('160 PASSOS PARA DIREITA NA TABELA >>')
    
    forma_pag_hover = cc.wait_appear(locator.rm.header_forma_de_pagamento_eletrônica, wait_timeout=15)
    forma_pag_hover.hover(4)
    logging.debug(f'HOVER NOME DA COLUNA FORMA DE PAGAMENTO')

    posição = forma_pag_hover.get_position()
    x, y = posição.Right - 5 , posição.Top + 5
    pyautogui.moveTo(x,y)
    pyautogui.click()

    logging.debug('CLICA PARA APARECER O FILTRO PERSONALIZAR')

    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)

    pyautogui.typewrite('(Personalizar)')
    time.sleep(1)
    pyautogui.press('enter')
    logging.debug('CLICA NO FILTRO PERSONALIZAR')

    time.sleep(1)
    pyautogui.typewrite('Igual a')

    time.sleep(1)
    pyautogui.press('tab')

    time.sleep(1)
    pyautogui.press('space')

    time.sleep(1)
    pyautogui.press('backspace')

    time.sleep(1)
    pyautogui.press('enter')

    texto = cc.wait_appear(locator.rm.button_12, wait_timeout=120)
    txt_extraido = texto.get_text()
    logging.debug(f'Texto extraido{txt_extraido}')
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.debug(f'Count {count}')
    logging.debug(f'Type {type(count)}')
    rows_int = count

    if rows_int == 0:
        logging.debug('SEM REGISTROS')
        time.sleep(2)
 
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(rows_int)
        logging.info(f'MOVIDO PRA CIMA {rows_int} VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')

    '''time.sleep(5)
    pyautogui.hotkey('Ctrl', 'g')
    time.sleep(1)

    numero_registros = cc.wait_appear(locator.rm.text_para_este_processo_é_necessário_que_existam_registros, wait_timeout=15)
    txt_table = numero_registros.get_text()
    logging.debug(f'{txt_table}')
    time.sleep(2)
    

    if txt_table == 'Para este processo é necessário que existam registros na visão.':
        time.sleep(2)
        logging.debug('SEM REMESSAS BANCARIA')
        rm_nao = cc.wait_appear(locator.rm.titlebar_titlebar_rm, wait_timeout=15)
        rm_nao.click()
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

    else:
        time.sleep(3)
        logging.debug('TABELA CONTÉM REGISTROS')      
        click_nao = cc.wait_appear(locator.rm.button_não, wait_timeout=15)
        click_nao.set_focus()
        time.sleep(3)
        pyautogui.hotkey('alt', 'n')
        logging.debug('CLICK NÃO')
        time.sleep(5)

        number_rows = re.findall(r'\b(\d+)\b', txt_table)
        logging.debug(f'TIPO: {type(number_rows)}')
        rows_int = int(number_rows[0])
        logging.debug(f'NUMERO DE TUPLAS: {rows_int}')

        click_up = cc.wait_appear(locator.rm.button_uma_linha_para_cima, wait_timeout=15)

        for i in range (rows_int):
            click_up.click()

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')'''
        

def register_desmark_all():
    time.sleep(2)
    if count_ref == rows_int:
        return True
    else:
        return False

def check_ted_cip():

    global count_ref, flag_desmark
    count_ref = 0
    count_reg = 0

    logging.debug('VERIFICANDO O COD DO CLIENTE EM CADA REGISTRO')

    select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)

    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    else:

        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(rows_int)
        logging.info(f'MOVIDO PRA CIMA {rows_int} VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')

        select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)    
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    

    logging.debug(f'rows_int check_ted_cip(): {rows_int}')

    for i in range(rows_int):

        time.sleep(5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        ref_num = pyperclip.paste()
        time.sleep(2)

        for i in range(3):
            pyautogui.hotkey('right')
            logging.debug(f'{i} PASSOS PARA DIREITA >>')
        
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        cliente_num = pyperclip.paste()
        time.sleep(2)

        logging.debug(f'REFERENCIA LANÇAMENTO: {ref_num}')
        logging.debug(f'CLIENTE: {cliente_num}')

        for i in range(3):
            pyautogui.hotkey('left')
            logging.debug('3 PASSOS PARA ESQUERDA <<')

        if cliente_num in clientes:

            flag_desmark = False

            time.sleep(2)
            logging.debug(f'CLIENTE CONTIDO NA LISTA A REFERENCIA: {ref_num} NÃO SERÁ MODIFICADO PARA PIX')
            logging.debug('VERIFICANDO OS DADOS DE TED CIP')
            pyautogui.hotkey('ctrl', 'enter')
            time.sleep(5)

            logging.debug('VERIFICANDO INFORMAÇÕES')

            select_integracao_bancaria = waitForImage(image = integracao_bancaria, timeout=60, name = 'INTEGRAÇÃO BANCÁRIA')
            if select_integracao_bancaria is not None:
                time.sleep(2)
                pyautogui.click(select_integracao_bancaria)
                logging.debug('CLICA EM INTEGRAÇÃO BANCÁRIA')

            time.sleep(2)

            dados_banc = waitForImage(image = dados_bancarios, timeout=20, name = 'DADOS BANCARIOS')
            if dados_banc is not None:
                x, y = dados_banc.left - 130 , dados_banc.top + dados_banc.height // 2 
                pyautogui.click(x, y)
                logging.debug('CLICK EM INTEGRAÇÃO BANCÁRIA')

            else: 
                dados_banc2 = waitForImage(image = dados_bancarios_2, timeout=20, name = 'DADOS BANCARIOS 2')
                if dados_banc2 is not None:
                    x, y = dados_banc2.left - 130 , dados_banc2.top + dados_banc2.height // 2 
                    pyautogui.click(x, y)
                    logging.debug('CLICK EM INTEGRAÇÃO BANCÁRIA')

            time.sleep(10)

            logging.debug('ENTROU DADOS BANCÁRIOS')

            pyautogui.press('tab')
            logging.debug('APERTA TAB')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'c')
            logging.debug('CTRL C')
            time.sleep(1)
            pyautogui.write('TED')

            time.sleep(5)

            forma_pag_ted = waitForImage(image = forma_pag_ted_cip, timeout=30, name = 'FORMA DE PAGAMENTO TED CIP')
            if forma_pag_ted is not None:
                time.sleep(2)
                logging.debug('FORMA DE PAGAMENTO TED CIP')

            else:
                for i in range(4):
                    time.sleep(1)
                    pyautogui.press('tab')

                for i in range(21):
                    time.sleep(1)
                    pyautogui.press('down')

                for i in range(12):
                    time.sleep(1)
                    pyautogui.press('up')

                time.sleep(2)
            
        else:

            flag_desmark = True

            time.sleep(2)
            logging.debug('CLIENTE NÃO CONTIDO NA LISTA O LANÇAMENTO SERÁ MODIFICADO PARA PIX')
            pyautogui.hotkey('ctrl', 'enter')
            time.sleep(5)

            select_integracao_bancaria = waitForImage(image = integracao_bancaria, timeout=60, name = 'INTEGRAÇÃO BANCÁRIA')
            if select_integracao_bancaria is not None:
                time.sleep(2)
                pyautogui.click(select_integracao_bancaria)
                logging.debug('CLICA EM INTEGRAÇÃO BANCÁRIA')

            logging.debug('VERIFICANDO INFORMAÇÕES')
            time.sleep(5)

            dados_banc = waitForImage(image = dados_bancarios, timeout=20, name = 'DADOS BANCARIOS')
            if dados_banc is not None:
                x, y = dados_banc.left - 130 , dados_banc.top + dados_banc.height // 2 
                pyautogui.click(x, y)
                logging.debug('CLICK EM DADOS BANCARIOS')

            else:
                dados_banc2 = waitForImage(image = dados_bancarios_2, timeout=20, name = 'DADOS BANCARIOS 2')
                if dados_banc2 is not None:
                    x, y = dados_banc2.left - 130 , dados_banc2.top + dados_banc2.height // 2 
                    pyautogui.click(x, y)
                    logging.debug('CLICK EM INTEGRAÇÃO BANCÁRIA')

            time.sleep(5)

            logging.debug('ENTROU DADOS BANCÁRIOS')

            pyautogui.press('tab')
            logging.debug('APERTA TAB')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'c')
            logging.debug('CLICOU ctrl+c')
            #logging.debug('CTRL C')
            time.sleep(1)
            pyautogui.write('PIX')
            logging.debug('DIGITOU PIX')

            for i in range(4):
                time.sleep(1)
                pyautogui.press('tab')
                logging.debug(f'TAB CLICADO {i}')

            for i in range(21):
                time.sleep(1)
                pyautogui.press('down')
                logging.debug(f'DOWN CLIACADO {i}')

            time.sleep(1)
            pyautogui.press('up')

            time.sleep(2)

        click_ok()

        click_ok()

        if flag_desmark == True:
            count_ref += 1
            time.sleep(2)
            logging.debug(f'RETIRANDO A REFERENCIA: {ref_num} DO PROCESSAMENTO TED CIP TRANSFORMANDO PARA PIX')
            time.sleep(2)
        else:
            logging.debug(f'INSERINDO A REFERENCIA: {ref_num} DO PROCESSAMENTO TED CIP')
            pyautogui.hotkey('ctrl', 'space')
        
        if count_reg == 150 or count_reg == rows_int: ###
        #if count_reg == 1 or count_reg == rows_int:
            logging.debug(f'FORAM INCLUIDOS: {count_reg} REFERENCIAS NO PROCESSAMENTO TED CIP')
            break
        
        time.sleep(2)
        pyautogui.press('down')
        logging.debug('PASSANDO PARA PRÓXIMO REGISTRO')
        time.sleep(2)

def check_ted_branco():


    global register_out
    global ref_num

    count_reg = 0
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M')
    ref_processadas = []

    # Especificar o caminho para a pasta onde você deseja salvar o arquivo
    caminho_pasta_ref = r'C:\\Projetos_Remessas\\Remessa_Bancaria\\VariaveisControle'

    # Verificar se o caminho da pasta existe, se não, criar
    if not os.path.exists(caminho_pasta_ref):
        os.makedirs(caminho_pasta_ref)

    # Caminho completo para o arquivo
    caminho_arquivo = os.path.join(caminho_pasta_ref, 'ref_proc_form_pag_branco.txt')

    
    logging.debug('VERIFICANDO O COD DO CLIENTE EM CADA REGISTRO')
    select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=60)
    
    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')
    else:
        logging.debug('TABELA CONTÉM REGISTROS')

        largura_tela, altura_tela = pyautogui.size()

        #Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        time.sleep(1)

        #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
        cc.mouse.scroll(rows_int)
        logging.info(f'MOVIDO PRA CIMA {rows_int} VEZES')

        caixa_selecao = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
        caixa_selecao.click()
        time.sleep(1)
        caixa_selecao.click()
        time.sleep(1)
        pyautogui.hotkey('right')

        select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=15)    
        select_first_row.click()
        logging.debug('CLICA NA PRIMEIRA LINHA DA TABELA')

    ### CHECK TED BRANCO LIMITADO DEPOIS MODIFICAR PARA ROWS_INT
    for i in range(rows_int):

        count_reg += 1

        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        ref_num = pyperclip.paste()
        logging.debug(f'REFERNCIA: {ref_num}')
        logging.debug(f'CONTAGEM: {count_reg}')
        time.sleep(0.3)
        logging.debug('ENTRANDO NO REGISTRO ')
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(3)

        select_integracao_bancaria = waitForImage(image = integracao_bancaria, timeout=60, name = 'INTEGRAÇÃO BANCÁRIA')
        if select_integracao_bancaria is not None:
            pyautogui.click(select_integracao_bancaria)
            logging.debug('CLICA EM INTEGRAÇÃO BANCÁRIA')

        logging.debug('VERIFICANDO INFORMAÇÕES')

        dados_banc = waitForImage(image = dados_bancarios, timeout=20, name = 'TRES PONTINHOS')
        if dados_banc is not None:
            time.sleep(2)
            for i in range (3):
                time.sleep(1)
                pyautogui.press('tab')
            time.sleep(1)

            pyautogui.press('enter')
            time.sleep(2)

            pyautogui.write('PIX')
            time.sleep(2)

            pyautogui.press('enter')
            time.sleep(2)
            logging.debug('VERIFICANDO SE TEM PIX NO FILTRO')

            select_PIX = waitForImage(image = filter_pix, timeout=10, name = 'CHECANDO DADOS BANCÁRIOS PIX')
            if select_PIX is not None:
                time.sleep(2)
                logging.debug(f'PIX NÃO ENCONTRADO PARA REFERENCIA: {ref_num}')
                
                for i in range (4):
                    time.sleep(0.3)
                    pyautogui.press('tab')

                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)

                logging.debug(f'APERTA EM CANCELAR')

            else:
                logging.debug('PIX ENCONTRADO')

                register_out =+ 1
                for i in range (3):
                    time.sleep(0.3)
                    pyautogui.press('tab')
                
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('tab')
                logging.debug('APERTA TAB')
                time.sleep(2)

                """pyautogui.hotkey('ctrl', 'c')
                time.sleep(2)"""

                dados_banc = waitForImage(image = dados_bancarios, timeout=10, name = 'DADOS BANCARIOS')
                if dados_banc is not None:
                    x, y = dados_banc.left - 130 , dados_banc.top + dados_banc.height // 2 
                    pyautogui.click(x, y)
                    logging.debug('CLICK EM DADOS BANCARIOS')

                else:
                    dados_banc2 = waitForImage(image = dados_bancarios_2, timeout=10, name = 'DADOS BANCARIOS 2')
                    if dados_banc2 is not None:
                        x, y = dados_banc2.left - 130 , dados_banc2.top + dados_banc2.height // 2 
                        pyautogui.click(x, y)
                        logging.debug('CLICK EM INTEGRAÇÃO BANCÁRIA')

                pyautogui.press('tab')
                logging.debug('APERTA TAB')
                time.sleep(1)

                pyautogui.write('PIX')

                forma_pag = waitForImage(image = forma_pag_pix, timeout=10, name = 'CHECANDO DADOS BANCÁRIOS PIX')
                if forma_pag is not None:
                    time.sleep(2)
                    logging.debug(f'FORMA DE PAGAMENTO PIX SELECIONADA PARA O REGISTRO: {ref_num}')
                else:
                    logging.debug(f'FORMA DE PAGAMENTO PIX NÃO SELECIONADA PARA O REGISTRO: {ref_num}')
                    for i in range(4):
                        time.sleep(0.3)
                        pyautogui.press('tab')

                    time.sleep(2)

                    for i in range(21):
                        time.sleep(0.3)
                        pyautogui.press('down')

                    time.sleep(2)
                    pyautogui.press('up')
                    time.sleep(2)

                click_ok()
                logging.debug('PRIMEIRO OK')
        else:
            logging.debug('SEM FILTRO PIX')

        click_ok()

        error_salvar_pix2 = waitForImage(image = error_generico, timeout=10, name = 'ERROR GENERICO')
        if error_salvar_pix2 is not None:

            pyautogui.click(error_salvar_pix2)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('tab')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('enter')

        error_salvar_pix1 = waitForImage(image = error_salvar_pix, timeout=5, name = 'ERROR FILTRO PIX')
        if error_salvar_pix1 is not None:
            time.sleep(2)
            pyautogui.click(error_salvar_pix1)
            logging.debug('PRESS ERROR FILTRO PIX')
            time.sleep(2)
            pyautogui.press('esc')
            time.sleep(2)
        
        if count_reg == 150 or count_reg == rows_int: ###
        #if count_reg == 1 or count_reg == rows_int:
            logging.debug(f'FORAM VERIFICADOS: {count_reg} REFERENCIAS NO PROCESSAMENTO FORMA DE PAGAMENTO ELETRONICA EM BRANCO')
            break

        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        logging.debug('PASSANDO PARA PRÓXIMO REGISTRO')


def click_ok():

    btt_ok = waitForImage(image = button_ok, timeout=10, name = 'PRESS BUTTON OK')
    if btt_ok is not None:
        time.sleep(2)
        pyautogui.click(btt_ok)
        logging.debug('PRESS BUTTON OK')
        time.sleep(2)

    else:
        btt_ok_2 = waitForImage(image = button_ok_2, timeout=10, name = 'PRESS BUTTON OK 2')
        if btt_ok_2 is not None:
            time.sleep(2)
            pyautogui.click(btt_ok_2)
            logging.debug('PRESS BUTTON OK 2')
            time.sleep(5)

def end_RM():

    if len(ref_out) > 0:
        texto_msg = f'O BOT FOI ENCERRADO \n\nE TODOS AS REFERENCIAS FORAM RETIRADAS: {ref_out} \n\nDEVIDO A ALGUM TIPO DE ERRO NO PROCESSAMENTO.'
    else:
        texto_msg = 'O BOT FOI ENCERRADO'

    emailFinalizado(texto_msg)
    encerrar_processo_windows(nome_processo)
    #processo_inicio.terminate()
    logging.debug('RM ENCERRADO')
    sys.exit()



def obter_intervalo_data():

    # Mude para o diretório especificado
    os.chdir(caminho_da_pasta_data)


    # Nome do arquivo que você deseja ler
    nome_arquivo = 'data.txt'

    # Caminho completo do arquivo
    caminho_arquivo = os.path.join(caminho_da_pasta_data, nome_arquivo)

    hora = datetime.now().time()
    hora_atual = hora.hour
    logging.debug(f'VERIFICANDO A HORA ATUAL {hora_atual}')

    # Verifique se o arquivo existe
    if os.path.exists(caminho_arquivo):
        # Abra o arquivo em modo de leitura
        
        # Padrão regex para encontrar a linha com PIX e a data
        padrao = re.compile(r'BANCARIA:\s*(\d{2}/\d{2}/\d{4}),\s*(\d{2}/\d{2}/\d{4})')

        # Variáveis para armazenar as datas
        data_inicial = None
        data_final = None

        # Ler o conteúdo do arquivo data.txt
        with open('data.txt', 'r') as arquivo:
            for linha in arquivo:
                # Encontrar a correspondência usando o padrão regex
                correspondencia = padrao.search(linha)

                # Verificar se a correspondência foi encontrada
                if correspondencia:
                    # Obter as datas correspondentes
                    data_inicial = correspondencia.group(1)
                    data_final = correspondencia.group(2)

        # Imprimir as datas antes da remoção
        logging.debug(f'Data Inicial BANCARIA antes da remoção: {data_inicial}')
        logging.debug(f'Data Final BANCARIA antes da remoção: {data_final}')

        # Remover as datas do arquivo data.txt
        with open('data.txt', 'r') as arquivo:
            conteudo = arquivo.read()

        conteudo_sem_datas = padrao.sub('BANCARIA:,', conteudo)

        with open('data.txt', 'w') as arquivo:
            arquivo.write(conteudo_sem_datas)

        # Imprimir as datas após a remoção
        logging.debug(f'Data Inicial BANCARIA após a remoção: {data_inicial}')
        logging.debug(f'Data Final BANCARIA após a remoção: {data_final}')

        
        if data_inicial == None or data_final == None:
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
                data_inicio = data_fim = None

            return data_inicio + timedelta(days=7), data_fim + timedelta(days=7)
        
        else:
            data_inicial_final = datetime.strptime(data_inicial, '%d/%m/%Y')
            data_final_final = datetime.strptime(data_final, '%d/%m/%Y')
            return data_inicial_final, data_final_final
    else:
        hoje = datetime.now()
        logging.debug(f'hoje -  {hoje}')
        dia_semana_hoje = hoje.weekday()  # Retorna um número entre 0 (segunda) e 6 (domingo)

        if dia_semana_hoje in [2, 3, 4, 5, 6]:  # Quarta, quinta ou sexta
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
            data_inicio = data_fim = None

        return data_inicio + timedelta(days=7), data_fim + timedelta(days=7)


def rename_arq():

    global novo_nome

    inicio, fim = obter_intervalo_data()

    dt_inicial_format = inicio.strftime("%d-%m-%Y")
    dt_final_format = fim.strftime("%d-%m-%Y")
    logging.debug('CLICK - SELECIONA A DATA DE QUARTA FEIRA E DA PROXIMA TERÇA')
    logging.debug(f'QUARTA-FEIRA: {dt_inicial_format}')
    logging.debug(f'TERCA-FEIRA: {dt_final_format}')

    data_inicial_param = inicio.strftime("%d")
    data_final_param = fim.strftime("%d")
    data_ano_param = fim.strftime("%Y")
    dois_digitos_ano = str(data_ano_param)[-2:]

    # Caminho da pasta
    #caminho_da_pasta = r"X:\\"
    #caminho_da_pasta = r"C:\\Totvs\\Remessa"
    # Nome original do arquivo

    #nome_original = 'SISPAG-PAGTO.txt' ####
    nome_original = 'PAG-SANTANDER.txt'
    

    # Liste todos os arquivos na pasta
    arquivos = os.listdir(caminho_da_pasta)

    # Encontre a última letra usada
    #arquivos_com_padrao = [arquivo[-5] for arquivo in arquivos if arquivo.startswith(f'B{data_inicial_param}{data_final_param}{dois_digitos_ano}') and arquivo.endswith('.txt')]
    arquivos_com_padrao = [arquivo[-5] for arquivo in arquivos if arquivo.startswith(f'SANT{data_inicial_param}{data_final_param}{dois_digitos_ano}') and arquivo.endswith('.txt')]
    logging.debug('ARQUIVO COM PADRAO: ', arquivos_com_padrao)

    if arquivos_com_padrao:    
        ultima_letra_usada = max(arquivos_com_padrao)
        logging.debug('QUANDO NÃO É A: ', ultima_letra_usada)
        # Determine a próxima letra
        proxima_letra = chr(ord(ultima_letra_usada) + 1)
        # Novo nome do arquivo
        #novo_nome = (f'B{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt')
        novo_nome = (f'SANT{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt')
        logging.debug(f'A PRÓXIMA LETRA SERÁ: {proxima_letra}')
        logging.debug(f'NOME ARQUIVO: B{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt')
    else:
        proxima_letra = 'A'
        logging.debug('A LETRA A SER USADA É: ', proxima_letra)
        # Novo nome do arquivo
        #novo_nome = (f'B{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt')
        novo_nome = (f'SANT{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt')
        logging.debug(f'SANT{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt')


    caminho_1 = f'{caminho_da_primeira_pasta}\\{nome_original}'
    caminho_2 = f'{caminho_da_pasta}\\{nome_original}'

    shutil.move(caminho_1, caminho_2)

    
    # Caminho completo do arquivo original
    caminho_original = os.path.join(caminho_da_pasta, nome_original)

    # Caminho completo do novo arquivo
    caminho_novo = os.path.join(caminho_da_pasta, novo_nome)

    # Renomeia o arquivo
    try:
        os.rename(caminho_original, caminho_novo)
        logging.debug(f"Arquivo renomeado com sucesso para {novo_nome}")
    except FileNotFoundError:
        logging.debug(f"O arquivo {nome_original} não foi encontrado no diretório {caminho_da_pasta}")
    except FileExistsError:
        logging.debug(f"Já existe um arquivo chamado {novo_nome} no diretório {caminho_da_pasta}")
    except Exception as e:
        logging.debug(f"Ocorreu um erro ao renomear o arquivo: {e}")
        
    excel()

    email_msg = 'Remessas Boleto foram processadas'
    emailSuccess(email_msg)
    
    
def excel():
    global workbook, caminho_excel

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
        
    nome = novo_nome.split('.')[0]
    caminho_excel = f'{excel_path}/{today}/{nome}.xlsx'
    workbook.save(caminho_excel) 
    
    logging.info('EXCEL Criado')


def waitForImage(image, timeout, name):
    inicialTime = time.time()

    while True:
        try:
            location = pyautogui.locateOnScreen(image=image, confidence=0.9)

            if location is not None:
                logging.info(f'{name} image found.')
                return location

            currentTime = time.time()
            if currentTime - inicialTime >= timeout:
                logging.info(f'{name} image not found.')
                return None

            time.sleep(0.5)
        
        except:
            currentTime = time.time()
            if currentTime - inicialTime >= timeout:
                logging.info(f'{name} image not found.')
                return None

            time.sleep(0.5)


def emailSuccess(email_msg):
    with open(f'{email_path}/emailSuccess.html', 'r', encoding='utf-8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.replace('{mensagem}', email_msg)

    yag.send(to=str(email_receivers).split(','), subject="SUCESSO - BOT REMESSA BANCÁRIA",
             contents=htmlSuccess,
             attachments=[f'{log_path}/{today}/{log_file_name}.log', f'{caminho_da_pasta}/{novo_nome}', caminho_excel])
    
    logging.info('Success e-mail sent.')

def emailErro(texto_msg):
    with open(f'{email_path}/emailError.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.format(mensagem = texto_msg)
    yag.send(to=str(email_receivers).split(','), subject=f"ERRO - BOT REMESSA BANCÁRIA",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Warning e-mail sent.')

def emailFinalizado(texto_msg):
    with open(f'{email_path}/emailFinalizado.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.format(mensagem = texto_msg)
    yag.send(to=str(email_receivers).split(','), subject=f"BOT REMESSAS BANCÁRIA FINALIZADO",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Warning e-mail sent.')


def caps():
    logging.debug('DESATIVANDO CAPS')

    pyautogui.press("capslock") if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False

