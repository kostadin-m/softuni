class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) < self.min_length:
            return False
        return True

    def __is_mail_valid(self, mail):
        if mail not in self.mails:
            return False
        return True

    def __is_domain_valid(self, domain):
        if domain not in self.domains:
            return False
        return True

    def validate(self, email):
        data = email.split('@')
        username = data[0]
        mail, domain = data[1].split('.')
        is_valid = all(
            [self.__is_name_valid(username),
             self.__is_mail_valid(mail),
             self.__is_domain_valid(domain)])

        return is_valid
