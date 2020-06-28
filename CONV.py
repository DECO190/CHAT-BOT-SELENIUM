from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
cont = 0
cont1 = sat = k = most = 0
rua = valo = av = av2 = rua2 =  resta = permis= b = nome = ''
def cab(text):
    print("=="*20)
    print(f'{text}'.center(40))
    print("==" * 20)
ach= True
oi = ['oi','ola','salve','suav?', 'tranquilo ']
temp = ['como esta o dia', 'como esta o dia hoje', 'qual a temperatura de hoje'
        ,'como esta o tempo', 'como esta o tempo hoje', 'vai chover hoje', 'hoje vai chover', 'vai chover hoje'
        ,'vai fazer sol hoje', 'hoje vai fazer sol' , 'vai ter sol hoje', 'qual a temperatura','tempo','temperatura']
cono = ['conometro','contar','contar segundos','segundos']
rest = ['restaurante', 'comida', 'restaurantes proximos', 'restaurantes','refeição']
idioma = ['traduza', 'traduzir essa porra', 'traduzir essa frase', 'traduzir']
dicionario = ['sig','palavra','significado','dic','dicionario']
mensagem = ['mensagem', 'insta','instagram','enviar mensagem', 'instagram','mensagem','enviar mensagem para alguem'
            ,'enviar', 'mensagens']
senha = ['senha','passe','password','pass','ver minhas senhas', 'senhas','entrar em senhas','gerenciador de senha'
         ,'gerenciador','gerenciador de senhas']
sair = ['quero sair', 'sair', 'vazar','mete o pe','sai']
print("\033[35;1m=="*20)
print(f'ASSISTENTE VIRTUAL'.center(40))
print("\033[35;1m==\033[m" * 20)
while True:
    permis = True
    site = True
    per = str(input('\033[1;33m>\033[m \033[1;34mCOMO POSSO AJUDAR? \033[m')).strip().lower()

    if per in oi:
        print('\033[1;32mOLÁ! Será um prazer atende-lo(a)\033[m')
        site = False

    if per in temp:
        cab('TEMPERATURA')
        while ach:
            site = False
            local = str(input('\033[1;33m>\033[m \033[1;34mDIGITE O LOCAL: \033[m')).strip()
            print("-"*40)
            print("\033[1;33mCOLETANDO INFORMARÇÕES...\033[m")
            print("-"*40)
            browser = Chrome()
            browser.minimize_window()
            browser.get('https://www.google.com/search?q=temperatura&oq=temperatura&aqs=chrome..69i57j0l7.3157j1j7&sourceid=chrome&ie=UTF-8')
            try:
                loc = browser.find_element_by_name('q')
                t = loc.send_keys(f' {local}')
                loc.send_keys(Keys.RETURN)

                tm = browser.find_element_by_id('wob_tm')
                ceu = browser.find_element_by_id('wob_dc')

            except:
                print('\033[1;31mLUGAR DESCONHECIDO!\033[m')
                print('--'*20)
                browser.close()
                pass
            else:
                g = ceu.text
                print(f'\033[34m> A TEMPERATURA EM \033[m\033[1;33m{local.upper()}\033[m \033[34mé de \033[m\033[1;33m{tm.text}°C\033[m')
                print(f'\033[1;33m> {g.upper()}\033[m')
                print("=="*20)
                browser.close()
                ach = False
    if per in rest:
        while True:
            permis = True
            site = False
            cab('RESTAURANTES')
            lugar = str(input('\033[1;33m> \033[m\033[1;34mDIGITE O LOCAL: \033[m'))
            print("-" * 40)
            print("\033[1;33mCOLETANDO INFORMARÇÕES...\033[m")
            print("-" * 40)
            browser = Chrome()
            browser.get(
                'https://www.google.com/search?q=restaurantes&oq=restaurantes+perdizes&aqs=chrome..69i57j0l7.10955j0j7&sourceid=chrome&ie=UTF-8')
            browser.minimize_window()
            sleep(1)
            loc = browser.find_element_by_name('q')
            t = loc.send_keys(f' {lugar}')
            loc.send_keys(Keys.RETURN)
            sleep(1)
            try:
                b = browser.find_elements_by_css_selector('[class="rllt__details lqhpac"]')
                nome = browser.find_elements_by_class_name('dbg0pd')
            except:
                print('\033[1;31mLOCAL NÃO ENCONTRADO!')
                print('DIGITE NOVAMENTE:\033[m')
                permis = False
            else:
                pass

            def rest(b, nome):
                try:
                    resta1 = b[0].text
                    resta1l = resta1.split()
                    print(f'\033[1;34mRESTAURANTE:\033[m \033[1;33m{nome[0].text}\033[m')
                    print(f'\033[1;34mAVALIAÇÃO:\033[1;33m {resta1l[0]}\033[m')
                    print(f'\033[1;34mRUA:\033[m \033[1;33m{resta1l[10]} {resta1l[11]}\033[m')
                    print('==' * 20)
                    # ==========================================================
                    resta2 = b[1].text
                    resta2l = resta2.split()
                    print(f'\033[1;34mRESTAURANTE: \033[m\033[1;33m{nome[1].text}\033[m')
                    print(f'\033[1;34mAVALIAÇÃO: \033[m\033[1;33m{resta2l[0]}\033[m')
                    print(f'\033[1;34mRUA: \033[m\033[1;33m{resta2l[10]} {resta2l[11]}\033[m')
                except:
                    print('\033[1;31mLOCAL NÃO ENCONTRADO!\033[m')
                else:
                    pass
            if permis == True:
                rest(b, nome)
                browser.close()
                break
    if per in idioma:
        site = False
        cab('TRADUZIR')
        print('\033[1;33m[1]>\033[m \033[1;34mTRADUZIR DO INGLES PARA PORTUGUES\033[m')
        print('\033[1;33m[2]>\033[m \033[1;34mTRADUZIR DO PORTUGUES PARA INGLES\033[m')
        print('--' * 20)
        while True:
            try:
                opi = int(input('\033[1;33mOPÇÃO: \033[m'))
            except:
                print('\033[1;31mOPÇÃO INVÁLIDA!')
                print('DIGITE NOVAMENTE:\033[m')
            else:
                break
        if opi not in [1,2]:
            while True:
                print('\033[1;31mOPÇÃO INVÁLIDA!')
                print('DIGITE NOVAMENTE:\033[m')
                opi = int(input('\033[1;33mOPÇÃO: \033[m'))

                if opi in [1,2]:
                    break

        if opi == 1:
            pal = str(input('\033[1;33m> \033[m\033[1;34mTRADUZIR: \033[m'))
            browser = Chrome()
            browser.minimize_window()
            browser.get(
                'https://www.google.com/search?sxsrf=ALeKk028vaFdhJHEK0Z1nukHrZ5M5lVNyg%3A1593114979788&ei=YwH1XorFL-rF5OUPlq-UoAg&q=google+tradutor&oq=google+tradutor&gs_lcp=CgZwc3ktYWIQAzIECCMQJzICCAAyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzoECAAQR1DECViJDmDND2gAcAF4AIABvwKIAb8CkgEDMy0xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjKgtPj353qAhXqIrkGHZYXBYQQ4dUDCAw&uact=5')

            sleep(0.5)
            fal1 = browser.find_element_by_id('tw-source-text-ta')
            fal1.send_keys(f'{pal}')
            sleep(1)
            tradu = browser.find_element_by_id('kAz1tf')
            print(f'\033[1;34mTRADUÇÃO: \033[m')
            txt = f'{tradu.text}'.split()
            for t in txt[0:len(txt) - 3]:
                print((f'\033[33;1m{t} '), end='')
            print('\033[m')
            browser.close()
        if opi == 2:
            pal = str(input('\033[1;33m> \033[m\033[1;34mTRADUZIR: \033[m'))
            browser = Chrome()
            browser.minimize_window()
            browser.get(
                'https://www.google.com/search?sxsrf=ALeKk028vaFdhJHEK0Z1nukHrZ5M5lVNyg%3A1593114979788&ei=YwH1XorFL-rF5OUPlq-UoAg&q=google+tradutor&oq=google+tradutor&gs_lcp=CgZwc3ktYWIQAzIECCMQJzICCAAyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzoECAAQR1DECViJDmDND2gAcAF4AIABvwKIAb8CkgEDMy0xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjKgtPj353qAhXqIrkGHZYXBYQQ4dUDCAw&uact=5')
            tro = browser.find_element_by_id('tw-swap').click()
            sleep(0.5)
            fal1 = browser.find_element_by_id('tw-source-text-ta')
            fal1.send_keys(f'{pal}')
            sleep(1)
            tradu = browser.find_element_by_id('kAz1tf')
            print(f'\033[1;34mTRADUÇÃO: \033[m')
            txt = f'{tradu.text}'.split()
            for t in txt[0:len(txt) - 3]:
                print((f'\033[33,1m{t} '), end='')
            print('\033[m')
            print(f'\033[1;34mTRADUÇÃO: \033[m\033[1;33m{tradu.text}\033[1;33m')
            browser.close()
        print('=='*20)
    if per in cono:
        site = False
        cab('CONOMETRO')
        most = 0
        print('\033[1;31m> PARA PARAR O ALARME FECHE A JANELA\033[m')
        print('\033[33;1mCONOMETRAR:\033[m')
        print('\033[1;33m[1]> \033[m\033[34;1mSEGUNDOS\033[m')
        print('\033[33;1m[2]> \033[m\033[34;1mMINUTOS\033[m')
        print('\033[33;1m[3]> \033[m\033[34;1mHORAS\033[m')
        print('--' * 20)
        while True:
            try:
                tempor = int(input('\033[1;33mOPÇÃO: \033[m'))
            except:
                print('\033[1;31mOPÇÃO INVÁLIDA!')
                print('DIGITE NOVAMENTE:\033[m')
            else:
                break
        if tempor not in [1, 2, 3]:
            while True:
                print('\033[1;31mOPÇÃO INVÁLIDA!')
                print('DIGITE NOVAMENTE:\033[m')
                opi = int(input('\033[1;33mOPÇÃO: \033[m'))

                if tempor in [1, 2, 3]:
                    break
        if tempor == 1:
            seg = int(input("\033[33;1m> \033[m\033[34;1mDIGITE QUANTOS SEGUNDOS: \033[m"))
            for t in range(0, seg + 1):
                sleep(1)
                if seg > 10:
                    if most == 5:
                        print((f'\033[31;1m{t}, '), end='')
                        most = 0
                if seg < 11:
                    print((f'\033[31;1m{t}, '), end='')
                most += 1
            print("\033[m")

        if tempor == 2:
            min = int(input('\033[33;1m> \033[m\033[34;1mDIGITE QUANTOS MINUTOS: \033[m'))
            seg1 = int(input("\033[33;1m> \033[m\033[34;1mDIGITE QUANTOS SEGUNDOS: \033[m"))
            temp1 = (min * 60) + seg1
            for t1 in range(0, temp1 + 1):
                sleep(1)
                if most == 5:
                    print((f'\033[31;1m{t1}, '), end='')
                    most = 0
                most += 1
            print('\033[m')

        if tempor == 3:
            hr = int(input('\033[33;1m> \033[m\033[34;1mDIGITE QUANTAS HORAS: \033[m'))
            min1 = int(input('\033[33;1m> \033[m\033[34;1mDIGITE QUANTOS MINUTOS: \033[m'))
            seg2 = int(input('\033[33;1m> \033[m\033[34;1mDIGITE QUANTOS SEGUNDOS: \033[m'))
            temp2 = (min1 * 60) + (3600 * hr) + seg2
            for t2 in range(0, temp2 + 1):
                sleep(1)
                if most == 5:
                    print((f'\033[31;1m{t2}, '), end='')
                    most = 0
                most += 1
            print('\033[m')
        print('\033[1;31m> PARA PARAR O ALARME FECHE A JANELA\033[m')
        try:
            browser = Chrome()
            browser.get('https://pt.pikbest.com/sound-effects/alarm-ringtone-sounds-quickly_1209196.html')
            bttn = browser.find_element_by_class_name('audio-btn').click()
            rep = browser.find_element_by_class_name('audio-replay')
            while most != 99999999999999999999999999999999999:
                sleep(8)
                rep.click()
        except:
            pass
        else:
            pass
        print('=='*20)
    if per in dicionario:
        site = False
        cab('DICIONARIO')
        sig = str(input("\033[33;1m> \033[m\033[34;1mDIGITE A PALAVRA: \033[m"))
        try:
            browser = Chrome()
            browser.get('https://www.dicio.com.br/')
            browser.minimize_window()
            h = 0
            pal = browser.find_element_by_name('q')
            pal.send_keys(f'{sig}')
            pal.send_keys(Keys.RETURN)
            sleep(0.3)
            div = browser.find_element_by_id('content')
            span = div.find_elements_by_tag_name('span')
            ro = span[5].text.split(':')
            print(f'\033[34;1m> SIGNIFICADO:\033[m \033[33;1m{ro[0]}\033[m')
            browser.close()
            print('==' * 20)
        except:
            print(f'\033[31;1mNÃO FOI POSSIVEL ACHAR UM SIGNIFICADO PARA "{sig}"\033[m')
        else:
            pass
    if per in mensagem:
        cab('MENSAGEM')
        site = False
        username = str(input('\033[33;1m> \033[m\033[34;1mDIGITE O NOME DO USUARIO: \033[m'))
        msgr = str(input('\033[33;1m> \033[m\033[34;1mDIGITE A MENSAGEM: \033[m'))
        browser = Chrome()
        browser.get('https://www.instagram.com/?hl=pt-br')
        sleep(1)
        user = browser.find_element_by_name('username')
        user.send_keys('python_farm')
        sen = browser.find_element_by_name('password')
        sen.send_keys('sempre190')
        sen.send_keys(Keys.RETURN)
        sleep(3)
        browser.get('https://www.instagram.com/direct/inbox/')
        sleep(1)
        an = browser.find_element_by_css_selector('[class = "aOOlW   HoLwm "]').click()
        browser.minimize_window()
        sleep(1)
        yu = browser.find_elements_by_css_selector(
            '[class = "_7UhW9   xLCgt      MMzan  KV-D4             fDxYl     "]')
        try:
            u = ''
            yu = browser.find_elements_by_css_selector(
                '[class = "_7UhW9   xLCgt      MMzan  KV-D4             fDxYl     "]')
            for u in yu:
                ty = u.text
                if ty == username:
                    u.click()
                    go = browser.find_element_by_css_selector('[class = "X3a-9"]')
                    ui = go.find_element_by_tag_name('textarea')
                    sleep(1)
                    ui.send_keys(f'{msgr}')
                    ui.send_keys(Keys.RETURN)
                    break
                else:
                    print('\033[31;1mNOME DE USUARIO NÃO ENCONTRADO\033[m')
                    break
        except:
            pass
        else:
            pass
    if per in senha:
        opo = [1, 2, 3]


        def linha(a='=', b=40):
            print(a * b)


        def cab(a):
            linha()
            print(f'\033[1;35m{a}\033[m'.center(47))
            linha()


        def cri(nome):
            try:
                a = open(nome, 'wt+')
                a.close()
            except:
                print('\033[1;31mERRO! Não foi possivél criar um arquivo!\033[m')
            else:
                print('\033[1;32mArquivo criado com SUCESSO!\033[m')


        def ex(nome):
            try:
                a = open(nome, 'rt')
                a.close()
            except FileNotFoundError:
                return False
            else:
                return True


        def cada(ar, sen, id=0):
            try:
                a = open(ar, 'at')
            except:
                print('Houve um problema para abrir o arquivo!')
            else:
                a.write(f'{sen}')
                a.close()


        def lar(arq):
            while True:
                cab('MENU DO USUARIO')
                print('\033[1;33m1>\033[m \033[1;34mVER SENHAS\033[m')
                print('\033[1;33m2>\033[m \033[1;34mCADASTRAR SENHA\033[m')
                print('\033[1;33m3>\033[m \033[1;34mSAIR\033[m')
                opi = int(input('\033[1;33mOPÇÃO: \033[m'))
                if opi not in opo:
                    print('\033[1;31mOPÇÃO INVALIDA\033[m')
                else:
                    if opi == 1:
                        linha('-')
                        print('\033[1;32mSENHAS:\033[m')
                        try:
                            c = open(arq, 'rt')
                        except:
                            print('Erro ao ler o arquivo! ')
                        else:
                            print(c.read())
                            c.close()

                    if opi == 2:
                        cab('NOVA SENHA')
                        ser = str(input('\033[1;33m>\033[m \033[1;34mSERVIÇO: \033[m'))
                        usa = str(input('\033[1;33m>\033[m \033[1;34mNOME DE USUARIO: \033[m'))
                        pah = str(input('\033[1;33m>\033[m \033[1;34mSENHA: \033[m'))
                        try:
                            c = open(arq, 'at')
                        except:
                            print('Erro ao ler o arquivo! ')
                        else:
                            c.write(f'\nSERVICO: {ser}, NOME DE USUARIO: {usa}, SENHA: {pah} ')
                            c.close()
                    if opi == 3:
                        break
        op = [1, 2, 3]
        blok = 0
        while True:
            cab('GERENCIADOR DE SENHAS')
            print('\033[1;33m1>\033[m \033[1;34mLOGIN\033[m')
            print('\033[1;33m2>\033[m \033[1;34mNOVO CADASTRO\033[m')
            print('\033[1;33m3>\033[m \033[1;34mSAIR\033[m')
            linha()
            opi = int(input('\033[1;33mOPÇÃO: \033[m'))
            if opi not in op:
                print('\033[1;31mOPÇÃO INVALIDA!\033[m')
            if opi == 2:
                while True:
                    cab('CADASTRO')
                    cu = str(input('\033[1;33m>\033[m \033[1;34mDIGITE O NOME DE USUARIO: \033[m'))
                    cs = str(input('\033[1;33m>\033[m \033[1;34mDIGTE UMA SENHA: \033[m'))
                    if not ex(f'{cu}.txt'):
                        cri(f'{cu}.txt')
                        cada(f'{cu}.txt', cs)
                        print('\033[1;32mUSUARIO CRIADO COM SUCESSO!\033[m')
                        break
                    if ex(f'{cu}.txt'):
                        print("\033[1;31mNOME DE USUARIO INVALIDO!")
                        print('DIGITE OUTRO:\033[m')
            if opi == 3:
                print('\033[1;31mSISTEMA FINALIZADO!\033[m')
                break
            if opi == 1:
                while True:
                    cab('LOGIN')
                    id = str(input('\033[1;33m> \033[m\033[1;34mDIGITE O NOME DE ÚSUARIO: \033[m'))
                    pas = str(input('\033[1;33m> \033[m\033[1;34mDIGITE O A SENHA: \033[m'))
                    try:
                        a = open(f'{id}.txt', 'rt')
                    except:
                        linha()
                        blok += 1
                        print('\033[1;31mERRO: USUARIO NÃO ENCONTRADO!\033[m')
                    else:
                        rnh = a.readline().strip()
                        if f'{rnh}' == f'{pas}':
                            lar(f'{id}.txt')
                            break
                        else:
                            blok += 1
                            print('\033[1;31mERRO: SENHA INCORRETA\033[m')
                    if blok == 3:
                        print('\033[1;31mAÇÕES BLOQUEADAS POR 1min!\033[m')
                        blok = 0
                        sleep(60)
    if per in sair:
        site = False
        print('\033[31;1mPROGRAMA FINALIZADO\033[m')
        break
    if per == '01100100 01100101 01100011 01101111':
        site = False
        print('\033[1;32m01000100 01000101 01000011 01001111 00100000 01010001 01010101 01000101 00100000 01001101 01000101 00100000 01000100 01000101 01010011 01000101 01001110 01010110 01001111 01001100 01010110 01000101 01010101\033[m')
    if site:
        print('\033[1;31mDESCULPE, NÃO CONSEGUI IDENTIFICAR SUA PERGUNTA!\033[m')
