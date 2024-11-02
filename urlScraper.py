import re
import requests
from bs4 import BeautifulSoup

#Recieving the user_url_input from user.
user_url_input = input('Please enter URL: ')

#Function used to ensure https and www are placed in url to prevent bs4 errors.
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

#Assigning a variable to call the above function and create a proper url.
formated_url = verify_url(user_url_input)
email_list = []

#Trying to call url, verify a reachable status, parse html with bs4 and target emails in the page.
try:
    response = requests.get(formated_url, timeout=10)
    response.raise_for_status()  # Raises an error for non-200 status codes
    soup = BeautifulSoup(response.text, 'html.parser')
    emails = soup.find_all('a', class_='email')
    
    #Adding to our email_list from the emails targets
    for i in emails:
        i_text = i.get_text()
        email_list.append(i_text)
    
    print(f'URL: {formated_url}\nStatus: {response.status_code}\n \n' + '\n'.join(email_list))

except requests.exceptions.RequestException as e:
    print(f'Error: Unable to reach the website: {formated_url}')
    print(e)



