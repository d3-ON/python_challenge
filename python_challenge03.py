from data03 import LETTER

def bodyguards(letter_1, letter_2, letter_3, letter_4, letter_5, letter_6, letter_7, letter_8):
    capital_list = [letter_1, letter_2, letter_3, letter_4, letter_5, letter_6]
    lower_list = [letter_7, letter_8]   
    
    count_capital: int = 0
    count_lower: int = 0
    
    for i in capital_list:
        if i == i.upper() and i != ' ' and i != '\n':
            count_capital += 1
            
    for i in lower_list:
        if i == i.lower() and i != ' ' and i != '\n':
            count_lower += 1   
               
    if count_capital == 6 and count_lower == 2:
        return True
      
solution: str = ''
range_letter = len(LETTER)

for i in range(range_letter):
    
    if LETTER[i] == LETTER[i].lower() and i + 4 < range_letter and i != ' ' and i != '\n':       
        if  bodyguards(LETTER[i-1], LETTER[i-2], LETTER[i-3], LETTER[i+1], LETTER[i+2], LETTER[i+3] , LETTER[i-4], LETTER[i+4]):
            solution += LETTER[i]
            
print(solution)


