import requests
from bs4 import BeautifulSoup
import urllib.parse



# FIRST: get current SAMLRequest and RelayState
def get_saml_request():
    response = requests.get(
        url='https://cast.itunes.uni-muenchen.de/auth/shibboleth/callback?from=frontend',
        allow_redirects=False
    )

    # find referral link
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find('a')['href']

    # extract SAMLRequest and RelayState form link
    saml_request = link.split('SAMLRequest=')[1].split('&RelayState=')[0]
    relay_state = link.split('SAMLRequest=')[1].split('&RelayState=')[1]

    return {
        'link': link,
        'saml_request': saml_request,
        'relay_state': relay_state
    }


# SECOND
def get_csrf_token(link):
    response = requests.get(url=link)

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', attrs={
        'name': 'csrf_token'
    })['value']

    action = soup.find('form', attrs={
        'method': 'post'
    })['action']

    cj = response.cookies

    for cookie in cj:
        print(cookie.name, cookie.value, cookie.domain)

    return {
        'csrf_token': csrf_token,
        'action': action
    }



# THIRD
def post_login_data(action, csrf_token, username, password):
    url = 'https://lmuidp.lrz.de'+action
    username = urllib.parse.quote_plus(username)
    password = urllib.parse.quote_plus(password)
    jsessionsid = ''
    eventid_proceed = ''

    payload = '_eventId_proceed='+eventid_proceed+'&csrf_token='+csrf_token+'&j_password='+password+'&j_username='+username
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=51CCC2B58AEBB1868734554BF96676A2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text



# saml = get_saml_request()
# print(saml)
# csrf = get_csrf_token(saml['link'])
# print(csrf)
# # print(post_login_data(csrf['action'], csrf['csrf_token'], 'ru76pes', 'test'))


def cookie():
    response = requests.get(url='https://lmuidp.lrz.de/idp/profile/SAML2/Redirect/SSO?SAMLRequest=jZJLT8MwEIT%2FSuR748YkSmo1lUJ7oFKhVVM4cEF5bIglxw5em9evJ30A5VJxs%2BSdmZ1PO8Wikz3PnG3VFl4coPXeO6mQHz5S4oziukCBXBUdILcVz7PbFWf%2BmPdGW11pSbwMEYwVWs21QteBycG8igrut6uUtNb2yCmtCrS%2BsE4B%2Bk6JUedAVS0ovwaat6IstQTb%2Boia7iMY3azzHfEWw05CFXv3Xy%2FZOVH3vjSfe%2FXwpMMyjZBwkm6hFgYqS%2FN8TbzlIiVPME6CqygMm7gJWZNMkrAqy2ASx3UUT8o4HMYQHSwV2kLZlLAxY6NxNGLJjjEeJJxFj8TbnDpfC1UL9XwZUHkcQn6z221GxzoPYPBQZRggs%2BkeMz8EmzPwl22Lb9pk9h%2B2%2BMN2Ss%2Fijtk9vxv8l4uNlqL68DIp9dvcQGEhJQGhs6Pk74XMvgA%3D&RelayState=ss%3Amem%3A610c47f41482e62385981d449e4adcf2ac5947e05e1f45d44f3d25a8d591761c')
    cj = response.cookies

    for cookie in cj:
        print(cookie.name, cookie.value, cookie.domain)

    print(response.headers)

cookie()