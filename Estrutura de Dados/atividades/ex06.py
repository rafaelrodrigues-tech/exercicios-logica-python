"""Faça um programa que carregue um  vetor 
com oito números inteiros, calcule e mostre dois vetores resultantes. O primeiro vetor 
resultante deve conter os números positivos. O segundo vetor resultante deve conter 
os  números  negativos.  Cada  vetor  resultante  vai  ter  no  máximo  oito  posições,  sendo 
que nem todas devem obrigatoriamente ser utilizadas. Imprima o conteúdo dos vetores 
resultantes, sem que sejam impressos "lixos de memória"""

vetor = []
vetor_p = [] # Vetor resultante para os Números Positivos
vetor_n = [] # Vetor resultante para os Números Negativos

print("Adicione um número para cada posição a seguir:\n")
for i in range(3): # teste com 3 números
   num = int(input(f" Adicionando na posição {i+1}: "))
   vetor.append(num)

for num in vetor:
   if num >= 0:
      vetor_p.append(num)
   else:
      vetor_n.append(num)

print(f"📝Resultado obtido sobre os vetores:")
print(f"Vetor: {vetor}")
print(f"Números Positivos: {vetor_p}")
print(f"Números Negativos: {vetor_n}")


      


