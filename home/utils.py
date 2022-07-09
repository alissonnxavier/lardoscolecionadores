

def menssagens(alert, msg):

    global contexto

    if int(len(msg) > 3):
        contexto = {'alert': alert, 'msg': msg, 'msgv': 1}

        return contexto
    else:
        contexto['msgv'] = 0


def sumform(usuario, email, senha1, senha2):
    contexto['usuario'] = usuario
    contexto['email'] = email
    contexto['senha1'] = senha1
    contexto['senha2'] = senha2


