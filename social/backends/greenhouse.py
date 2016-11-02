"""
Greenhouse OAuth2 backend, docs at:
    https://developers.greenhouse.io/candidate-ingestion.html#authentication
"""
from social.backends.oauth import BaseOAuth2


class GreenhouseOAuth2(BaseOAuth2):
    name = 'greenhouse'
    AUTHORIZATION_URL = 'https://api.greenhouse.io/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.greenhouse.io/oauth/token'
    CONSUMER_KEY = 'fY5Te7oIUIqqq1qJ3rHPnNkP8G3SHmolDRnmQidc'
    CONSUMER_SECRET = 'Z457rsGsWTZZ9I3CsJXQroySQeUH9rV0TQKDnSOz'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_id(self, details, response):
        return response['response']['user']['id']

    def get_user_details(self, response):
        """Return user details from Foursquare account"""
        info = response['response']['user']
        email = info['contact']['email']
        fullname, first_name, last_name = self.get_user_names(
            first_name=info.get('firstName', ''),
            last_name=info.get('lastName', '')
        )
        return {'username': first_name + ' ' + last_name,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('https://api.foursquare.com/v2/users/self',
                             params={'oauth_token': access_token,
                                     'v': self.API_VERSION})
