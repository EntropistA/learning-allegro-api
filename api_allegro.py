import requests
import json

CLIENT_ID = "5dda08b6cb044a19aeff1544b59feb16"          # wprowadź Client_ID aplikacji
CLIENT_SECRET = "uE1UQgVsydVBsRG8kgAE0NEEuD2JvDn5yZD4L40fhMYgpiR9z0zMPr0Xhn8RoHMt"      # wprowadź Client_Secret aplikacji

REDIRECT_URI = "http://localhost:8000"       # wprowadź redirect_uri
AUTH_URL = "https://allegro.pl/auth/oauth/authorize"
TOKEN_URL = "https://allegro.pl.allegrosandbox.pl/auth/oauth/token"



def get_access_token():
    try:
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False,
                                              allow_redirects=False, auth=(CLIENT_ID, CLIENT_SECRET))
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        return access_token
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def main():
    access_token = get_access_token()
    print("access token = " + access_token)


if __name__ == "__main__":
    main()