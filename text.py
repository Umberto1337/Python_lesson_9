main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакт',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

main_menu_input_error = f'Ошибка ввода! Введите число от 1 до {len(main_menu) - 1}:'

empty_book = 'Телефонная книга пуста или не открыта'
load_successful = 'Телефонная книга успешно загружена'
save_successful = 'Телефонная книга успешна сохранена'

fields_new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите комметарий: ']

def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'

input_search_word = 'Введите ключевое элемент для поиска: '

def empty_search(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены'


input_del_uid = 'Введите ID контакта, который хотите удалить: '

def contact_deleted(name: str) -> str:
    return f'Контакт {name} успешно удалён'


fields_rename_contact = ['Введите новое имя контакта (или Enter без изменений): ', 
                         'Введите новый телефон (или Enter без изменений): ', 
                         'Введите новый комметарий (или Enter без изменений): ']

input_rename_uid = 'Введите ID контакта, который хотите изменить: '

def rename_successful(name: str) -> str:
    return f'Контакт {name} успешно изменён'


save_changes = 'Сохранить изменения перед выходом? (y/n)'
good_bay = 'Давай до свидания!'