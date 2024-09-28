"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_informada_str = input(
    'Por gentileza, informe a hora local escrevendo sempre' +
    ' no formato \nde dois números. Ex.: "01"(Uma hora da manhã)' +
    ' ou "23"(Onze horas da noite):  '
)

hora_confirmada = hora_informada_str.isdigit()
primeiro_digito_valido = '012'
segundo_digito_valido = '0123'

primeiro_numero_digitado = hora_informada_str[0]
segundo_numero_digitado = hora_informada_str[1]

mensagem_bom_dia = f'\nBom dia, são {hora_informada_str} hora(s)!\n'
mensagem_boa_tarde = f'\nBom tarde, são {hora_informada_str} hora(s)!\n'
mensagem_boa_noite = f'\nBom noite, são {hora_informada_str} horas(s)!\n'

mensagem_erro_digitacao_texto = (
    f'\nO que você digitou "{hora_informada_str}" não foram números.\n'
)
mensagem_erro_primeiro_digito_invalido = (
    f'\nO únicos valores permitidos para o primeiro campo são '
    f'"O", "1" ou "2". \n'
)
mensagem_erro_segundo_digito_invalido = (
    f'\nO únicos valores permitidos para o segundo campo são '
    f'"O", "1", "2" ou "3".\n'
)

if not hora_confirmada:
    print(mensagem_erro_digitacao_texto)
elif primeiro_numero_digitado not in primeiro_digito_valido:
    print(mensagem_erro_primeiro_digito_invalido)
elif segundo_numero_digitado not in segundo_digito_valido:
    print(mensagem_erro_segundo_digito_invalido)

hora = int(hora_informada_str)
horario_matutino = (hora >= 0 and hora <= 11)
horario_vespertino = (hora >= 12 and hora <= 17)
horario_noturno = (hora >= 18) and (hora <= 23)

if horario_matutino:
    print(mensagem_bom_dia)
elif horario_vespertino:
    print(mensagem_boa_tarde)
elif horario_noturno:
    print(mensagem_boa_noite)





