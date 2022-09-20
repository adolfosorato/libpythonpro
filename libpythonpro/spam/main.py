class EnviadorDeSpam:
    def __init__(self, sessao: object, enviador: object) -> object:
        self.enviador = enviador
        self.sessao = sessao

    def enviar_emails(self, remetente, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                usuario.email,
                assunto,
                corpo
            )
