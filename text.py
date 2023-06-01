main_menu = '''\nГЛАВНОЕ МЕНЮ\n
1. Открыть файл
2. Записать файл
3. Показать контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта'
save_successful = 'Телефонная книга успешно сохранена'

load_error = 'Телефонная книга пуста или не открыта'

input_contact = {'name':'Введите имя: ', 
                 'phone':'Введите телефон: ',
                 'comment':'Введите комментарий: '}

new_contact = 'Введите данные нового контакта (пустое поле для отмены): '


def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'

cancel_input = 'Отмена ввода'

index_del_contact = 'Введите индекс контакта который хотите удалить: '

def del_contact(name: str):
    return f'Контакт {name} успешно удален'

find_contact = 'Введите кого нужно найти: '

def empty_search(word)->str:
    return f'Контакты содержащие слово {word} не найдены'


input_change = 'Введите кого нужно изменить: '