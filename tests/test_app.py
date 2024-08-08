from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@teste.com',
            'password': '123456',
        },
    )
    #  voltou 201 o status code correto?
    assert response.status_code == HTTPStatus.CREATED  # 201
    #  Validar UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'testeusername',
        'email': 'teste@teste.com',
    }


def test_read_users(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {'username': 'testeusername', 'email': 'teste@teste.com', 'id': 1}
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testeusername',
        'email': 'teste@teste.com',
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testeusername2',
            'email': 'teste2@teste.com',
            'id': 1,
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testeusername2',
        'email': 'teste2@teste.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Eu',
            'email': 'eu2@teste.com',
            'password': '212121',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
