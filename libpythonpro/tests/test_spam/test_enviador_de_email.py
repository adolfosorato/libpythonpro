import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['adolfosorato@gmail.com', 'andersonsorato@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['adolfosorato@gmail.com', 'andersonsorato@hotmail.com']
    destinatario
    resultado = enviador.enviar(
        destinatario,
        'adolfosorato@outlook.com',
        'Curso Python Pro',
        'Turma Erle Carrara aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'adolfosorato']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'adolfosorato@outlook.com',
            'Curso Python Pro',
            'Turma Erle Carrara aberta.'
        )
