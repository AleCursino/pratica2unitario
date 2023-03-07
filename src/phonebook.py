class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}
        self.tamanho_minimo_num = 3
        self.caracteres_invalidos = ['#', '@', '!', '$', '%']

    #refatoraćão da validaćão do tamaanho do numero
    def verify_valid_number(self, number):
        if len(number) >= self.tamanho_minimo_num:
            return True
        else:
            return False

    #metodo pra verificar nomes vazios
    def verify_none_name(self, name):
        if name is None or name == "":
            return True
        else:
            return False

    #verificar se o nome é invalido
    #refatoraćão do método de validaćão do nome
    def verify_valid_name(self, name):
        if not self.verify_none_name(name):
            for item in self.caracteres_invalidos:
                if item in name:
                    return False
            return True
        else:
            return False

    #refatorei o método
    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if self.verify_valid_name(name) and self.verify_valid_number(number):
            if name not in self.entries:
                self.entries[name] = number
                return "Numero adicionado"
            else:
                return "Contato já existente"
        else:
            return "Nome ou número invalido"

    #método refatorado
    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if name in self.entries:
            # return "Numero adicionado"
            return f"O número de {name} é {self.entries[name]}"
        else:
            return "Contato não cadastrado"

    #refatorado
    def get_names(self):
        """

        :return: return all names in phonebook
        """
        lista_names = []
        for name in self.entries.keys():
            lista_names.append(name)
        return lista_names

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        lista_num = []
        for number in self.entries.values():
            lista_num.append(number)
        return lista_num

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return "Phonebook sem registros"

    #metodo alterado
    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        encontrado = {} #inicializar um dicionario
        for name, number in self.entries.items():
            if search_name in name: #deveria ser in
                encontrado[name] = number
        if encontrado != {}:
            return encontrado
        else:
            return "Pesquisa não retornou resultado"

    #refatorado
    def get_phonebook_sorted(self): #ordenar os numeros
        """

        :return: return phonebook in sorted order
        """

        lista_nums = []
        for number in self.entries.values():
            lista_nums.append(number)
        lista_nums.sort()
        return lista_nums

    #refatorado
    def get_phonebook_reverse(self): #reverter os numeros
        """

        :return: return phonebook in reverse sorted order
        """
        lista_nums = []
        for number in self.entries.values():
            lista_nums.append(number)
        lista_nums.sort(reverse=True)
        return lista_nums

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """

        if name in self.entries:
            self.entries.pop(name)
            return 'Numero deletado'
        else:
            return "Contato não cadastrado"

    #método criado usando TDD para atualizar o telefone
    def change_number(self, nome, new_num):
        if self.verify_valid_name(nome) and self.verify_valid_number(new_num):
            if nome in self.entries:
                self.entries[nome] = new_num
                return "Numero atualizado"
            else:
                return "Contato não cadastrado"
        else:
            return "Nome ou numero invalido"


    #método criado usando TDD para saber o nome da pessoa a partir do telefone
    def get_name_by_number(self, num):
        if self.verify_valid_number(num):
            for name, number in self.entries.items():
                if number == num:
                    return name
            return "Numero não cadastrado"
        else:
            return "Numero invalido"
