def calculateCase(word): 
    uCase = 0
    lCase = 0

    for elm in word:
        if(elm.isupper()):
            uCase += 1
        else:
            lCase += 1
        
    print('Upper Case: ' + str(uCase) + '\nLower Case: ' + str(lCase))

calculateCase('Learning Python is a lot of fun. I enjoy it!')