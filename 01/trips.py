def trips(dias, em_casa, em_work, clima1):
    
    for i in range(dias):
            
        if clima1[i][0] == "Y" or em_work == 0:
            em_casa -= 1 #casa 1 e trabalho 2
            em_work += 1
            clima1[i][0] = "Y"
        else: 
            clima1[i][0] = "N"
        
        if clima1[i][1] == "Y" or em_casa == 0:
            em_casa += 1 #casa 1 e trabalho 2
            em_work -= 1
            clima1[i][1] = "Y"
        else: 
            clima1[i][1] = "N"
        
        
    
        return clima1
    

#clima1 = trips(2, 1, [["Y", "N"], ["N", "N"], ["Y", "N"], ["N", "Y"], ["Y", "Y"]], "")
print(trips(5, 2, 1, [["Y", "N"], ["N", "N"], ["Y", "N"], ["N", "Y"], ["Y", "Y"]]))
    
