"""
Greenhouse OAuth2 backend, docs at:
    https://developers.greenhouse.io/candidate-ingestion.html#authentication
"""
from social.backends.oauth import BaseOAuth2


class GreenhouseOAuth2(BaseOAuth2):
    name = 'greenhouse'
    AUTHORIZATION_URL = 'https://api.greenhouse.io/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.greenhouse.io/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        """Return user details from Greenhouse account"""
        return {}
