from lib.users import *

class UsersRepo:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            item = SocialNetworkUsers(
                row["id"], 
                row["user_account"], 
                row["user_name"], 
                row["user_post"])
            users.append(item)
        return users
    
    def find(self, users_id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [users_id])
        row = rows[0]
        return SocialNetworkUsers(
                row["id"], 
                row["user_account"], 
                row["user_name"], 
                row["user_post"])