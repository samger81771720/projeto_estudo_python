# Até a data 14/10/2024 o python na versão 3.13 está tentando introduzir
# um novo complilador que elimina a necessidade e=de implementação do 
# bytecode.

'''
A ordem é: código Python é criado pelo programador, 
depois bytecode e finalmente código de máquina. 

O código Python é primeiro compilado para bytecode, 
que é uma representação intermediária. Esse bytecode 
é então interpretado pela máquina virtual do Python, 
que traduz o bytecode para o código de máquina específico 
do processador.

Essa estrutura facilita a portabilidade do código Python,
permitindo que ele rode em diferentes plataformas com 
pouca ou nenhuma modificação.

'''

'''
EXEMPLO:

Vamos simplificar o processo com o exemplo de print('olá mundo').

------------------------------------------------------------------
1 - "Código Python":

print('olá mundo')

------------------------------------------------------------------

Bytecode em formato legível (usando o "descompilador dis" do Python):

  0 LOAD_GLOBAL              0 (print)
  2 LOAD_CONST               1 ('Olá mundo')
  4 CALL_FUNCTION            1
  6 POP_TOP
  8 LOAD_CONST               0 (None)
 10 RETURN_VALUE

 
 Bytecode (em formato binário):

0 64 00 00 5a 00 71 02 64 01 53 28 00 0a

------------------------------------------------------------------
             
"Código de máquina" (exemplo fictício em x86 assembly):

section .data
    msg db 'olá mundo', 0

section .text
    global _start

_start:
    mov edx, len msg       ; comprimento da mensagem
    mov ecx, msg           ; ponteiro para a mensagem
    mov ebx, 1             ; arquivo de saída (stdout)
    mov eax, 4             ; número da chamada do sistema (sys_write)
    int 0x80               ; chamar o kernel

    mov eax, 1             ; número da chamada do sistema (sys_exit)
    int 0x80               ; chamar o kernel


------------------------------------------------------------------------

'''


# Traduzir é a palavra que melhor captura a essência da 
# "compilação", pois expressa a ideia de converter um código 
# de uma linguagem para outra, permitindo sua execução pelo 
# computador.

