

class User:
    def __init__(self, uname: str, email: str, password: str):
        self.uname = uname
        self.email = email
        self.password = password
        self.servers = []
        self.friends = []

