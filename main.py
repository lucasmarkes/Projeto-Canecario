opcao_info = 0
opcao = 0

descartado = open('descartaveis.txt' , 'a')
descartado.close()

def insert_file(objeto, name_file):

    import simplejson

    # Reading file
    try:
        f = open(name_file, 'r')

        filecontents = simplejson.load(f)
    except:
        filecontents = []
    finally:
        # Close file
        f.close()

    # Writing file
    try:
        f = open(name_file, 'w')
        filecontents.append(objeto)
        simplejson.dump(filecontents, f)

    except:
        print('...')


    finally:
        # Close file
        f.close()


def edit_file(find_column, pesq, edit_row, name_file):

    import simplejson

    # Reading file
    try:
        f = open(name_file, 'r')
        filecontents = simplejson.load(f)


        cont = 0
        for row in filecontents:

            if row[find_column] == pesq:
                filecontents[cont] = edit_row
                break

            cont += 1

    except:
        filecontents = []
    finally:
        # Close file
        f.close()


    # Writing file
    try:
        f = open(name_file, 'w')

        simplejson.dump(filecontents, f)

    except:
        print('...')
    finally:
        # Close file
        f.close()


def remover_file(find_column, pesq, name_file):

    import simplejson

    # Reading file
    try:
        f = open(name_file, 'r')
        filecontents = simplejson.load(f)


        cont = 0
        for row in filecontents:

            if row[find_column] == pesq:

                del filecontents[cont]

                break

            cont += 1

    except:
        filecontents = []
    finally:
        # Close file
        f.close()


    # Writing file
    try:
        f = open(name_file, 'w')

        if len(filecontents) == 0:
            filecontents = None

        simplejson.dump(filecontents, f)

    except:
        print('...')
    finally:
        # Close file
        f.close()



def find_file(name_column, pesq, name_file):

    import simplejson

    result = None

    # Reading file
    try:
        f = open(name_file, 'r')
        filecontents = simplejson.load(f)

        for row in filecontents:
            value = row[name_column]

            if value == pesq:
                # object found
                result = row

    except:
        print('...')
    finally:
        # Close file
        f.close()


    return result

def show_file(name_file):

    import simplejson

    result = None

    # Reading file
    try:
        f = open(name_file, 'r')
        result = simplejson.load(f)

    except:
        print('...')
    finally:
        # Close file
        f.close()

    return result

def level():
    usuarios = show_file('usuarios.txt')
    for usuario in usuarios:
        id = usuario['id']
        xp = usuario['exp']
        level = int(int(xp) / 1000)
        usuario['level'] = level
        edit_file('id' , id , usuario , 'usuarios.txt')

def cont_descartaveis():
    descartavel = find_file('id', 1, 'descartaveis.txt')

    descartavel_atual = descartavel['descartavel']

    i = descartavel['descartavel'] + 1
    descartavel['descartavel'] = i
    edit_file('descartavel', descartavel_atual, descartavel, 'descartaveis.txt')

criarquivo = open('usuarios.txt' , 'a')
criarquivo.close()

while opcao != -1:

    # INTRODUÇÃO
    print("\n" * 2)
    print("=-" * 30)
    print("|", " " * 16, "BEM VINDO AO CANNECT", " " * 17, "|")
    print("=-" * 30)
    print("\n1 - CANNECTAR")
    print("2 - Informações")
    print("3 - Registrar Usuário")
    print("-1 - Para finalizar o programa\n")

    opcao = int(input("Escolhe uma das opções acima: "))

    if opcao == 1: # Será opcao == 1
        print("Área de login")
        login_usuário = input("Digite seu ID ou email: ")

        usuario = find_file('id', login_usuário, 'usuarios.txt')


        if usuario is None:
            print('\n** Usuário não encontrado **')
            print('Faça o cadastro se ainda não estiver cadastrado\n')

        else:
            print(" ** Bem-vindo ao Cannect, {} !! ** ".format(usuario['nome']))

            # First Page
            opcao_login = -1
            while opcao_login != 0:

                caneca_atual = usuario['caneca']
                teste2 = open('canecas.txt', 'a')
                teste2.close()
                caneca = find_file('mug_num', caneca_atual, 'canecas.txt')

                print("O que deseja fazer ?\n")
                print("1 - Pegar caneca")
                print("2 - Devolver caneca")
                print("3 - Report")
                print("4 - Meu perfil")
                print("5 - Placar dos times")
                print("6 - Ver descartáveis não utilizados")
                print("7 - Leaderboards")
                print("0 - Descannectar")
                opcao_login = int(input("Escolha uma das opções acima: "))

                if opcao_login == 1:

                    if usuario['caneca'] is None:
                        while True:
                            num_caneca = input("\nDigite a numeração da caneca: ")
                            caneca = find_file('mug_num', num_caneca, 'canecas.txt')

                            caneca_atual = num_caneca
                            usuario_atual = usuario['id']

                            if caneca is None:
                                print(" ** Caneca não foi encontrada **")
                                print("Tente outra\n")
                                continue

                            if caneca['mug_state'] == "Dirty":
                                print("** Caneca reportada como SUJA **")
                                decisao = int(input("Digite 1 para pegar\n Digite -1 para pegar outra: "))

                                if decisao == 1:
                                    print("** Lembre-se que ela está suja, lave a caneca antes do uso **")
                                    caneca['disp'] = 'indisponivel'
                                    usuario['caneca'] = num_caneca
                                    break

                                if decisao == -1:
                                    continue

                            if caneca['mug_state'] == "Broken":
                                print(" ** Caneca Reportada como quebrada ** ")
                                decisao = int(input("Digite 1 se ela de fato estiver quebrada\n"
                                                    " ou -1 se não estiver quebrada: "))

                                if decisao == 1:
                                    print(" ** Tente pegar outra caneca ** ")
                                    continue

                                if decisao == -1:
                                    print(" ** Você pegou essa caneca ** ")
                                    caneca['disp'] = 'indisponivel'
                                    usuario['caneca'] = num_caneca
                                    break

                            if caneca['mug_state'] == "Lost":
                                print(" ** Essa caneca foi reportada como perdida **")
                                decisao = int(input("Digite 1 se ela de fato estiver perdida\n"
                                                    "ou -1 se não estiver quebrada"))

                                if decisao == 1:
                                    print(" ** Tente pegar outra caneca ** ")
                                    continue
                                if decisao == -1:
                                    print(" ** Você pegou essa caneca ** ")
                                    caneca['disp'] = 'indisponivel'
                                    usuario['caneca'] = num_caneca

                                    break

                            if caneca['disp'] == 'indisponivel':
                                print(" ** Essa caneca está em uso, tente outra ** ")
                                continue

                            else:
                                print(" ** Você pegou essa caneca ** ")
                                caneca['disp'] = 'indisponivel'
                                usuario['caneca'] = num_caneca
                                break

                            edit_file('mug_num', caneca_atual, caneca, 'canecas.txt')
                            edit_file('id', usuario_atual, usuario, 'usuarios.txt')

                    else:
                        print("** Você já está com a caneca {} ** ".format(usuario['caneca']))
                        print("Para pegar outra você deve devolver-la\n")


                    cont_descartaveis()


                if opcao_login == 2:
                    if usuario['caneca'] is not None:
                        print("DEVOLVER CANECA")
                        print("Após o usuário escanear o QR code na pia")

                        decisao_limpeza = input("Você lavou a caneca {} (Digite s ou n) ? ".format(usuario['caneca']))


                        usuario_atual = usuario['id']
                        caneca_atual = usuario['caneca']

                        if decisao_limpeza == 's':

                            print(" ** Você devolveu a caneca, Obrigado :D **")
                            print("Você recebeu 100 CP/XP pela sua boa conduta\n")

                            ponto_acumulativo = usuario['pontuacao'] + 100
                            XP_acumulativo = usuario['exp'] + 100

                            usuario['caneca'] = None
                            caneca['disp'] = 'disponivel'
                            usuario['pontuacao'] = ponto_acumulativo
                            usuario['exp'] = XP_acumulativo
                            caneca['mug_state'] = "Clean"

                        if decisao_limpeza == 'n':
                            decisao_final = input("Você deseja devolver a caneca {} mesmo suja (Digite s ou n) ?"
                                                  .format(usuario['caneca']))
                            if decisao_final == 's':
                                print("** Que pena :(, você não pôde lavar a caneca, por favor, deixe-a no devido lugar **")
                                print("Infelizmente você perderá 50 CP/XP por isso\n")

                                ponto_acumulativo = usuario['pontuacao'] - 50
                                XP_acumulativo = usuario['exp'] - 50

                                usuario['caneca'] = None
                                caneca['disp'] = "disponivel"
                                usuario['pontuacao'] = ponto_acumulativo
                                usuario['exp'] = XP_acumulativo
                                caneca['mug_state'] = "Dirty"

                        edit_file('id', usuario_atual, usuario, 'usuarios.txt')
                        edit_file('mug_num', caneca_atual, caneca, 'canecas.txt')
                    if usuario['caneca'] is None:
                        print('Para escolher essa opção, você precisa primeiro pegar uma caneca!')


                opcao_report = 0
                if opcao_login == 3:
                    while opcao_report != -1:
                        print("ÁREA DE REPORT")
                        print("1 - Caneca suja")
                        print("2 - Caneca perdida")
                        print("3 - Caneca quebrada")
                        print("\n-1 - Para voltar")

                        opcao_report = int(input("Que tipo de problema deseja reportar ? "))
                        if opcao_report != -1:
                            num_caneca = input("Digite a numeração da caneca que deseja reportar: ")

                            caneca = find_file('mug_num', num_caneca, 'canecas.txt')

                            if caneca is None:
                                print("** Caneca não encontrada **")

                            else:


                                caneca_antiga = caneca['mug_num']
                                usuario_atual = usuario['id']

                                if opcao_report == 1:
                                    print("O CANNECT agradece o seu report :D")
                                    print("{}, você recebeu 50 CP pelo report".format(usuario['nome']))

                                    ponto_acumulativo = usuario['pontuacao'] + 50
                                    XP_acumulativo = usuario['exp'] + 50

                                    caneca['mug_state'] = "Dirty"
                                    usuario['pontuacao'] = ponto_acumulativo
                                    usuario['exp'] = XP_acumulativo

                                if opcao_report == 2:
                                    print("O CANNECT agradece o seu report :D")
                                    print("{}, você recebeu 50 CP pelo report".format(usuario['nome']))

                                    ponto_acumulativo = usuario['pontuacao'] + 50
                                    XP_acumulativo = usuario['exp'] + 50

                                    caneca['mug_state'] = "Lost"
                                    usuario['pontuacao'] = ponto_acumulativo
                                    usuario['exp'] = XP_acumulativo

                                if opcao_report == 3:
                                    print("O CANNECT agradece o seu report :D")
                                    print("{}, você recebeu 50 CP pelo report".format(usuario['nome']))

                                    ponto_acumulativo = usuario['pontuacao'] + 50
                                    XP_acumulativo = usuario['exp'] + 50

                                    caneca['mug_state'] = "Broken"
                                    usuario['pontuacao'] = ponto_acumulativo
                                    usuario['exp'] = XP_acumulativo

                                edit_file('id', usuario_atual, usuario, 'usuarios.txt')
                                edit_file('mug_num', caneca_antiga, caneca, 'canecas.txt')
                                level()

                if opcao_login == 4:
                    print("Seu perfil")
                    print("Nome: {}".format(usuario['nome']))
                    print("ID ou email: {}".format(usuario['id']))

                    if usuario['time'] == 1:
                        time = 'Gato'

                    if usuario['time'] == 2:
                        time = 'Cachorro'

                    print("Time: {}".format(usuario['time']))
                    print("CP: {}".format(usuario['pontuacao']))

                    if usuario['caneca'] is None:
                        caneca = "Você não pegou nenhuma caneca"
                    else:
                        caneca = usuario['caneca']

                    print("Caneca atual: {}".format(caneca))
                    xp = usuario['exp']
                    print("XP: {}" .format(xp))
                    user = usuario['level']
                    print("Level: {}" .format(user))  # level inteiro

                if opcao_login == 5:

                    times = show_file('times.txt')

                    for time in times:
                        time_atual = time['nome_time']
                        print("{}: {}".format(time_atual, time['pontuacao']))

                if opcao_login == 6:
                    descartavel = find_file('id', 1, 'descartaveis.txt')
                    total_descartavel = descartavel['descartavel']

                    print("\n** Total de descartáveis não utilizados: {} **\n".format(total_descartavel))

                if opcao_login == 7:
                    while True:
                        print("1 - LeaderBoard de Level")
                        print("2 - LeaderBoard de Pontos")
                        print("0 - Voltar")

                        escolha = int(input("Escolha qual LeaderBoard deseja visualizar: "))
                        if escolha == 1:
                            print("LEADERBOARD LEVEL")
                            level()

                            unsorted_list = show_file('usuarios.txt')

                            sorted_list = sorted(unsorted_list, key=lambda k: k['exp'], reverse=True)

                            i = 1
                            print("-" * 30)
                            print("**(TOP 50)**\n")
                            for pontuacao in sorted_list:

                                print("{}. {} / LEVEL: {} / XP: {}".format(i, pontuacao['nome'], pontuacao['level'], pontuacao['exp']))
                                i += 1
                                if i == 51:
                                    break

                            print("-" * 30)
                            print("\n")

                        if escolha == 2:
                            print("LEADERBOARD DE PONTUAÇÃO")
                            unsorted_list = show_file('usuarios.txt')

                            sorted_list = sorted(unsorted_list, key=lambda k: k['pontuacao'], reverse=True)

                            i = 1
                            print("-" * 30)
                            print("**(TOP 50)**\n")
                            for pontuacao in sorted_list:

                                print("{}. {} / CP: {}".format(i, pontuacao['nome'], pontuacao['pontuacao']))
                                i += 1
                                if i == 51:
                                    break

                            print("-" * 30)
                            print("\n")

                        else:
                            break



    if opcao == 2:

        while opcao_info != -1:

            print("1 - COMO DOAR CANECAS")
            print("2 - COMO USAR O CANECÁRIO")
            print("3 - COMO USAR O SITE")
            print("4 - JOGO DA VEZ")
            print("OU -1 para finalizar")

            opcao_info = int(input("Escolha a informação que você deseja consultar ou -1 para finalizar: "))

            if opcao_info == 1:
                print("Texto 1")

            elif opcao_info == 2:
                print("Texto 2")

            elif opcao_info == 3:
                print("Texto 3")

            elif opcao_info == 4:
                print("Texto 4")

            else:
                print("OPÇÃO INVÁLIDA")

        print("\nConsulta de informações concluída")

    # 3 CONCLUIDO
    elif opcao == 3:
        print("\n" * 2)
        print("=-" * 30)
        print("|", " " * 18, "ÁREA DE CADASTRO", " " * 19, "|")
        print("=-" * 30)

        criar = open('usuarios.txt' , 'a')
        criar.close()

        nome = input("Digite seu nome: ")

        time = input("Qual seu time? Digite 1 para a Gato ou 2 para Cachorro: ")

        validacao_nome = nome.isalpha()
        pontuacao = 0
        XP = 0

        while True:
            teste = open('usuarios.txt' , 'a')
            teste.close()
            ID = input("Digite seu ID ou email CESAR (será usado como login): ")

            usuario = show_file('usuarios.txt')
            id_verificar = find_file('id', ID, 'usuarios.txt')

            if id_verificar is None:
                break

            else:
                print("** ID ou email já existente **")

        if not validacao_nome:
            print("O NOME DEVE HAVER APENAS CARACTERES, TENTE NOVAMENTE")
            nome = input("Digite seu nome: ")
            validacao_nome = nome.isalpha()

        while time != '1' and time != '2':
            print("DIGITE UM TIME VÁLIDO, TENTE NOVAMENTE")
            time = input("Qual seu time ? (1 para Gato ou 2 para Cachorro): ")

        usuario = {
            'id': ID,
            'nome': nome,
            'time': time,
            'pontuacao': pontuacao,
            'exp': XP,
            'caneca': None,
            'level': 0
        }

        insert_file(usuario, 'usuarios.txt')

        print("USUARIO REGISTRADO COM SUCESSO")

level()

print("\n" * 2)
print("=-" * 30)
print("|", " " * 8, "OBRIGADO PELA SUA PRESENÇA NO CANNECT", " " * 8, "|")
print("=-" * 30)
