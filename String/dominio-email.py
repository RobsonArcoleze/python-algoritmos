class EmailInfo:
    def __init__(self, username, domain, is_brazilian):
        self.username = username
        self.domain = domain
        self.is_brazilian = is_brazilian;
        
    def to_string(self):
        return self.username + ', ' + self.domain + ', ' + 'sim' if self.is_brazilian else 'nao'  

def extract_email_information(email: str):
    part = email.split('@')
    domain = part[1]
    username = part[0]
    
    is_brazilian = domain.endswith('.br')
    
    return EmailInfo(username, domain, is_brazilian).to_string()


# print(extract_email_information('joao.silva23@yahoo.com.br'))
print(extract_email_information('maria123@gmail.com'))