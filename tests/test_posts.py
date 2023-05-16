from lib.posts import *

def test_recipe_constructs():
    posts = SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5)
    assert posts.id == 1
    assert posts.post_title == 'Monday'
    assert posts.post_content == 'hello world'
    assert posts.post_read == 'emily'
    assert posts.post_viewed == 5

def test_posts_equal_function():
    post1 = SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5)
    post2 = SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5)
    assert  post1 == post2

def test_posts_format_nicely():
    posts = SocialNetworkPosts(1, 'Monday', 'hello world', 'emily', 5)
    assert str(posts) == "Posts(1, Monday, hello world, emily, 5)"