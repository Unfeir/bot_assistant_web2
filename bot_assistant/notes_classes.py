from collections import UserList
from colorama import Fore, Style, init
from bot_assistant.address_book_classes import SaveData

import re

init()


class Notes(UserList, SaveData):
    ''' Загальний клас в якому зберігаються всі нотатки як екземплври класу Record'''

    def add_record(self, record):
        '''метод додає новий єекземпляр класу'''
        self.data.append(record)

    def cahange_note_text(self, number: int, new_value):
        '''змінює текст нотатку, на вході приймає № нотатку та нове значення'''
        self.data[number].change(new_value)

    def cahange_tag(self, number: int, action, tag):
        '''змінює текст нотатку, на вході приймає № нотатку, дію(додати/видалит) та нове значення'''
        if action == 'add':
            self.data[number].add_tag(tag)
        elif action in ['del', 'dell', 'delete']:
            self.data[number].del_tag(tag)
        else:
            return 'no such tag'

    def sort_notes(self, way=1):
        '''функція сортуввання. для реверсного сортування потрібно передати -1
        повертае всі ноаттки'''
        if way == 1:
            self.data.sort(key=lambda record: record.tag.value)
        else:
            self.data.sort(key=lambda record: record.tag.value, reverse=True)

        return self.get_notes()


class Note:
    '''1 екземпляр класу = 1 нотатка, в середені має текст і тегі'''

    def __init__(self, tag, body):
        self.tag = Tag(tag)
        self.body = Body(body)

    def change(self, new_value):
        '''змінює текст нотатки, приймає новий текст'''
        self.body.value = new_value

    def add_tag(self, new_tag):
        '''додає тег, приймає новий тег'''
        splited = sorted(re.split('\W', new_tag))
        self.tag.value.extend([i.lower() for i in splited if bool(i) == True])
        self.tag.value.sort()

    def del_tag(self, tag):
        '''видаляє тег, приймає тег. Повертає текст помилки якщо такого тегу немає без помилки'''
        try:
            self.tag.value.remove(tag.lower())
        except:
            raise Exception('no such tag')


class Field:
    def __init__(self, value):
        self.value = value


class Tag(Field):
    def __init__(self, value):
        splited = sorted(re.split('\W', value))
        self.value = [i.lower() for i in splited if bool(i) == True]


class Body(Field):
    pass
