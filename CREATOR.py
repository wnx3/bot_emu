import time
import os
import random
import subprocess
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import string
import sys
from faker import Faker
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from colorama import init, Fore, Back, Style
from mailtm import Email
import re
import logging
print('testewww')
logger = logging.getLogger(__name__)

handler = logging.FileHandler('log.txt')
handler.setLevel(logging.ERROR)

logger.addHandler(handler)

username = os.getenv('USERNAME')

with open("configuracoes\outros\SPREADSHEET_ID.txt", "r") as arquivo:
    SPREADSHEET_ID = arquivo.read().strip()
RANGE_NAME = 'contas!A:D'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def vpn_nord():
    global sms
    print(Fore.LIGHTRED_EX + 'SMS' + Style.RESET_ALL)
    gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    print('Limpando dados.')
    sms = True
    print(Fore.LIGHTMAGENTA_EX + 'Alterando IP da NordVPN\n' + Style.RESET_ALL)
    try:
        driver.start_activity("com.nordvpn.android", ".MainActivity")
    except:
        pass
    time.sleep(10)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/reconnect_button'))).click()
    except:
        pass
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/secondary_quick_connect_button'))).click()
    except:
        pass
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/primary_quick_connect_button'))).click()
    time.sleep(5)
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)

    abc = False


def vpn_surf():
    global sms
    print(Fore.LIGHTRED_EX + 'SMS' + Style.RESET_ALL)
    sms = True
    print(Fore.LIGHTMAGENTA_EX + 'Alterando IP da SurfShark\n' + Style.RESET_ALL)
    gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True, shell=True)
    print('Limpando dados.')
    try:
        driver.start_activity("com.surfshark.vpnclient.android", ".StartActivity")
    except:
        pass
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
    time.sleep(5)
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True, shell=True)

    abc = False


def vpn_avg():
    global sms
    print(Fore.LIGHTRED_EX + 'SMS' + Style.RESET_ALL)
    gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True, shell=True)
    print('Limpando dados.')
    sms = True
    print(Fore.LIGHTMAGENTA_EX + 'Alterando IP da AVG\n' + Style.RESET_ALL)
    try:
        driver.start_activity("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
    except:
        pass
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True, shell=True)

    #time.sleep(10)
    #WebDriverWait(driver, 30).until(
    #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
    #time.sleep(10)
    #WebDriverWait(driver, 30).until(
    #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
    #time.sleep(5)
    #WebDriverWait(driver, 30).until(
    #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
    #time.sleep(5)
    
    abc = False
def listener(message):
    global cod
    if 'code' in message['subject']:
        cod = re.search(r'\d+', message['subject']).group(0)
def gerar_email():
    global sms
    global email
    lista_user = random.choices(range(1, 9), k=3)
    fake = Faker()
    nome = fake.first_name_female()
    sobrenome = fake.last_name_female()
    nome_completo = nome + ' ' + sobrenome
    nome_completo_s = nome + sobrenome
    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
    user_completo = nome_completo_s + '.' + str(numeros_concatenados)

    test = Email()
    arquivo = open('configuracoes/contas/senha_perfis.txt')
    senha = arquivo.read()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

    test.register(username=user_completo, password=senha)
    print("Email gerado: " + str(test.address))
    time.sleep(4)
    email = str(test.address)
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
        email)
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
    # driver.find_element(By.XPATH,
    #                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()

    print('Codigo enviado')
    codigo = None
    try:
        test.start(listener, interval=15)
        codigo = 0
        while codigo != 20:
            time.sleep(2)
            codigo = codigo + 1
        codigo = cod
    except Exception as e:
        if "many requests" in str(e):
            pass
        else:
            print(e)
    print(f"Codigo recebido: {codigo}")
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            codigo)
    except:
        print('Instagram fechou')
    time.sleep(2)

    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()

    except:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()

    test.stop()
    time.sleep(3)
    codigo_invalido = driver.find_elements(By.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
    continua_na_tela = driver.find_elements(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View')
    continua_na_tela2 = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
    criou = driver.find_elements(By.XPATH,
                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
    time.sleep(15)
    if len(criou) == 1 and len(continua_na_tela) or len(continua_na_tela2) == 0:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
        print('Codigo aceito na primeira tentativa')
        return
        # irverificar = 1

    if len(codigo_invalido) == 1:
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()
        codigo = None
        try:
            test.start(listener, interval=15)
            codigo = 0
            while codigo != 20:
                time.sleep(1.5)
                codigo = codigo + 1
            codigo = cod
        except Exception as e:
            if "many requests" in str(e):
                pass
            else:
                print(e)
        print(f"Codigo recebido: {codigo}")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            codigo)
        try:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        except:
            pass
        try:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
            except:
                pass
        except:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
            except:
                pass
        test.stop()
        time.sleep(3)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')))
    reenv_cod = driver.find_elements(By.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
    if len(reenv_cod) == 1:
        print('Enviando um novo codigo.')
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()

        codigo = None
        
        codigo = 0
        try:
            while codigo != 20:
                test.start(listener, interval=5)
                time.sleep(1.5)
                codigo = codigo + 1
            codigo = cod
        except Exception as e:
            if "many requests" in str(e):
                pass
            else:
                print(e)
        print(f"Codigo recebido: {codigo}")
        #time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            codigo)
        #try:
        #    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #except:
        #    pass
        try:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
            except:
                pass
        except:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
            except:
                pass
        test.stop()
        time.sleep(3)
        codigo_invalido = driver.find_elements(By.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
        continua_na_tela = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[5]')
        if len(codigo_invalido) == 1:
            driver.find_element(By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
            driver.find_element(By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()
            codigo = None
            try:
                test.start(listener, interval=15)
                codigo = 0
                while codigo != 20:
                    time.sleep(2)
                    codigo = codigo + 1
                codigo = cod
            except Exception as e:
                if "many requests" in str(e):
                    pass
                else:
                    print(e)
            print(f"Codigo recebido: {codigo}")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                codigo)
            try:
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
                try:
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
                except:
                    pass
            except:
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                try:
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
                except:
                    pass

            test.stop()
            time.sleep(5)
    elif reenv_cod == 0:
        print('Codigo aceito.')
def gerar_email_firts_reg():
    global cod
    global email
    global lista_user
    global fake
    global nome
    global sobrenome
    global nome_completo
    global nome_completo_s
    global numeros_concatenados
    global user_completo
    lista_user = random.choices(range(1, 9), k=3)
    fake = Faker()
    nome = fake.first_name_female()
    sobrenome = fake.last_name_female()
    nome_completo = nome + ' ' + sobrenome
    nome_completo_s = nome + sobrenome
    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
    user_completo = nome_completo_s + '.' + str(numeros_concatenados)

    test = Email()
    arquivo = open('configuracoes/contas/senha_perfis.txt')
    senha = arquivo.read()
    test.register(username=user_completo, password=senha)
    print("Email gerado: " + str(test.address))
    time.sleep(2)
    email = str(test.address)
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
        email)
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()

    print('Codigo enviado')
    codigo = None
    try:
        test.start(listener, interval=15)
        codigo = 0
        while codigo != 20:
            time.sleep(2)
            codigo = codigo + 1
        codigo = cod
    except Exception as e:
        if "many requests" in str(e):
            pass
        else:
            print(e)
    print(f"Codigo recebido: {codigo}")
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            codigo)
        time.sleep(2)
    except:
        print('Erro encontrado.')
        time.sleep(5)
    time.sleep(2)
    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
    except:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
    test.stop()
    time.sleep(5)
    codigo_invalido = driver.find_elements(By.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
    continua_na_tela = driver.find_elements(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
    if len(codigo_invalido) and len(continua_na_tela) == 1:
        print('Erro encontrado.')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]'))).click()
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ''))).click()

        time.sleep(2)
        codigo = None
        try:
            test.start(listener, interval=15)
            codigo = 0
            while codigo != 20:
                time.sleep(1.5)
                codigo = codigo + 1
            codigo = cod
        except Exception as e:
            if "many requests" in str(e):
                pass
            else:
                print(e)
        print(f"Código recebido: {codigo}")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            codigo)
        try:
            driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()

        except:
            driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()

        test.stop()
        time.sleep(3)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[8]')))
def gerar_id():
    chars = string.ascii_lowercase + string.digits
    android_id = ''.join(random.choice(chars) for i in range(16))
    return android_id
def firts_reg():
    abc = True
    while abc:
        global sms
        sms = True
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)

        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            time.sleep(3)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            time.sleep(1)
            gerar_email_firts_reg()
        except Exception as e:
            pass

            # Gerar nome de usuário, digitar no campo e clicar em avançae
            # nome_completo = nome + ' ' + sobrenome

        print('Nome escolhido: ' + nome_completo)
        try:
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                nome_completo)
        except:
            cont = False
            print('Erro encontrado.')
            pass
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]'))).send_keys(
            senha)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[5]/android.view.View'))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'))).click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[6]'))).click()
        idade_aleatoria = random.randint(25, 50)
        print(f'Idade escolhida: {idade_aleatoria}')
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(idade_aleatoria)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
        op2 = driver.find_elements(By.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View')
        op1 = driver.find_elements(By.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
        time.sleep(5)
        try:
            if len(op1) == 0:
                try:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View').click()
                except:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click()
        except:
            try:
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()

            except:
                print('Erro ao criar')
                sms = True
                continue

        try:
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]'))).click()
            time.sleep(3)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                user_completo)
            print(f'Usuário gerado: {user_completo}')
            time.sleep(3)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            time.sleep(5)
            erro_2 = driver.find_elements(By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[*]/android.view.View[*]/android.widget.Button')
            erro_1 = driver.find_elements(By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
            if len(erro_2) == 1:
                print('Tentando gerar novamente')
                time.sleep(5)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))).click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]'))).click()
                time.sleep(3)
            if len(erro_1) == 1:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
            time.sleep(4)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View'))).click()

        except:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
        time.sleep(5)
        print('Verificando...')
        time.sleep(2)
        verificar = driver.find_elements(By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
        #time.sleep(10)

        conta_criada = driver.find_elements(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
        conta_sms = driver.find_elements(By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')

        try:
            if len(verificar) == 1:
                print(Fore.LIGHTGREEN_EX + 'Conta criada com sucesso.' + Style.RESET_ALL)
                now = datetime.now()
                timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                service = build('sheets', 'v4', credentials=creds)
                # Get values of columns A and B
                result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
                values = result.get('values', [])
                # Find first empty row
                first_empty_row_index = len(values) + 1
                # Insert user, password, and timestamp into first empty row
                range_to_update = f'contas!A{first_empty_row_index}:D{first_empty_row_index}'
                value_input_option = 'USER_ENTERED'
                value_range_body = {'values': [[user_completo + ' ' + senha, email, timestamp, username]]}
                result = service.spreadsheets().values().update(
                    spreadsheetId=SPREADSHEET_ID,
                    range=range_to_update,
                    valueInputOption=value_input_option,
                    body=value_range_body).execute()

                arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                # Escreva mais conteúdo no arquivo
                arquivo.write(user_completo + ' ' + senha + "\n")
                arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                # Escreva mais conteúdo no arquivo
                arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View'))).click()

                sms = False
                break
            else:
                with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                    conteudo = arquivo.read().strip()
                # Executa a função correspondente ao conteúdo do arquivo
                if conteudo == "avg":
                    vpn_avg()
                elif conteudo == "surf":
                    vpn_surf()
                elif conteudo == "nord":
                    vpn_nord()
                else:
                    print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")

        except:
            sms = True
            break

options = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
options.page_load_strategy = 'none'
options.add_experimental_option("prefs", prefs)


porta = input('Digite a porta: ')
arquivo = open('configuracoes/contas/senha_perfis.txt')
senha = arquivo.read()
print(f'Senha sendo utilizada: {senha}\n')

device = [
    {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
]
comando = f"adb connect 127.0.0.1:{porta}"
subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

gerar_id()
android_id = gerar_id()
subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL, shell=True)
time.sleep(2)
subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)
cont = True
while cont is True:

    print('\n-----------------------------------\nIniciando criação')
    with open("storage/apk/caminho.txt", "r") as arquivo:
        appinsta = arquivo.read().strip()
    try:
        time.sleep(10)
        quantidade = 0
        desired_caps = {}
        desired_caps['udid'] = '127.0.0.1:' + porta
        desired_caps['newCommandTimeout'] = '500'
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['appPackage'] = 'com.instagram.lite'
        desired_caps['appActivity'] = 'com.facebook.lite.MainActivity'
        desired_caps['systemPort'] = random.randint(6000, 8299)
        desired_caps['noReset'] = True
        desired_caps['app'] = appinsta
        
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        gerar_id()
        android_id = gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        time.sleep(2)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)

        try:
            firts_reg()

        except Exception as e:
            sms = True
            with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                conteudo = arquivo.read().strip()

               # Executa a função correspondente ao conteúdo do arquivo
                if conteudo == "avg":
                    vpn_avg()
                elif conteudo == "surf":
                    vpn_surf()
                elif conteudo == "nord":
                    vpn_nord()
                else:
                    print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
            continue

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View')))
        except:
            continue
        
        while sms is False:
            try:
                pular_erro = driver.find_elements(By.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                if len(pular_erro) == 0:
                    try:
                        driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                    except:
                        sms = True
                        continue
                print('-----------------------------------\nCriação de outro perfil.')
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                # Clicar no botão de perfil
                try:
                    time.sleep(3)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]')))
                    time.sleep(2)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()

                except:
                    time.sleep(3)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(2)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()

                # Clicar em perfis
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                # Clicar em adicionar conta
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'))).click()
                # Clicar em criar nova conta
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'))).click()
                # Gerar nome de usuário, digitar no campo e clicar em avançae
                lista_user = random.choices(range(1, 9), k=3)
                fake = Faker()
                nome = fake.first_name_female()
                sobrenome = fake.last_name_female()
                nome_completo = nome + sobrenome
                numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                user_completo = nome_completo + '.' + str(numeros_concatenados)
                print('User criado: ' + user_completo)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                    user_completo)
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                # Digitar senha e avançar
                arquivo = open('configuracoes/contas/senha_perfis.txt')
                senha = arquivo.read()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                    senha)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                # Clicar em adicionar email
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                # Clicar em email, gerar e avançar

                time.sleep(5)
                gerar_email()
                WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                print('Verificando...')
                time.sleep(20)
                verificar = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
                time.sleep(1)

                conta_criada = driver.find_elements(By.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                conta_sms = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                if len(verificar) == 1:
                    try:
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()
                    except:
                        pass
                    print(Fore.LIGHTGREEN_EX + 'Conta criada com sucesso.' + Style.RESET_ALL)

                    now = datetime.now()
                    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

                    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                    service = build('sheets', 'v4', credentials=creds)
                    # Get values of columns A and B
                    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                                 range=RANGE_NAME).execute()
                    values = result.get('values', [])
                    # Find first empty row
                    first_empty_row_index = len(values) + 1
                    # Insert user, password, and timestamp into first empty row
                    range_to_update = f'contas!A{first_empty_row_index}:D{first_empty_row_index}'
                    value_input_option = 'USER_ENTERED'
                    value_range_body = {'values': [[user_completo + ' ' + senha, email, timestamp, username]]}
                    result = service.spreadsheets().values().update(
                        spreadsheetId=SPREADSHEET_ID,
                        range=range_to_update,
                        valueInputOption=value_input_option,
                        body=value_range_body).execute()
                    arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')  # Escreva mais conteúdo no arquivo
                    arquivo.write(user_completo + ' ' + senha + "\n")
                    time.sleep(4)
                    arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                    arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()
                    sms = False

                else:
                    try:
                        with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                            conteudo = arquivo.read().strip()

                        # Executa a função correspondente ao conteúdo do arquivo
                        if conteudo == "avg":
                            vpn_avg()
                        elif conteudo == "surf":
                            vpn_surf()
                        elif conteudo == "nord":
                            vpn_nord()
                        else:
                            print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")

                    except:
                        sms = True
            except:
                sms = True
    # finally:
    #    print('')
    except Exception as e:
        logger.error('Ocorreu um erro: %s', e)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        print('Algum erro não catalogado encontrado.\n-----------------------------------\n')
