from src.phonebook import Phonebook

phonebook = Phonebook()
#phonebook.add("Ale", "123")
#resultado = phonebook.add("Alessandra", "123")
phonebook.add("Marilia", "111")
phonebook.add("Zoe", "888")
phonebook.add("Alessandra", "222")
phonebook.add("José", "777")
phonebook.add("Alecsandro", "333")


print(phonebook.get_names())
print(phonebook.get_numbers())
print(phonebook.delete(""))
