alphabet = 'abcdefghijklmnopqrstuvwxyz'


def read_file():
    text = ''
    with open('text.txt', 'r', encoding='utf8') as f:
        text = ''.join([line for line in f]).lower()
    return text


def write_file(encrypted_text):
    with open('./encrypted_text.txt', 'w', encoding='utf8') as f:
        f.write(encrypted_text)


def encrypt_text(t, shift):
    text = list(t)
    for i in range(len(text)):
        if text[i] in alphabet:
            index_in_alphabet = alphabet.index(text[i])
            new_letter_index = (index_in_alphabet + shift) % len(alphabet)
            text[i] = alphabet[new_letter_index]
    return ''.join(text)


def decrypt_text(t, shift):
    text = list(t)
    for i in range(len(text)):
        if text[i] in alphabet:
            index_in_alphabet = alphabet.index(text[i])
            new_letter_index = (index_in_alphabet - shift) % len(alphabet)
            text[i] = alphabet[new_letter_index]
    return ''.join(text)


text = read_file()
shift = int(input('shift: '))
encrypted_text = encrypt_text(text, shift)
write_file(encrypted_text)
print(text == decrypt_text(encrypted_text, shift))  # проверка, что decrypt_text правильно работает
