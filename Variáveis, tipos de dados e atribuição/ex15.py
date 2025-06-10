"""Sabe-se que: 
   
 1 pé = 12 polegadas; 
 1 jarda = 3 pés; 
 1 milha = 1760 jardas; 
  
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre 
os resultados. 
   
a) polegadas; 
 b) jardas; 
 c) milhas"""

"""
ex: número 5

1 pé ---------- 12 po | 1 jarda ------- 3 pes     | /1760jardas x 3 pés = 5280 pés/ 
5 ------------- x     | x jardas ------ 5 pes     | 1 milha ------ 5280 pés
x = 60                | 3x = 5                    | x ------------ 5 pés
                      | x = 5/3    x = 1,6 jardas | 5280x = 5     x = 5/ 5280     x = 9,46969696969697e-4
"""

num = int(input("Informe a media em pés: "))
po = num * 12
j = num / 3
m = num / 5280 

print("📝Resultado: ")
print(f"{po} Polegadas.")
print(f"{j} Jardas.")
print(f"{m} Milhas.")

