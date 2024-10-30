import requests
from bs4 import BeautifulSoup

#Recieving the user_url_input from user
user_url_input = input('Please enter URL: ')

#Function used to ensure https and www are place in url 
def verify_url(user_url_input):
    http_head = 'https://'
    www_head = 'www.'
    fin_user_url_input = ''
    
    if www_head and http_head not in user_url_input:
        if www_head not in user_url_input:
            user_url_input = www_head + user_url_input
        if http_head not in user_url_input:
            user_url_input = http_head + user_url_input
            
    if www_head not in user_url_input:
            parts = user_url_input.split('://')
            parts[0] += '://'
            parts.insert(1, 'www.')
            user_url_input = ''.join(parts)
        
    return user_url_input

formated_url = verify_url(user_url_input)

try:
    response = requests.get(formated_url, timeout=10)
    response.raise_for_status()  # Raises an error for non-200 status codes
    soup = BeautifulSoup(response.text, 'html.parser')
    # Proceed with your parsing here...
    print(f'Status: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error: Unable to reach the website: {formated_url}')
    print(e)


