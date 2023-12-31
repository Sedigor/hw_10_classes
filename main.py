from collections import UserDict

class Field:
    pass

class Name:
    def __init__(self, name):
        self.value = name

class Phone:
    def __init__(self, phone):
        self.value = phone

class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = []
        self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        
    def add_record(self, record):
        self.data[record.name.value] = record
        
        
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')