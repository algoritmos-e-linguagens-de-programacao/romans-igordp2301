def trips(em_casa, em_work, clima1, resultado):
    em_casa = 2
    em_work = 1
    clima1 = [
        ["Y", "N"],
        ["N", "N"],
        ["Y", "N"],
        ["N", "Y"],
        ["Y", "Y"],
    ]
    resultado = ""


    if clima1[0][0] == "Y" or em_work == 0:
        em_casa -= 1 #casa 1 e trabalho 2
        em_work += 1
        resultado += "Y"
    else: 
        resultado += " N"
    
    if clima1[0][1] == "Y" or em_casa == 0:
        em_casa += 1 #casa 1 e trabalho 2
        em_work -= 1
        resultado += "Y"
    else: 
        resultado += " N,"
    
    if clima1[1][0] == "Y" or em_work == 0:
        em_casa -= 1 #casa 1 e trabalho 2
        em_work += 1
        resultado += "Y"
    else: 
        resultado += " N"
    
    if clima1[1][1] == "Y" or em_casa == 0:
        em_casa += 1 #casa 1 e trabalho 2
        em_work -= 1
        resultado += "Y"
    else: 
        resultado += " N,"

    if clima1[2][0] == "Y" or em_work == 0:
        em_casa -= 1 #casa 1 e trabalho 2
        em_work += 1
        resultado += " Y"
    else: 
        resultado += " N"

    if clima1[2][1] == "Y" or em_casa == 0:
        em_casa += 1 #casa 1 e trabalho 2
        em_work -= 1
        resultado += " Y,"
    else: 
        resultado += " N"

    if clima1[3][0] == "Y" or em_work == 0:
        em_casa -= 1 #casa 1 e trabalho 2
        em_work += 1
        resultado += "Y"
    else: 
        resultado += " N"

    if clima1[3][1] == "Y" or em_casa == 0:
        em_casa += 1 #casa 1 e trabalho 2
        em_work -= 1
        resultado += " Y,"
    else: 
        resultado += " N"

    if clima1[4][0] == "Y" or em_work == 0:
        em_casa -= 1 #casa 1 e trabalho 2
        em_work += 1
        resultado += " Y"
    else: 
        resultado += " N"

    if clima1[4][1] == "Y" or em_casa == 0:
        em_casa += 1 #casa 1 e trabalho 2
        em_work -= 1
        resultado += " Y."
    else: 
        resultado += " N"

    return resultado
    


resultado = trips(2, 1, [["Y", "N"], ["N", "N"], ["Y", "N"], ["N", "Y"], ["Y", "Y"]], "")
print(resultado)
    
