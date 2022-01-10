
riddle = """http://www.pythonchallenge.com/pc/def/map.html"""

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y','z']

solution : str = ''
             
for i in riddle:
    if i in ALPHABET:
        indx = ALPHABET.index(i) + 2
        if indx < len(ALPHABET): 
            solution += ALPHABET[indx]
            # solution = riddle.maketrans(i, ALPHABET[indx])
        elif i == 'y':
            solution += ALPHABET[0]
        elif i == 'z':
            solution += ALPHABET[1]
            
    elif i not in ALPHABET:
        solution += i        

# import string
# text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
#             amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
#             ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
#             lmu ynnjw ml rfc spj."""
# table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:]+string.ascii_lowercase[:2])        
    
       
                          
print(solution)
# print(table)