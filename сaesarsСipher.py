# Получение данных от пользователя
def data():
    encryption_or_decryption = input(
        'Шифруем или дешифруем? (e = шифруем, d = дешифруем) ').rstrip()
    language = input(
        'Какой языку используем? (r = русский, e = английский) ').rstrip()
    shift_step = int(input('Шаг сдвига вправо: '))
    text = input('Введите текст: ').rstrip()
    return encryption_or_decryption, language, shift_step, text


# Шифровка текста
def encryption_caesar(text, step, lang):
    # Русский язык
    if lang == 'r':
        for i in text:
            if i.isupper():
                num = ord(i) + step
                if num > 1071:
                    num -= 32
                print(chr(num), end='')
            elif i.islower():
                num = ord(i) + step
                if num > 1103:
                    num -= 32
                print(chr(num), end='')
            else:
                print(i, end='')
    # Английский язык
    elif lang == 'e':
        for i in text:
            if i.isupper():
                num = ord(i) + step
                if num > 90:
                    num -= 26
                print(chr(num), end='')
            elif i.islower():
                num = ord(i) + step
                if num > 122:
                    num -= 26
                print(chr(num), end='')
            else:
                print(i, end='')


# Дешифровка текста
def decryption_caesar(text, step, lang):
    # Русский язык
    if lang == 'r':
        for i in text:
            if i.isupper():
                num = ord(i) - step
                if num < 1040:
                    num += 32
                print(chr(num), end='')
            elif i.islower():
                num = ord(i) - step
                if num < 1072:
                    num += 32
                print(chr(num), end='')
            else:
                print(i, end='')
    # Английский язык
    elif lang == 'e':
        for i in text:
            if i.isupper():
                num = ord(i) - step
                if num < 65:
                    num += 26
                print(chr(num), end='')
            elif i.islower():
                num = ord(i) - step
                if num < 97:
                    num += 26
                print(chr(num), end='')
            else:
                print(i, end='')


# Основная функция
def main():
    code, lang, step, text = data()
    if code == 'e':
        encryption_caesar(text, step, lang)
    elif code == 'd':
        decryption_caesar(text, step, lang)


main()
