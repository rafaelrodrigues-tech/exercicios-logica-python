# Receber dois números como parâmetro e retornar o maior entre eles.
def encontra_maior(A, B): # escopo local
    if A > B:
        return A
    else:
        return B

num1 = float(input("Digite o primeiro número: "))   
num2 = float(input("Digite o segundo número: ")) 
res = encontra_maior(num1,num2)

#res = encontra_maior(10,20) #escopo global    

print("O maior número é",res)