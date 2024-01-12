import random

digits = '0123456789'
lowercase_letter = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

countPass = int(input('Введите количество паролей для генерации: '))
lenPass = int(input('Введите длину пароля: '))
includeNum = input('Включать цифры? (y = да, n = нет) ').strip()
includeUp = input('Включать прописные буквы? (y = да, n = нет) ').strip()
includeLo = input('Включать строчные буквы? (y = да, n = нет) ').strip()
includeSym = input('Включать символы? (y = да, n = нет) ').strip()
excludeSym = input(
    'Исключать неоднозначные символы? (y = да, n = нет) ').strip()

chars = ''
if includeNum == 'y':
    chars += digits
if includeUp == 'y':
    chars += uppercase_letters
if includeLo == 'y':
    chars += lowercase_letter
if includeSym == 'y':
    chars += punctuation
if excludeSym == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(len_pass, chars_elem):
    password = ''
    for _ in range(len_pass):
        password += random.choice(chars_elem)
    return password


for _ in range(countPass):
    print(generate_password(lenPass, chars))
