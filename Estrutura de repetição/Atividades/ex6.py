"""Um  funcionário  de  uma  empresa  recebe 
aumento salarial anualmente. Sabe-se que:  
 
a) esse funcionário foi contratado em 2015, com salário inicial de R$ 1.000,00; 
b) em 2016 recebeu aumento de 1,5% sobre seu salário inicial; 
c) a partir de 2017 (inclusive), os aumentos salariais sempre corresponderam ao dobro 
da porcentagem do ano anterior."""
from datetime import date # Importando o ano atual.
atual = date.today().year 
sal_i = 1000
perc = (1.5 / 100)

# Aumento de 2016
sal_i += sal_i * perc

for ano in range(2017,atual + 1):
    perc *= 2
    sal_i += sal_i*perc
    print(f"Em {ano} o funcionário vai ter um aumento de {sal_i:.2f}")