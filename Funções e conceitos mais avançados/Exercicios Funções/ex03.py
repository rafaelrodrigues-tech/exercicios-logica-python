""" Pedro comprou um saco de ração para seus 
gatos, com o peso em quilos. Faça uma função que receba o peso do saco de ração, em 
quilos, o número de gatos e a quantidade de ração fornecida para cada gato por dia, em 
gramas. A função deve retornar o total de quilos de ração restante no saco, após um dia 
de consumo. Assim sendo, considerando que Pedro possui dois gatos, crie um algoritmo 
que invoque a função recém criada para calcular e mostrar quanto restará de ração no 
saco após cinco dias."""
def calculando_racao_restante(peso_racao,qtdd_racao):
    kg = qtdd_racao / 1000
    cinco =  peso_racao - (2 * kg) * 5 # São 2 gatos e 5 dias de consumo
    return cinco
    
peso_racao = float(input("Insira o peso do saco de ração(em Kg): "))
qtdd_racao = float(input("Insira a quantidade de ração fornecida para cada gato(em gramas): "))

cinco = calculando_racao_restante(peso_racao,qtdd_racao)
print(f"Em 5 dias, vão restar {cinco}kg de ração no saco.")