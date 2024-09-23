from linkedin_api import Linkedin

class LinkedInBot:
    def __init__(self, access_token: str):
        self.linkedin = Linkedin(access_token)

    def get_connections(self):
        return self.linkedin.get_connections()
