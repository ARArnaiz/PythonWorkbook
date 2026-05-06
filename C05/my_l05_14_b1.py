USERS = {
    "alfredo" : "ArnaiZ",
    "claudia" : "SibilA",
    "fredo" : "ArnaizSibilA",
    "camila": "ArnaizSibila,"
}

def login():
    counter = 1
    while True:
        user = input('Enter your username: ').strip().casefold()
        if user in USERS:
            password = input('Enter your password: ').strip()
            if password == USERS[user]:
                print('Login successful!')
                break
            else:
                print('Incorrect password. Please try again.')
        else:
            if counter < 3:
                print('Username not found. Please try again.')
                counter += 1
            else:
                print('Too many failed attempts. Please try again later.')
                break

login()