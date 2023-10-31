import random
import string

# global TOKEN_LIST

class Authenticator():
    def __init__(self, seed : int):
        self.characters = string.ascii_letters + string.digits
        self.SEED = seed
        self.TOKEN_LENGTH = 40

        self.AVAILABLE_TOKEN_LIST = []
        self.ACTIVE_TOKEN_LIST = []

        self.VALID_HOSTS = ['127.0.0.1']
        self.generate_new_token_list()


    def generate_new_token_list(self):
        self.SEED += 10
        random.seed(self.SEED)
        for i in range(10):
            TOKEN = ''.join(random.choice(self.characters) for i in range(self.TOKEN_LENGTH))
            self.AVAILABLE_TOKEN_LIST.append(TOKEN)


    def delete_all_active_tokens(self):
        self.ACTIVE_TOKEN_LIST.clear()
        with open('./dir_noti_app/active_tokens.txt', 'w') as f:
            pass


    def get_token(self):
        if len(self.AVAILABLE_TOKEN_LIST) > 0:
            TOKEN = random.choice(self.AVAILABLE_TOKEN_LIST)
            self.AVAILABLE_TOKEN_LIST.remove(TOKEN)
            self.ACTIVE_TOKEN_LIST.append(TOKEN)

            with open('./dir_noti_app/active_tokens.txt', 'a') as f:
                    f.write(TOKEN + '\n')
            return TOKEN
        else:
            print("No token available!")
            return None


    def authenticate_token(self, TOKEN : str) -> bool:
        print("ACTIVE_TOKENS: ", self.ACTIVE_TOKEN_LIST)
        print("TOKENS available: ", len(self.AVAILABLE_TOKEN_LIST))
        return TOKEN in self.ACTIVE_TOKEN_LIST
    

    def authenticate_host(self, host : str) -> bool:
        print("ACTIVE_HOST: ", self.VALID_HOSTS)
        return host in self.VALID_HOSTS
    

    def authenticate(self, host, TOKEN) -> bool:
        return self.authenticate_host(host) and self.authenticate_token(TOKEN)

    




# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)