import pytest

from src.phonebook import Phonebook


class TestPhonebook:

    #testando o método que verifica se o número tem o tamanho correto. Aqui ele será inválido: len(num) < 3
    def test_verify_valid_number_invalid(self):
        #Setup
        phonebook = Phonebook()
        num_invalido = "1"

        #chamada
        result = phonebook.verify_valid_number(num_invalido)

        #avaliacao
        assert result is False

    #testando o método que verifica se o número tem o tamanho correto. Aqui ele será válido: len(num) >= 3
    def test_verify_valid_number_valid(self):
        # Setup
        phonebook = Phonebook()
        num_valido = "123"

        # chamada
        result = phonebook.verify_valid_number(num_valido)

        # avaliacao
        assert result is True

    # testando o método que verifica se o nome é vazio ou None. Aqui ele será vazio
    def test_verify_none_name_empty(self):
        # Setup
        phonebook = Phonebook()
        nome_vazio = ""

        # chamada
        result = phonebook.verify_none_name(nome_vazio)

        # avaliacao
        assert result is True

    # testando o método que verifica se o nome é vazio ou None. Aqui ele será válido
    def test_verify_none_name_valid(self):
        # Setup
        phonebook = Phonebook()
        nome = "Ale"

        # chamada
        result = phonebook.verify_none_name(nome)

        # avaliacao
        assert result is False

    # testando o método que verifica se o nome válido (sem os caracteres não permitidos). Aqui ele será inválido com percentual
    def test_verify_valid_name_invalid_percent(self):
        # Setup
        phonebook = Phonebook()
        nome_percent = "Ale%"

        # chamada
        result = phonebook.verify_valid_name(nome_percent)

        # avaliacao
        assert result is False

    # testando o método que verifica se o nome válido (sem os caracteres não permitidos). Aqui ele será inválido com arroba
    def test_verify_valid_name_invalid_at(self):
        # Setup
        phonebook = Phonebook()
        nome_at = "@Ale"

        # chamada
        result = phonebook.verify_valid_name(nome_at)

        # avaliacao
        assert result is False

    # testando o método que verifica se o nome válido (sem os caracteres não permitidos). Aqui ele será válido
    def test_verify_valid_name_valid(self):
        # Setup
        phonebook = Phonebook()
        nome_valido = "Ale"

        # chamada
        result = phonebook.verify_valid_name(nome_valido)

        # avaliacao
        assert result is True

    #testando o método de adicionar contato com sucesso
    def test_add_new_contact(self):
        #Setup
        phonebook = Phonebook()
        nome_valido = "Alessandra"
        numero_valido = "123789"
        resultado_esperado = "Numero adicionado"

        #chamada
        result = phonebook.add(nome_valido, numero_valido)

        #avaliacao
        assert result == resultado_esperado
        assert phonebook.entries.keys().__contains__(nome_valido)
        assert phonebook.entries.get(nome_valido) == numero_valido #traz o numero relacionado aquele nome

        # testando o método de adicionar contato com sucesso

    #testando o método de adicionar contato. Aqui, tenta inserir um contato já existente
    def test_add_already_contact(self):
        # Setup
        phonebook = Phonebook()
        nome_valido = "Alessandra"
        numero_valido = "123789"
        phonebook.add("Alessandra", "875464")
        resultado_esperado = "Contato já existente"

        # chamada
        result = phonebook.add(nome_valido, numero_valido)

        # avaliacao
        assert result == resultado_esperado

    #testando o método de adicionar contato. Aqui, tenta inserir um nome inválido
    def test_add_invalid_name(self):
        #Setup
        phonebook = Phonebook()
        nome_invalido = "Ale#"
        numero_valido = "123789"
        resultado_esperado = "Nome ou número invalido"

        #chamada
        result = phonebook.add(nome_invalido, numero_valido)

        #avaliacao
        assert result == resultado_esperado

    #testando o método de adicionar contato. Aqui, tenta inserir um numero inválido
    def test_add_invalid_number(self):
        # Setup
        phonebook = Phonebook()
        nome_valido = "Ale"
        numero_invalido = "1"
        resultado_esperado = "Nome ou número invalido"

        # chamada
        result = phonebook.add(nome_valido, numero_invalido)

        # avaliacao
        assert result == resultado_esperado

    #testando o método de buscar um contato pelo nome. Aqui o contato existe
    def test_lookup_valid(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")
        phonebook.add("Carla", "8987654321")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        nome_valido = "Carla"
        numero_esperado = "8987654321"
        retorno = f"O número de {nome_valido} é {numero_esperado}"

        # chamada
        result = phonebook.lookup(nome_valido)

        # avaliacao
        assert result == retorno

    #testando o método de buscar um contato pelo nome. Aqui o contato não existe
    def test_lookup_not_registered(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")
        phonebook.add("Carla", "8987654321")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        nome_nao_cadastrado = "Alessandra"
        retorno = "Contato não cadastrado"

        # chamada
        result = phonebook.lookup(nome_nao_cadastrado)

        # avaliacao
        assert result == retorno

    #testando o método que retorna o nome de todos os contatos
    def test_get_names(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")
        phonebook.add("Carla", "8987654321")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        tamanho_lista_esperado = phonebook.entries.__len__()
        nomes_esperados = list(phonebook.entries.keys())

        # Chamada
        result = phonebook.get_names()

        # Avaliaćao
        assert result.__len__() == tamanho_lista_esperado
        assert list(result) == nomes_esperados

    #testando o método que retorna o número de todos os contatos
    def test_get_numbers(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "120")
        phonebook.add("Carla", "130")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        tamanho_lista_esperado = phonebook.entries.__len__()
        numeros_esperados = list(phonebook.entries.values())

        # Chamada
        result = phonebook.get_numbers()

        # Avaliaćão
        assert result.__len__() == tamanho_lista_esperado
        assert list(result) == numeros_esperados

    #testando o método que apaga todos os contatos
    def test_clear(self):
        # Setup
        phoneBook = Phonebook()
        phoneBook.add("Amanda", "123456")
        tamanho_lista_esperado = 0
        resul_esperado = "Phonebook sem registros"

        # Chamada
        result = phoneBook.clear()

        # Avaliaćão
        assert result == resul_esperado
        assert phoneBook.entries.__len__() == tamanho_lista_esperado

    #testando o método que faz uma busca nos contatos. Aqui ele trará resultado
    def test_search_with_results(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido1 = "Alessandra"
        num_valido1 = "81999999999"
        nome_valido2 = "Alecsandro"
        num_valido2 = "81999999997"
        busca = "Ale"
        phoneBook.add(nome_valido1, num_valido1)
        phoneBook.add(nome_valido2, num_valido2)

        # Chamada
        result = phoneBook.search(busca)

        # Avaliaćão
        assert result[nome_valido1] == num_valido1
        assert result[nome_valido2] == num_valido2

    #testando o método que faz uma busca nos contatos. Aqui ele NÃO trará resultado
    def test_search_no_results(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido1 = "Fernando"
        num_valido1 = "81999999999"
        nome_valido2 = "Joana"
        num_valido2 = "81999999997"
        busca = "Zoe"
        phoneBook.add(nome_valido1, num_valido1)
        phoneBook.add(nome_valido2, num_valido2)

        resultado_esperado = "Pesquisa não retornou resultado"

        # Chamada
        result = phoneBook.search(busca)

        # Avaliaćão
        assert result == resultado_esperado

    #testando o método que ordena os números em ordem crescente
    def test_get_phonebook_sorted(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido1 = "José"
        num_valido1 = "220"
        nome_valido2 = "Carmen"
        num_valido2 = "340"
        phoneBook.add(nome_valido1, num_valido1)
        phoneBook.add(nome_valido2, num_valido2)
        lista_esperada = ["190", num_valido1, num_valido2]

        # Chamada
        result = phoneBook.get_phonebook_sorted()

        # Avaliaćão
        assert result == lista_esperada

    #testando o método que ordena os números em ordem crescente
    def test_get_phonebook_reverse(self):
        # Setup
        phoneBook = Phonebook()
        nome_valido1 = "José"
        num_valido1 = "220"
        nome_valido2 = "Manoel"
        num_valido2 = "340"
        phoneBook.add(nome_valido1, num_valido1)
        phoneBook.add(nome_valido2, num_valido2)
        lista_esperada = [num_valido2, num_valido1, "190"]

        # Chamada
        result = phoneBook.get_phonebook_reverse()

        # Avaliaćão
        assert result == lista_esperada

    #testando o método que deleta um contato da agenda. Aqui irá remover com sucesso.
    def test_delete_success(self):
        # Setup
        phoneBook = Phonebook()
        phoneBook.add("Joana", "158794658")
        phoneBook.add("Morgana", "8745965")
        resul_esperado = 'Numero deletado'
        nome_valido = "Morgana"
        tamanho_lista_esperado = 2 #porque ainda existe o contato da Policia

        # Chamada
        result = phoneBook.delete(nome_valido)

        # Avaliaćão
        assert resul_esperado == result
        assert phoneBook.entries.__len__() == tamanho_lista_esperado

    # testando o método que deleta um contato da agenda. Aqui o contato não existe.
    def test_delete_not_registered(self):
        # Setup
        phoneBook = Phonebook()
        phoneBook.add("Joana", "158794658")
        phoneBook.add("Morgana", "8745965")
        resul_esperado = "Contato não cadastrado"
        nome = "Marcelo"
        tamanho_lista_esperado = 3  # porque existe o contato da Policia e nenhum foi excluído

        # Chamada
        result = phoneBook.delete(nome)

        # Avaliaćão
        assert resul_esperado == result
        assert phoneBook.entries.__len__() == tamanho_lista_esperado

    #primeiro TDD
    # cenarios de testes:
    # case sucesso
    # contato inexistente
    # nome ou numero invalidos - fora das regras estipuladas
    def test_change_number_success(self):
        #Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "12023424")
        phonebook.add("Carla", "1301212")
        nome_valido = "Carla"
        novo_num = "987337"

        resultado_esperado = "Numero atualizado"

        #Chamada
        result = phonebook.change_number(nome_valido, novo_num)

        #Avaliaćão
        assert result == resultado_esperado

    def test_change_number_not_registered(self):
        #Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "120")
        phonebook.add("Carla", "130")
        nome_nao_cadastrado = "Lucas"
        novo_numero = "130"

        resultado_esperado = "Contato não cadastrado"

        #Chamada
        result = phonebook.change_number(nome_nao_cadastrado, novo_numero)

        #Avaliaćão
        assert result == resultado_esperado

    def test_change_number_invalid_name(self):
        #Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "120")
        phonebook.add("Carla", "130")
        nome_invalido = ""
        novo_num = "9877"

        resultado_esperado = "Nome ou numero invalido"

        #Chamada
        result = phonebook.change_number(nome_invalido, novo_num)

        #Avaliacao
        assert result == resultado_esperado

    def test_change_number_invalid_new_number(self):
        #Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "120")
        phonebook.add("Carla", "130")
        nome_valido = "Ale"
        novo_num_invalido = "12"

        resultado_esperado = "Nome ou numero invalido"

        #Chamada
        result = phonebook.change_number(nome_valido, novo_num_invalido)

        #Avaliaćão
        assert result == resultado_esperado

    # Segundo TDD
    # cenarios de testes:
    # case sucesso
    # contato inexistente
    # numero invalido - fora das regras estipuladas
    def test_get_name_by_number_success(self):
        #Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "12023424")
        phonebook.add("Carla", "1301212")
        nome_valido = "Carla"
        numero = "1301212"

        resultado_esperado = nome_valido

        #Chamada
        result = phonebook.get_name_by_number(numero)

        #Avaliaćão
        assert result == resultado_esperado

    def test_get_name_by_number_not_registered(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "120")
        phonebook.add("Carla", "130")
        numero_nao_cadastrado = "9876698"

        resultado_esperado = "Numero não cadastrado"

        # Chamada
        result = phonebook.get_name_by_number(numero_nao_cadastrado)

        # Avaliaćão
        assert result == resultado_esperado

    def test_get_name_by_number_invalid_number(self):
        #Setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "120")
        phonebook.add("Carla", "130")
        num_invalido = "0"

        resultado_esperado = "Numero invalido"

        #Chamada
        result = phonebook.get_name_by_number(num_invalido)

        #Avaliaćão
        assert result == resultado_esperado