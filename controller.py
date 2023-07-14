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
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break