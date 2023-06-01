import text

def mein_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_message(message: str):
    print("\n" + '*' * len(message))
    print(message)
    print('*' * len(message) + "\n")    

def print_contacts(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '=' * 71)
        for contact in book:
            print(f'{contact.get("id"):>3}. {contact.get("name"):<20} | {contact.get("phone"):^20} | {contact.get("comment"):<20}')
        print('=' * 71 + '\n')
    else:
        print_message(error)


def input_contact(message: str, cancel: str) -> dict:
    contact = {}
    for key, value in text.input_contact.items():
        data = input(value)
        if data:
            contact[key] = data
        else:
            print_message(cancel)
    return contact

def input_index(message: str, pb: list, error: str) -> int:
    print_contacts(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb)+1:
            return int(index)
        
def input_search(message) -> str:
    return input(message)