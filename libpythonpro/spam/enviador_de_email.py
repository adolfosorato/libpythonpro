class Enviador:
    def enviar(self, remetente, destiantario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'E-mail de remetente inválido{remetente}')
        return remetente


class EmailInvalido(Exception):
    pass