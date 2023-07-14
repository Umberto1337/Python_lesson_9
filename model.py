phone_book = {}
path ='phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contanct in data:
       uid, name, phone, comment = contanct.strip().split(';')
       phone_book[int(uid)] = [name, phone, comment]
