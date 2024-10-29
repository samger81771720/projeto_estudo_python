"""
Interpretador do Python

O interpretador do Python é o software responsável 
por executar programas escritos na linguagem Python.
Ele lê o código-fonte, interpreta e executa as 
instruções linha por linha. Diferente de linguagens 
compiladas, onde o código é convertido para linguagem 
de máquina antes da execução, o Python é uma linguagem 
interpretada, o que significa que o código é executado 
diretamente pelo interpretador.

Essa característica de ser uma linguagem interpretada 
é uma das razões pela qual Python é tão popular para 
desenvolvimento rápido e prototipagem. Não há necessidade 
de uma etapa de compilação separada, o que torna o ciclo 
de desenvolvimento mais ágil. 

Interpretação Dinâmica: Python converte o código-fonte para 
bytecode na hora da execução. Esse bytecode é então 
interpretado pela máquina virtual Python (PVM). Esse 
processo é transparente e imediato, permitindo a 
execução direta e interativa do código.

Agilidade: A ausência de uma fase explícita de 
compilação permite um ciclo de desenvolvimento
mais rápido, ideal para prototipagem e scripts 
de automação.

Interatividade: O modo interativo de Python 
(REPL - Read-Eval-Print Loop) permite testar 
e executar comandos linha por linha no terminal.

------------------------------------------------------------------------

Uma comparação com Java:

Java é uma linguagem de programação que utiliza uma 
combinação de compilação e interpretação. Quando 
você escreve um programa em Java, o código fonte é 
primeiro compilado para bytecode pelo compilador 
Java (javac). Esse bytecode não é código de máquina, 
mas uma representação intermediária que pode ser 
executada pela Java Virtual Machine (JVM).
A JVM então interpreta ou compila (usando a compilação 
Just-In-Time - JIT) esse bytecode em código de máquina 
específico da plataforma onde o programa está sendo 
executado. Isso permite que o Java seja uma linguagem 
multiplataforma, pois o bytecode pode ser executado 
em qualquer máquina que tenha a JVM adequada instalada.

Compilação Explícita: Java requer a compilação do 
código-fonte em bytecode usando o compilador javac. 
Esse bytecode é então executado pela Java Virtual 
Machine (JVM).

Desempenho: Java pode realizar otimizações durante 
a compilação Just-In-Time (JIT) na JVM, convertendo 
bytecode em código de máquina altamente otimizado 
no momento da execução.

Portabilidade: O bytecode Java pode ser executado 
em qualquer plataforma que tenha uma JVM, o que o 
torna extremamente portátil.

------------------------------------------------------------------
COMANDOS:

* python --help (fornece uma lista de 
opções de linha de comando e argumentos 
que você pode usar ao executar o 
interpretador Python.)

* python mod.py (executa o mod)
* python -u (unbuffered)
* python -m mod (lib mod como script)
* python -c 'cmd' (comando)
* python -i mod.py (interativo com mod)

-------------------------------------------------------------------
"The Zen of Python, por Tim Peters"

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""