criarquivo = open('times.txt' , 'a')
criarquivo.close()

winner = 0

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

def atualizar_placar():
    soma_time1 = 0
    soma_time2 = 0
    soma_usuario_time1 = 0
    soma_usuario_time2 = 0

    time = show_file('times.txt')
    usuario = show_file('usuarios.txt')

    time1 = find_file('id_time', '1', 'times.txt')
    time2 = find_file('id_time', '2', 'times.txt')

    time1_atual = find_file('id_time', "1", 'times.txt')
    time2_atual = find_file('id_time', '2', 'times.txt')


    # Soma time
    for pontuacao in time:

        if pontuacao['id_time'] == '1':
            soma_time1 = soma_time1 + pontuacao['pontuacao']
            time1_id = pontuacao['id_time']


        if pontuacao['id_time'] == '2':
            soma_time2 = soma_time2 + pontuacao['pontuacao']
            time2_id = pontuacao['id_time']

    # Soma ponto
    for ponto in usuario:
        if ponto['time'] == time1_id:
            soma_usuario_time1 = soma_usuario_time1 + ponto['pontuacao']
        if ponto['time'] == time2_id:
            soma_usuario_time2 = soma_usuario_time2 + ponto['pontuacao']

    if soma_time1 == soma_usuario_time1:
        print("Pontuação time 1 não houve alteração")
    else:
        soma_time1 = soma_usuario_time1
        time1['pontuacao'] = soma_time1
        edit_file('id_time', time1_id, time1, 'times.txt')

    if soma_time2 == soma_usuario_time2:
        print("Pontuação do time 2 não houve alteração")
    else:
        soma_time2 = soma_usuario_time2
        time2['pontuacao'] = soma_time2

        edit_file('id_time', time2_id, time2, 'times.txt')

    print("** Atualização feita com sucesso **\n")


while True:
    print("Gerenciamento de times")
    print("1 - Criar times")
    print("2 - Atualizar placar")
    print("3 - EndGame")
    print("4 - Zerar pontuação dos usuários")
    print("0 - Sair")
    escolha = int(input("Digite uma das opções acima: "))



    if escolha == 1:
        print(" ** Criar Time ** ")
        nome_time = input("Digite o nome do time: ")
        id_time = input("1 ou 2 ? ")
        pontuacao_inicial = 0

        time = {
            'nome_time': nome_time,
            'id_time': id_time,
            'pontuacao': pontuacao_inicial
        }

        insert_file(time, 'times.txt')

        print(" ** TIME CADASTRADO ** ")

    if escolha == 2:
        atualizar_placar()

    if escolha == 3:

        atualizar_placar()
        time1 = find_file('id_time' , '1' , 'times.txt')
        time2 = find_file('id_time' , '2' , 'times.txt')
        if time1['pontuacao'] > time2['pontuacao']:
            print('O vencedor foi o time {}'.format(time1['nome_time']))
            print('-=-' * 30)
            print('\n')

        elif time1['pontuacao'] < time2['pontuacao']:
            print('O vencedor foi o time {}'.format(time2['nome_time']))
            print('-=-' * 30)
            print('\n')

        else:
            print('Eita! Empate!')
            print('-=-' * 30)
            print('\n')

        print("** Para iniciar um novo jogo digite o nome dos dois novos times **")
        nome_time_1 = input("Digite o nome do novo time 1: ")
        nome_time_2 = input("Digite o nome do novo time 2: ")

        time1 = find_file('id_time', '1', 'times.txt')
        time2 = find_file('id_time', '2', 'times.txt')

        remover_file('id_time', time1['id_time'], 'times.txt')
        novo_time1 = {
            'nome_time': nome_time_1,
            'id_time': '1',
            'pontuacao': 0
        }
        insert_file(novo_time1, 'times.txt')

        remover_file('id_time', time2['id_time'], 'times.txt')

        novo_time2 = {
            'nome_time': nome_time_2,
            'id_time': '2',
            'pontuacao': 0
        }

        insert_file(novo_time2, 'times.txt')

        usuarios = show_file('usuarios.txt')

        for usuario in usuarios:
            id_usuario = usuario['id']
            usuario['pontuacao'] = 0
            edit_file('id', id_usuario, 'pontuacao', 'usuarios.txt')

    if escolha == 4:
        print("*****")
        usuarios = show_file('usuarios.txt')

        for usuario in usuarios:
            id_usuario = usuario['id']
            usuario['pontuacao'] = 0
            edit_file('id', id_usuario, usuario, 'usuarios.txt')

    if escolha == 0:
        break