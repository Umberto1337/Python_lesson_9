from copy import deepcopy

phone_book = {}
path ='phones.txt'
original_phone_book = {}

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contanct in data:
       uid, name, phone, comment = contanct.strip().split(';')
       phone_book[int(uid)] = [name, phone, comment]
    original_phone_book = deepcopy(phone_book)

def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        all_conacts = []
        for uid, contact in phone_book.items():
            all_conacts.append(';'.join([str(uid), contact[0], contact[1], contact[2]]))
        all_conacts = '\n'.join(all_conacts)
        file.write(all_conacts)
            


def add_contact(new: list[str]) -> str:
    uid = max(phone_book) + 1
    phone_book[uid] = new
    

def search(word):
    result = {}
    for uid, contact in phone_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[uid] = contact
                break
    return result


def delete_contact(uid: int) -> str:
    return phone_book.pop(uid)[0]


def change_contact(uid: int, rename: list[str]):
    contact = phone_book.get(uid)
    for i in range(3):
        if rename[i]:
            contact[i] = rename[i]          
    phone_book[uid] = contact
    return contact[0]