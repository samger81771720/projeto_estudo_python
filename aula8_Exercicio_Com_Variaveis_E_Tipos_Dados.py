nome_do_cidadao = 'André Luiz Geraldo Sampaio'
ano_atual = 2024
ano_de_nascimento = 1978
idade_atual = ano_atual - ano_de_nascimento
idade_da_maioridade = 18
altura_em_metros = 1.78
confirmacao_da_maioridade = idade_atual >= idade_da_maioridade

print(
    'Nome do cidadão: ' + nome_do_cidadao + '\n', 
    '\rAno de nascimento:', ano_de_nascimento,
    '\nIdade:', idade_atual,
    '\nAltura em metros:', altura_em_metros,
    '\nConfirma maior de idade?', confirmacao_da_maioridade, '\n\n'
)