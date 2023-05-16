class SocialNetworkUsers:
    def __init__(self, id, user_account, user_name, user_post):
        self.id = id
        self.user_account = user_account
        self.user_name = user_name
        self.user_post = user_post

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Users({self.id}, {self.user_account}, {self.user_name}, {self.user_post})"
    

class SocialNetworkPosts:
    def __init__(self, id, post_title, post_content, post_read, post_viewed):
        self.id = id
        self.post_title = post_title
        self.post_content = post_content
        self.post_read = post_read
        self.post_viewed = post_viewed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Posts({self.id}, {self.post_title}, {self.post_content}, {self.post_read}, {self.post_viewed})"
    