
from os import system
from logo import logo

def caesar(chosen_direction,text_typed,shift_amount):
    final_text = ''
    if shift_amount > 84:
        shift_amount %= 84
    for letter in text_typed:
        position = characters.index(letter)
        forward_position = position+shift_amount
        backward_position = position - shift_amount
        if chosen_direction == 'encode' or chosen_direction == 'enconde':
            if position + shift_amount > 84:
                final_text += characters[forward_position-84]
            else:
                final_text += characters[forward_position]
        else:
            if position + shift_amount <0:
                final_text += characters[backward_position+84]
            else:
                final_text += characters[backward_position]
    
    print(f'The {chosen_direction}d message is: {final_text}\n')

characters = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','0','1','2','3','4','5','6','7','8','9',
',','.','!','?',':',';','@','#','$','%','*','(',')','[',']','{','}','/',"'",'-','_',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
loop = True
while loop == True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != 'encode' and direction != 'decode':
        direction = input("You write wrong\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift NUMBER:\n"))

    caesar(chosen_direction=direction,text_typed=text,shift_amount=shift)

    again = input('Do you want to type another message? y/n\n').lower()
    if again != 'y':
        loop = False
        print('goodbye friend')
    else:
        system('cls')
