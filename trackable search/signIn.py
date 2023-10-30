import requests

loginURL = 'https://www.geocaching.com/account/signin'
username = 'your_username'
password = 'your_password'

#Make a session logged in to a geocaching account
with requests.Session() as session:
    response = session.get(loginURL)
    csrfToken = response.text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    loginData = {
        '__RequestVerificationToken': csrfToken,
        'UsernameOrEmail': username,
        'Password': password,
        'RememberMe': 'true' 
    }
   
    response = session.post(loginURL, data=loginData)
   
    if response.status_code == 200:
        print("Logged in.")
    else:
        print("Login failed.")

    profile_page = session.get('https://www.geocaching.com/account/dashboard')
    print(profile_page.text)
    input()
