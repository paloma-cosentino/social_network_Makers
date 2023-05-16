from lib.users_repo import *
from lib.users import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepo(db_connection)
    result = repository.all()
    assert result == [
        SocialNetworkUsers(1, 'henry@email', 'henry', 'hello world')
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepo(db_connection)
    result = repository.find(1)
    assert result == SocialNetworkUsers(1, 'henry@email', 'henry', 'hello world')

