"""Charlinho tem 11 anos, mede 1,40 metros de altura e cresce em média 2,1 centímetros 
ao ano. Seu irmão, Bossa, aos 14 anos, tem 1,45 metros de altura e cresce em média 1,1 
centímetro por ano. Elabore um programa que  conte  quantos anos serão necessários 
para que a altura de Charlinho ultrapasse a de Bossa."""

anos = 0
c = 140
b = 145

while c <= b:
    anos += 1
    c += 2.1
    b += 1.1
    
print(f"Serão necessarios {anos} anos.")    