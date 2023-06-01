class PhoneBook:

    def __init__(self, path: str = 'PhoneBook.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            # read - считывает файл отдной строчкой
            # readline - читает по одной строчке (прочитал строку и остановился)
            # readlines - читает полностью файл,разбивает его построчно и делает список строк
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            new = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
            self._phone_book.append(new)

    def save(self):
        data = []
        for contact in self._phone_book:
            contact = ':'.join([value for value in contact.values()])
            data.append(contact)
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    def load(self):
        return self._phone_book

    def add(self, new: dict[str, str]) -> str:
        self._last_id += 1
        new['id'] = str(self._last_id)
        self._phone_book.append(new)
        return new.get('name')

    def del_contact(self, index: int):
        return self._phone_book.pop(index-1).get('name')

    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self._phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result

    def change(self, new: dict, index: int | str) -> str:
        for contact in self._phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')
