'''

def find_frequency(char_list):
    char_list = ['a', 'A', 'B', 'B', 'C', 'd', 'e', 'E']
    a = dict()
    for item in char_list:
        if item.isupper():
            if item in a:
                a[item] += 1
            else:
                a[item] = 1
    print(a)
'''


# Python program to create passwords

from random import random
import string


def generate_random_password(password_length):
    data_source = string.ascii_letters + string.digits + string.punctuation
    password = random.(string.ascii_lowercase)
    password += random(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(password_length):
        password += random.choice(data_source)

    password_list = list(password)
    password_list = random.shuffle(password_list)
    password = ''.join(password_list)
    return password


def main():
    print('Password Generator\n==================\n')
    number = int(input('Number of passwords: '))

    length = input('Password length (min 4): ')
    length = int(length)

    print('\nHere are your passwords:')

    for i in range(1, number):
        print(f"Password number {i}: {generate_random_password(length)}")

    print('\n==================\n')


if __name__ == '__main__':
    main()