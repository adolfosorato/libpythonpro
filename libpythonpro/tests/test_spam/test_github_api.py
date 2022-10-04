from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value={
        'login': 'adolfosorato',
        'id': 111198921,
        'avatar_url': 'https://avatars.githubusercontent.com/u/111198921?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('adolfosorato')
    assert 'https://avatars.githubusercontent.com/u/111198921?v=4' == url
