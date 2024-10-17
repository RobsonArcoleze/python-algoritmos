import re

# // Problema "cpf"
# // Dado o CPF de uma pessoa, o qual pode conter pontos ou traços como separadores, retorne o CPF contendo somente dígitos.

# // Exemplo 1:
# // Entrada 87409217293 Saída 87409217293

# // Exemplo 2:
# // Entrada 874092172-93 Saída 87409217293 

# // Exemplo 3:
# // Entrada 874.092.172-93 Saída 87409217293

def remove_non_digits(cpf):
    return re.sub(r'\D', '', cpf);



def remove_non_digits_2(cpf):
    char_array = []

    for char in cpf:
        if char.isdigit():
            char_array.append(char)
            
    return ''.join(char_array);


print(remove_non_digits_2('874.092.172-93'))
