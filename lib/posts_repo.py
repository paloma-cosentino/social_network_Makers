from lib.posts import *

class PostsRepo:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        post = []
        for row in rows:
            item = SocialNetworkPosts(
                row["id"], 
                row["post_title"], 
                row["post_content"], 
                row["post_read"],
                row["post_viewed"])
            post.append(item)
        return post
    
    def find(self, post_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])
        row = rows[0]
        return SocialNetworkPosts(
                row["id"], 
                row["post_title"], 
                row["post_content"], 
                row["post_read"],
                row["post_viewed"])
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (post_title, post_content, post_read, post_viewed) VALUES (%s, %s,  %s,  %s)', [
                                post.post_title, post.post_content, post.post_read, post.post_viewed])
        return None