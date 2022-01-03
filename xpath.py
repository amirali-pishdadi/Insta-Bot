xpath = {
    'Login': {
        'username': "//input[@name='username']",
        'password': "//input[@name='password']",
        'submit': "//button[@type='submit']",
    },
    'Home': {
        'sava_not': "//button[text()='Not Now']",
        'profile': '//a[@href="/direct/inbox/"]'
    }
}


def get_xpath(part, element):
    return xpath[part][element]

# print(get_xpath('Login' , 'username'))
