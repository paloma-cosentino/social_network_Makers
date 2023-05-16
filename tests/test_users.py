from lib.users import *

def test_recipe_constructs():
    users = SocialNetworkUsers(1, 'henry@email', 'henry', 'hello world')
    assert users.id == 1
    assert users.user_account == 'henry@email'
    assert users.user_name == 'henry'
    assert users.user_post == 'hello world'

def test_users_equal_function():
    user1 = SocialNetworkUsers(1, 'henry@email', 'henry', 'hello world')
    user2 = SocialNetworkUsers(1, 'henry@email', 'henry', 'hello world')
    assert  user1 == user2


def test_users_format_nicely():
    users = SocialNetworkUsers(1, 'henry@email', 'henry', 'hello world')
    assert str(users) == "Users(1, henry@email, henry, hello world)"
