
from os import system
from logo import logo

def caesar(chosen_direction,text_typed,shift_amount):
    final_text = ''
    for letter in text_typed:
        position = alphabet.index(letter)
        forward_position = position+shift_amount
        backward_position = position - shift_amount
        if chosen_direction == 'encode' or chosen_direction == 'enconde':
            if position + shift_amount > 26:
                final_text += alphabet[forward_position-26]
            else:
                final_text += alphabet[forward_position]
        else:
            if position + shift_amount <0:
                final_text += alphabet[backward_position+26]
            else:
                final_text += alphabet[backward_position]
    
    print(f'The {chosen_direction}d message is: {final_text}\n')

loop = True
while loop == True:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != 'encode' and 'decode':
        direction = input("You write wrong\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift NUMBER:\n"))

    caesar(chosen_direction=direction,text_typed=text,shift_amount=shift)

    again = input('Do you want to type another message? y/n\n').lower()
    if again != 'y':
        loop = False
        print('goodbye friend')
    else:
        system('cls')
