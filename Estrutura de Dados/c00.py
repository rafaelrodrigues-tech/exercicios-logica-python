conj1 = {"Carlos", "Josiel", "Jandira", "Aline"}
conj2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

print(f"Pessoas presentes nos dois grupos: {conj1.intersection(conj2)}")
print(f"Pessoas que estão somente em um grupo : {conj1.symmetric_difference(conj2)}") # Está em um, mas n está no outro, simultaneamente.
print(f"Lista de pessoas : {conj1.union(conj2)}")
