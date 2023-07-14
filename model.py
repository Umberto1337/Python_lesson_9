phone_book = {}
path ='phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contanct in data:
       uid, name, phone, comment = contanct.strip().split(';')
       phone_book[int(uid)] = [name, phone, comment]


def add_contact(new: list[str]) -> str:
    uid = max(phone_book) + 1
    phone_book[uid] = new
    

def search(word):
    result = {}
    for uid, contact in phone_book.items():
        for field in contact:
            if word in field:
                result[uid] = contact
                break
    return result