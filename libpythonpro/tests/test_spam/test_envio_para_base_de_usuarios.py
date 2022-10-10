from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Adolfo', email='adolfosorato@gmail.com'),
            Usuario(nome='Anderson', email='adolfosorato@gmail.com')
        ],
        [
            Usuario(nome='Adolfo', email='adolfosorato@gmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
         'adolfosorato@gmail.com',
         'Curso python Pro',
         'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
        usuario = Usuario(nome='Adolfo', email='adolfosorato@gmail.com')
        sessao.salvar(usuario)
        enviador = Mock()
        enviador_de_spam = EnviadorDeSpam(sessao, enviador)
        enviador_de_spam.enviar_emails(
            'adolfosorato@outlook.com',
            'Curso python Pro',
            'Confira os módulos fantásticos'
        )
        enviador.enviar.assert_called_once_with(
            'adolfosorato@outlook.com',
            'adolfosorato@gmail.com',
            'Curso python Pro',
            'Confira os módulos fantásticos'
        )
