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

def cont_descartes():
    descartavel = {
        "id": 1,
        "descartavel": 0
    }
    insert_file(descartavel, 'descartaveis.txt')

caneca = open('canecas.txt' , 'a')
caneca.close()

criarquivo = open('descartaveis.txt' , 'a')
criarquivo.close()

check = show_file('descartaveis.txt')

if check is None:
    cont_descartes()

print("** MÓDULO FEITO PARA ADICIONAR CANECAS NO SISTEMA")
while True:
    try:
        manipulador = show_file('canecas.txt')
        num_canecas = len(manipulador)
        print("A última registrada caneca é a: {}".format(num_canecas))

    except TypeError:
        print('Nenhuma caneca foi registrada ainda!')

    mug_num = input("Digite o número da caneca ou -1 para finalizar: ")
    if mug_num == "-1":
        break
    print("1 - Clean")
    print("2 - Dirty")
    print("3 - Broken")
    print("4 - Lost")

    while True:
        mug_state = int(input("Digite o status da caneca: "))

        if mug_state == 1:
            mug_state = "Clean"
            break

        if mug_state == 2:
            mug_state = "Dirty"
            break

        if mug_state == 3:
            mug_state = "Broken"
            break

        if mug_state == 4:
            mug_state = "Lost"
            break

        else:
            print("** Código inválido **")
            continue

    while True:
        disp = int(input("Digite 1 para disponível ou 0 para indisponível: "))

        if disp == 1:
            disp = 'disponivel'
            break

        if disp == 0:
            disp = 'indisponivel'
            break

        else:
            print(" ** Código Inválido ** ")
            continue



    caneca = {
        'mug_num': mug_num,
        'mug_state': mug_state,
        'disp': disp
    }

    caneca = insert_file(caneca, 'canecas.txt')
    print("\n** Caneca Cadastrada ** \n")