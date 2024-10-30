card_valid = False

def Validation():
    global card_valid
    original_card_number = list(map(int, input("Enter your credit card number: ")))
    card_number = original_card_number.copy()
    if len(card_number) <= 0:
        print(f"Your card number, {card_number}, is invalid. Please enter a valid card number.")
        card_valid = False
    for i in range (len(card_number) -1, -1, -1):
         if (len(card_number) - i) % 2 == 0:
            card_number[i] *= 2
            if card_number[i] > 9:
                number = [int(digit) for digit in str(card_number[i])]
                card_number[i] = sum(number)
                card_number1 = "".join(map(str, card_number))
    if sum(card_number) % 2 == 0:
        print(card_number)
        original_card_number = "".join(map(str, original_card_number))
        print(f"Your card number, {original_card_number}, is valid.")
        card_valid = True
    else:
        print(f"Your card number, {original_card_number}, is invalid. Please enter a valid card number.")
        card_valid = False
    
while card_valid == False:
        Validation()

# card_valid is False

# define function Validation:
#     set card_valid as global
#     set original_card_number as a list of integers from user input
#     create a copy of orignal_card_number and assign it to card_number
#     if the length of card_number is less than or equal to 0:
#         Output("Your card number is invalid")
#         set card_valid as False
#     for i in range of length card_number from the end to the beginning:
#          if (length of card_number - i) is even:
#             double the value of card_number[i]
#             if the value of card_number[i] is greater than 9:
#                 split the digits of the value of card_number[i] and assign it to number
#                 update card_number[i] to the sum of number
#                 convert card_number to a string and store it in card_number1
#     if the sum of card_number is even:
#         Output(card_number)
#         convert original_card_number to a string 
#         Output(f"Your card number is valid.")
#         set card_valid as True
#     else:
#         Output(f"Your card number is invalid. Please enter a valid card number.")
#         set card_valid as False
    
# while card_valid is False:
#     call Validation function
    