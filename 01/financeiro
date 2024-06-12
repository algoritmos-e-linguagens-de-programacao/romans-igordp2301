def proximo_dia_util(dias_passados, dia_atual):  # Adicionando dias_da_semana como um argumento
    dias_da_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
    dias_passados = max(dias_passados)
    dias_restantes = 30 - dias_passados  
    indice_dia_atual = dias_da_semana.index(dia_atual)  
    indice_dia_renovacao = (indice_dia_atual + dias_restantes) % 7  

    if indice_dia_renovacao == 5:  # Sábado
        dias_restantes += 2
    elif indice_dia_renovacao == 6:  # Domingo
        dias_restantes += 1

    return dias_restantes

# Calcular o tempo mínimo de renovação
print(proximo_dia_util([5, 4, 3, 1, 1], "Sab"))
