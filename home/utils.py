

def menssagens(alert, msg, username='', email='', btn=0):
    contexto = {}

    if int(len(msg) > 3):
        contexto = {'alert': alert, 'msg': msg, 'username': username, 'email': email, 'btn': btn, 'msgv': 1}

        return contexto
    else:
        contexto['msgv'] = 0
        return contexto




