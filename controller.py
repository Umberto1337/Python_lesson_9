import view
import model
import text

def start():
    while True:
        user_select = view.show_menu()
        match user_select:
            case 1:
                model.open_file()
                view.print_msg(text.load_successful)
            case 2:
                pass
            case 3:
                pb = model.phone_book
                view.show_contact(pb, text.empty_book)
            case 4:
                contact = view.input_new_contact()
                model.add_contact(contact)
                view.print_msg(text.new_contact_successful(contact[0]))
            case 5:
                word = view.input_data(text.input_search_word)
                result = model.search(word)
                view.show_contact(result, text.empty_search(word))
            case 6:
                pass
            case 7:
                pass
            case 8:
                break