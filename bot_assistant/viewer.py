from abc import abstractmethod, ABC
from colorama import Fore, Style, init


class GeneralView(ABC):
    @abstractmethod
    def view(self):
        pass


class NoteView(GeneralView):
    def view(self, note):
        return f'{Fore.GREEN}{note.tag.value}{Style.RESET_ALL}\n {Fore.BLUE}{note.body.value}{Style.RESET_ALL}'


class ContactView(GeneralView):
    def view(self, contact):
        return f'{Fore.BLUE}    Name:{Style.RESET_ALL}{contact.name.value} \n' \
               f'{Fore.BLUE}  Phones:{Style.RESET_ALL}{contact.get_information(contact.phones)} \n' \
               f'{Fore.BLUE} Address:{Style.RESET_ALL}{contact.get_information(contact.address)} \n' \
               f'{Fore.BLUE}   Email:{Style.RESET_ALL}{contact.get_information(contact.email_list)} \n' \
               f'{Fore.BLUE}Birthday:{Style.RESET_ALL}{contact.birthday} '


class GeneralShow(ABC):
    @abstractmethod
    def show(self):
        pass


class NoteShow(GeneralShow):
    def show(self, notes):
        separate = 50 * '-'
        result = ''
        for idx, note in enumerate(notes, start=1):
            result += f'{Fore.RED}---note №{idx}---{Style.RESET_ALL}\n'
            result += NoteView().view(note)
            result += f'\n {separate}\n'
        return result


class NoteSearch(GeneralShow):
    def show(self, notes, search_text):
        separate = 50 * '-'
        result = ''
        for idx, note in enumerate(notes.data, start=1):
            if search_text in note.body.value:
                result += f'{Fore.RED}---note №{idx}---{Style.RESET_ALL}\n'
                result += NoteView().view(note)
                result += f'\n {separate}\n'
        return result


class NoteSearchTag(GeneralShow):
    def show(self, notes, tag):
        separate = 50 * '-'
        result = ''
        for idx, note in enumerate(notes.data, start=1):

            if tag.lower() in note.tag.value:
                result += f'{Fore.RED}---note №{idx}---{Style.RESET_ALL}\n'
                result += NoteView().view(note)
                result += f'\n {separate}\n'
        return result


class ContactShow(GeneralShow):
    def show(self, address_book, name):
        separate = 30 * '-'
        return f'{ContactView().view(address_book[name])}\n {separate}'


class ContactsShow(GeneralShow):
    def show(self, address_book):
        separate = 30 * '-'
        result = ''
        for contact in address_book:
            result += ContactView().view(address_book[contact])
            result += f'\n {separate}\n'
        return result


class ContactSearch(GeneralShow):
    def show(self, address_book, args):
        search_value = args[0].lower() # if args[0].isalpha() else args[0]
        contacts = []
        for key in address_book.data:
            val = address_book.data[key]
            if search_value in key.lower():
                contacts.append(address_book.data[key])

            else:
                for phone in val.phones:
                    if search_value[0] in phone.value:
                        contacts.append(address_book.data[key])

        separate = 30 * '-'
        result = ''

        for contact in contacts:
            result += ContactView().view(contact)
            result += f'\n {separate}\n'

        return result

