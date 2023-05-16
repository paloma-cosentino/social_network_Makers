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

    