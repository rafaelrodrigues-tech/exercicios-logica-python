# upper(): Converte todos os caracteres da string para maiúsculas.          
# lower(): Converte todos os caracteres da string para minúsculas.
# strip(): Remove espaços em branco e caracteres de quebra de linha do inicio e do final da string.
# lstrip(): Remove espaços em branco e caracteres de quebra de linha do inicio da string.
# rstrip(): Remove espaços em branco e caracteres de quebra de linha do final da string.
# replace(<str1>,<str2>): Substitui todas as ocorrências de <str1> por <str2> na string.
# split(<separador>): Divide a string em uma lista de substrings com base no <separador> especificado.
# join (<iterável>): Concatena elementos de um <iterável> (como uma lista) em uma única string, usando a string original.
# startswith(<prefixo>): Verifica se a string começa com o <prefixo> especificado.
# endswith(<sufixo>): Verifica se a string termina com o <sufixo> especificado.
# find(<substrings>):  Retorna o ìndice da primeira ocorrência da <substring> na string (ou -1 se não for encontrada).
# count(<substring>): Conta o número de ocorrências da <substring> na string.
# isalpha(): Verifica se todos os caracteres da string são letras alfabéticas.
# isdigit(): Verifica se todos os caracteres da string são dígitos numéricos.
# isalnum(): Verifica se a string é alfanúmerica, ou seja, consiste em letras e/ou dígitos.
# isnumeric(): Verifica se a string contém apenas caracteres numéricos. 
# len(): Verifica oo tamanho do caractere.
# capitalize(): Vai colocar toodas as letras em minusculas, menos a que inicia.


texto = "Teste"
print("texto",texto)

upper = texto.upper()
print("texto.upper()",upper)
print()

lower = texto.lower()
print("texto.lower()",lower)
print()

texto = "    texto    "
print(f"texto:{texto}")

strip = texto.lstrip()
print(f"texto.lstrip()|{strip}|")

strip = texto.rstrip()
print(f"texto.rstrip()|{strip}|")

strip = texto.strip()
print(f"texto.strip()|{strip}|")
print()

separador = ", "
print(f"separador: {separador}")
join = separador.join(["Eu","Tu","Eles","Nós","Voz","Eles"])
print(f"separador: {join}")

texto = "proparóxitona"
print(f"texto: {texto}")
prefixo = "pro"
e_prefix = texto.startswith(prefixo)
print(f"texto.startswith(\"pro\"):{e_prefix}")

print(f"texto: {texto}")
sufixo = "tona"
e_sufix = texto.endswith(sufixo)
print(f"texto.endswith(\"tona\"):{e_sufix}")
print()

palavra = "disjhvchmicroscodosdosdviusdvhsuidsivbsd"
print(f"palavra: {palavra}")
find = palavra.find("micro")
print(f"palavra.find(\"micro\"):{find}")

count = palavra.count("co")
print(f"palavra.count(\"co\"):{count}")
print()
print()
print()

texto_alfanumerico = "senha123"
texto_alfabetico = "texto"
texto_numerico = "12345"
texto_especiais = "Caracteres especiais: 123,.!@#"
print(f"texto_alfanumerico: {texto_alfanumerico}")
print(f"texto_albetico: {texto_alfabetico}")
print(f"texto_numerico: {texto_numerico}")
print(f"texto_especiais: {texto_especiais}")
print()

isalpha1 = texto_alfanumerico.isalpha()
isalpha2 = texto_alfabetico.isalpha()
isalpha3 = texto_numerico.isalpha()
isalpha4 = texto_especiais.isalpha()
print(f"texto_alfanumerico.isalpha(): {isalpha1}")
print(f"texto_alfabetico.isalpha(): {isalpha2}")
print(f"texto_numerico.isalpha(): {isalpha3}")
print(f"texto_especiais.isalpha(): {isalpha4}")
print()

isdigit1 = texto_alfanumerico.isdigit()
isdigit2 = texto_alfabetico.isdigit()
isdigit3 = texto_numerico.isdigit()
isdigit4 = texto_especiais.isdigit()
print(f"texto_alfanumerico.isdigit(): {isdigit1}")
print(f"texto_alfabetico.isdigit(): {isdigit2}")
print(f"texto_numerico.isdigit(): {isdigit3}")
print(f"texto_especiais.isdigit(): {isdigit4}")
print()

isalnum1 = texto_alfanumerico.isalnum()
isalnum2 = texto_alfabetico.isalnum()
isalnum3 = texto_numerico.isalnum()
isalnum4 = texto_especiais.isalnum()
print(f"texto_alfanumerico.isalnum(): {isalnum1}")
print(f"texto_alfabetico.isalnum(): {isalnum2}")
print(f"texto_numerico.isalnum(): {isalnum3}")
print(f"texto_especiais.isalnum(): {isalnum4}")
print()

isnumeric1 = texto_alfanumerico.isnumeric()
isnumeric2 = texto_alfabetico.isnumeric()
isnumeric3 = texto_numerico.isnumeric()
isnumeric4 = texto_especiais.isnumeric()
print(f"texto_alfanumerico.isnumeric(): {isnumeric1}")
print(f"texto_alfabetico.isnumeric(): {isnumeric2}")
print(f"texto_numerico.isnumeric(): {isnumeric3}")
print(f"texto_especiais.isnumeric(): {isnumeric4}")
print()







