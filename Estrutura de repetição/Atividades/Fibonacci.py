"""Faça  um  programa  que  mostre  os  oito 
primeiros termos da sequência de Fibonacci. 
 
0-1-1-2-3-5-8-13-21-34-55-..."""

print("-"*40)
print("Sequência de Fibonacci".center(40))
print("-"*40)
print()
t = 8
t1 = 0
t2 = 1

print(f"{t1} -> {t2} ",end="")
cont = 3
while cont <= t:
    t3 = t1 + t2
    print(f"-> {t3} ",end="") 
    t1 = t2
    t2 = t3
    cont += 1
