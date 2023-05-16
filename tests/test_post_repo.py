from lib.posts_repo import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepo(db_connection)
    result = repository.all()
    assert result == [
        SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepo(db_connection)
    result = repository.find(1)
    assert result == SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5)

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepo(db_connection)
    repository.create(SocialNetworkPosts(None, "Tuesday", "content", "henry", 7))
    result = repository.all()
    assert result == [
        SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5),
        SocialNetworkPosts(2, "Tuesday", "content", "henry", 7)
    ]