import ssl
import nltk # need to pip install
import time
import paramiko # Need to pip install
import getpass

from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    return word_list

def check_for_word(words):
    user_answer = input("Enter a word: ")
    if user_answer in words:
        print("The word is in the dictionary")
    else:
        print("The word is not in the dictionary")

def load_external_file():
    password_list = []
    with open('rockyou_sample.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            password_list.append(line)
            print(password_list)

def get_host():
    host  = input('Enter an SSH Client to connect to or enter for default: ') or "192.168.12.211"
    return host

def get_user():
    user = input("Enter a username or enter for default: ") or "darthvader"
    return user

def get_password():
    password = getpass.getpass(prompt="Please provide a password:") or "password1234"
    return password

def ssh_client():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(get_host(), port, get_user(), get_password())
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(3)
        output = stdout.read()
        print("-" * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("pwd")
        time.sleep(3)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(3)
        output = stdout.read()
        print(output)
        print("-" * 50)

    except paramiko.AuthenticationException as e:
        print("Authentication Failed!")
        print(e)

    ssh.close()



if __name__ == "__main__":
    external_words = get_words()
    # print(external_words)
    # print(word_list)
    # check_for_word(external_words)
    # load_external_file()
    ssh_client()