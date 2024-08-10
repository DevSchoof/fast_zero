from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='testeusername',
        email='teste@teste.com',
        password='Senha_bizurada',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'teste@teste.com')
    )
    assert result.id == 1
