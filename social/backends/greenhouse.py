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

    def get_user_id(self, details, response):
        return response['email']

    def get_user_details(self, response):
        """Return user details from greenhouse account"""
        first_name = response['first_name']
        last_name = response['last_name']
        email = response['email']
        fullname, first_name, last_name = self.get_user_names(
            first_name=first_name,
            last_name=last_name
        )
        return {'first_name': first_name,
                'last_name': last_name,
                'full_name': fullname,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json(
            'https://api.greenhouse.io/v1/partner/current_user',
            headers={'Authorization': 'Bearer {0}'.format(access_token)}
        )
