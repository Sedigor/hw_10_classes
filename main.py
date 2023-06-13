from collections import UserDict

class Field:
    pass

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone=None):
        self.phone = phone

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        
    def name(self):
        return self.name

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone == old_phone:
                phone.value = new_phone

class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name()
        self.data[key] = record