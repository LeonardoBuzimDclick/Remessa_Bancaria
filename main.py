from clicknium import locator, ui
from clicknium import clicknium as cc
from SUBPROGRAMS.functions import *
from SUBPROGRAMS.parameters import *
import pyautogui, time

if __name__ == '__main__':

    sys.excepthook = show_exception_and_exit
    encerrar_processo_windows(nome_processo)
    bot_text_art()
    open_RM()
    caps()
    loggin_RM()
    enter_coligada()
    check_movimentacao_bancaria()
    enter_contas_a_pagar()
    data_filter()
    desmark_filter()
    filter_clean()
    result = check_table_record()
    if result == True:
        movimentacao_bancaria()
        processo_pagamento()
        logging.debug('SEM REMESSA BANCÁRIA')
        logging.debug('ENCERRANDO O RM')
        email_msg = 'Sem Remessa Bancária para essa data. O programa será encerrado'
        emailFinalizado(email_msg)
        logging.debug('FECHA O PROGRAMA')
        time.sleep(2)
        logging.debug('RM ENCERRADO')
        sys.exit()
    else:
        select_tipo_documento()
        filter_IPTE()
        result = check_table_record()
        if result == True:
            logging.debug('SEM REMESSA BANCÁRIA')
            #email_msg = 'Sem Remessa Bancária com filtro tipo de documento diferente de INV e filtro IPTE (não branco). \n PASSO 1 FINALIZADO'
            #emailFinalizado(email_msg)
            #logging.debug(email_msg)
            movimentacao_bancaria()
            processo_pagamento()
            enter_contas_a_pagar()
            data_filter()
            desmark_filter()
            filter_clean()
            filter_forma_pagamento()
            result = check_table_record()
            if result == True:
                time.sleep(2)
                logging.debug('SEM REMESSA DE TED CIP')
                #email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica igual a TED CIP \n PASSO 2 FINALIZADO'
                #emailFinalizado(email_msg)
                #logging.debug(email_msg)
                enter_contas_a_pagar()
                data_filter()
                desmark_filter()
                filter_clean()
                filter_forma_pagamento_branco()
                result = check_table_record()
                if result == True:
                    time.sleep(2)
                    logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                    email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                    emailFinalizado(email_msg)
                    logging.debug(email_msg)
                    logging.debug('O PROGRAMA SERÁ ENCERRADO')
                    end_RM()
                else:
                    check_ted_branco()
                    email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                    emailFinalizado(email_msg)
                    logging.debug(email_msg)
                    logging.debug('O PROGRAMA SERÁ ENCERRADO')
                    end_RM()
            else:
                check_ted_cip()
                result = register_desmark_all()
                if result == False:
                    result == process_lancamentos()
                    if result == True:
                        movimentacao_bancaria()
                        processo_pagamento()
                        #email_msg = 'Remessas TED CIP foram processadas \n PASSO 2 FINALIZADO'
                        #emailFinalizado(email_msg)
                        #logging.debug(email_msg)
                        enter_contas_a_pagar()
                        data_filter()
                        desmark_filter()
                        filter_clean()
                        filter_forma_pagamento_branco()
                        result = check_table_record()
                        if result == True:
                            time.sleep(2)
                            logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                            email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                            emailFinalizado(email_msg)
                            logging.debug(email_msg)
                            logging.debug('O PROGRAMA SERÁ ENCERRADO')
                            end_RM()
                        else:
                            check_ted_branco()
                            email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                            emailFinalizado(email_msg)
                            logging.debug(email_msg)
                            logging.debug('O PROGRAMA SERÁ ENCERRADO')
                            end_RM()
                    else:
                        enter_contas_a_pagar()
                        data_filter()
                        desmark_filter()
                        filter_clean()
                        filter_forma_pagamento_branco()
                        result = check_table_record()
                        if result == True:
                            time.sleep(2)
                            logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                            email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                            emailFinalizado(email_msg)
                            logging.debug('O PROGRAMA SERÁ ENCERRADO')
                            end_RM()
                        else:
                            check_ted_branco()
                            email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificada para pix \n PASSO 3 FINALIZADO'
                            emailFinalizado(email_msg)
                            logging.debug(email_msg)
                            logging.debug('O PROGRAMA SERÁ ENCERRADO')
                            end_RM()
                else:
                    #email_msg = 'Remessas de TED cliente não listado foram transformadas em pix. \n PASSO 2 FINALIZADO'
                    #emailFinalizado(email_msg)
                    #logging.debug(email_msg)
                    enter_contas_a_pagar()
                    data_filter()
                    desmark_filter()
                    filter_clean()
                    filter_forma_pagamento_branco()
                    result = check_table_record()
                    if result == True:
                        time.sleep(2)
                        logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                        email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                        emailFinalizado(email_msg)
                        logging.debug(email_msg)
                        logging.debug('O PROGRAMA SERÁ ENCERRADO')
                        end_RM()
                    else:
                        check_ted_branco()
                        email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                        emailFinalizado(email_msg)
                        logging.debug(email_msg)
                        logging.debug('O PROGRAMA SERÁ ENCERRADO')
                        end_RM()
        else:
            check_payment_type()
            result = process_lancamentos()
            if result == True:
                movimentacao_bancaria()
                processo_pagamento()
                enter_contas_a_pagar()
                data_filter()
                desmark_filter()
                filter_clean()
                filter_forma_pagamento()
                result = check_table_record()
                if result == True:
                    time.sleep(2)
                    logging.debug('SEM REMESSA DE TED CIP')
                    #email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica igual a TED CIP \n PASSO 2 FINALIADO'
                    #emailFinalizado(email_msg)
                    #logging.debug(email_msg)
                    enter_contas_a_pagar()
                    data_filter()
                    desmark_filter()
                    filter_clean()
                    filter_forma_pagamento_branco()
                    result = check_table_record()
                    if result == True:
                        time.sleep(2)
                        logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                        email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco\n PASSO 3 FINALIZADO'
                        emailFinalizado(email_msg)
                        logging.debug(email_msg)
                        logging.debug('O PROGRAMA SERÁ ENCERRADO')
                        end_RM()
                    else:
                        check_ted_branco()
                        email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                        emailFinalizado(email_msg)
                        logging.debug(email_msg)
                        logging.debug('O PROGRAMA SERÁ ENCERRADO')
                        end_RM()
                else:
                    check_ted_cip()
                    result = register_desmark_all()
                    if result == False:
                        result = process_lancamentos()
                        if result == True:
                            movimentacao_bancaria()
                            processo_pagamento()
                            #email_msg = 'Remessas TED CIP foram modificadas \n PASSO 2 FINALIADO'
                            #emailFinalizado(email_msg)
                            #logging.debug(email_msg)
                            enter_contas_a_pagar()
                            data_filter()
                            desmark_filter()
                            filter_clean()
                            filter_forma_pagamento_branco()
                            result = check_table_record()
                            if result == True:
                                time.sleep(2)
                                logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                                email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                                emailFinalizado(email_msg)
                                logging.debug(email_msg)
                                logging.debug('O PROGRAMA SERÁ ENCERRADO')
                                end_RM()
                            else:
                                check_ted_branco()
                                email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                                emailFinalizado(email_msg)
                                logging.debug(email_msg)
                                logging.debug('O PROGRAMA SERÁ ENCERRADO')
                                end_RM()
                        else:
                            enter_contas_a_pagar()
                            data_filter()
                            desmark_filter()
                            filter_clean()
                            filter_forma_pagamento_branco()
                            result = check_table_record()
                            if result == True:
                                time.sleep(2)
                                logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                                email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                                emailFinalizado(email_msg)
                                logging.debug(email_msg)
                                logging.debug('O PROGRAMA SERÁ ENCERRADO')
                                end_RM()
                            else:
                                check_ted_branco()
                                email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                                emailFinalizado(email_msg)
                                logging.debug(email_msg)
                                logging.debug('O PROGRAMA SERÁ ENCERRADO')
                                end_RM()
                    else:
                        #email_msg = 'Remessas de TED cliente não listado foram transformadas em pix. \n PASSO 2 FINALIZADO'
                        #emailFinalizado(email_msg)
                        #logging.debug(email_msg)
                        enter_contas_a_pagar()
                        data_filter()
                        desmark_filter()
                        filter_clean()
                        filter_forma_pagamento_branco()
                        result = check_table_record()
                        if result == True:
                            logging.debug('SEM REMESSA FORMA DE PAGAMENTO TED CIP EM BRANCO')
                            email_msg = 'Sem Remessa Bancária com filtro forma de pagamento eletronica em branco \n PASSO 3 FINALIZADO'
                            emailFinalizado(email_msg)
                            logging.debug(email_msg)
                            logging.debug('O PROGRAMA SERÁ ENCERRADO')
                            end_RM()
                        else:
                            check_ted_branco()
                            email_msg = 'Remessa Bancária TED CIP com filtro de pagamento eletronica em branco modificadas para pix \n PASSO 3 FINALIZADO'
                            emailFinalizado(email_msg)
                            logging.debug(email_msg)
                            logging.debug('O PROGRAMA SERÁ ENCERRADO')
                            end_RM()