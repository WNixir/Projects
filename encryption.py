# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28


def clean_message(original_message):
    '''(str) -> str
    The function takes in a text message that only has one line of text and
    strips away any non-alphabet chacters and spaces, then it converts all
    the letters in the message to uppercase.

    REQ: a string with only one line of text

    >>> clean_message('this Is a    sTring')
    'THISISASTRING'
    >>> clean_message('____Hello World$$$$')
    'HELLOWORLD'
    '''
    # start an empty string
    character_str = ''
    # loop through each character in the original message
    for character in original_message:
        # check if the character is a member of the alphabet
        if character.isalpha():
            # add to the str if the character belongs to the alphabet
            character_str += character
    # convert the new string to all uppercase
    clean_message = character_str.upper()
    # return the result
    return clean_message


def encrypt_letter(input_letter, keystream):
    ''' (str, int) -> str
    This function takes in a single letter and a keystream value as inputs
    It then converts the letter to uppercase, and assigns it a value based
    on its value in the ASCII (i.e. 'A' becomes 65, 'B' becomes 66, 'C'
    become 67...) Then the function will add this value to the keystream value
    together, if the final value is greater than ord('Z') = 90, meaning it's
    outside the alphabet, it will subtract 26 from it. The final value is then
    used to find an uppcase letter using ASCII

    REQ: the letter must be a single alphabetical character
    REQ: keystream is an int of values between 1 to 26

    >>> encrypt_letter('D', 13)
    'Q'
    >>> encrypt_letter('f', 23)
    'C'
    >>> encrypt_letter('z', 26)
    'Z'
    >>> encrypt_letter('A', 25)
    'Z'
    '''
    # first the function ensures any input letter is capitalized
    letter_upper = input_letter.upper()
    # the function converts the letter to ASCII value
    letter_ascii = ord(letter_upper)
    # the function takes the keystream value and adds to ASCII
    letter_keystream_sum = letter_ascii + keystream
    # if the sum is less or equal to ord('Z)
    if letter_keystream_sum <= ord('Z'):
        # return an encrypted letter with this ASCII value
        encrypted_letter = chr(letter_keystream_sum)
    # if the value is great than ord('Z')
    else:
        # return an encryted letter at the ascii value minus 26
        encrypted_letter = chr(letter_keystream_sum - 26)
    return encrypted_letter


def decrypt_letter(input_letter, keystream):
    ''' (str, int) -> str
    This function takes one encrypted letter and a keystream value as input
    The function will first convert the input letter into an integer based
    on its representaion in the ASCII, then it will subtract the keystream
    value from this number. If the number is less than ord('A) = 0, meaning
    it's outside the uppercase alphabet, it will add 26 to it. Lastly the
    function uses the final value to find the uppercase letter in the ASCII

    REQ: the letter must be a single alphabetical character
    REQ: keystream is an int of values between 1 to 26

    >>> decrypt_letter('a', 13)
    'N'
    >>> decrypt_letter('C', 23)
    'F'
    >>> decrypt_letter('z', 25)
    'A'
    >>> decrypt_letter('A', 25)
    'B'
    >>> decrypt_letter('a', 1)
    'Z'
    '''
    # first the function ensures any input letter is in uppercase
    letter_upper = input_letter.upper()
    # convert the letter to its ASCII value
    letter_ascii = ord(letter_upper)
    # the function then subtracts the keystream value from ASCII
    letter_keystream_sub = letter_ascii - keystream
    # if this difference is greater or equal to ord('A')
    if letter_keystream_sub >= ord('A'):
        # return the decrypted letter with this ASCII value
        decrypted_letter = chr(letter_keystream_sub)
    # if this difference is less than ord('A')
    else:
        # function will add 26 and return the letter
        decrypted_letter = chr(letter_keystream_sub + 26)
    return decrypted_letter


def swap_cards(card_list, index):
    ''' (list of int, int) -> NoneType
    This function takes a list of cards, represented by a list of integers
    ranging from values 1 to 28; and it takes in the target card represented
    by its indext in this list. It then swaps the target card with the card
    that follows it. If the target card is the last item in the list, it will
    be swapped with the first element in the list

    REQ: card_list must be a valid list of integers numbered from 1-28
    REQ: index must be an int with value between 1 and 28

    >>> card_list = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_cards(card_list, 3)
    >>> expected = [1, 2, 3, 5, 4, 6, 7]
    >>> card_list == expected
    True
    >>> card_list = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_cards(card_list, 6)
    >>> expected = [7, 2, 3, 4, 5, 6, 1]
    >>> card_list == expected
    True
    '''
    # check to see if the target card index is at the end of the list
    if (index + 1) == len(card_list):
        # function will exchange the element at this index with
        # the element at the 0th index in the list
        (card_list[index], card_list[0]) = (card_list[0], card_list[index])
    # if the target card index is not at the end of a list
    # function will swap it with the card at the index position following it
    else:
        (card_list[index], card_list[index+1]) = (card_list[index + 1],
                                                  card_list[index])


def move_joker_1(card_list):
    ''' (list of int) -> NoneType
    This function takes a list of cards, represented by a list of integers
    numbered from 1 to 28. It then looks for the index position of JOKER1
    and swap it with the card after it. If JOKER1 happens to be at the end
    of the deck, it will exchange it with the first card in the deck

    REQ: card_list must be a valid list of integers numbered from 1-28

    >>> card_list = [1, 2, 3, JOKER1, 5, 6, 7]
    >>> move_joker_1(card_list)
    >>> expected = [1, 2, 3, 5, 27, 6, 7]
    >>> card_list == expected
    True
    >>> card_list = [1, 2, 3, 4, 5, 6, JOKER1]
    >>> move_joker_1(card_list)
    >>> expected = [27, 2, 3, 4, 5, 6, 1]
    >>> card_list == expected
    True
    '''
    # locate the index position of JOKER1 in the card_list
    joker_1_index = card_list.index(JOKER1)
    # move the position of JOKER1 by performing swap_cards once
    swap_cards(card_list, joker_1_index)


def move_joker_2(card_list):
    ''' (list of int) -> NoneType
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28. It then looks for the index position of JOKER2 and
    performs the card swap twice on JOKER2, so that it is moved 2 positions
    down. The deck is treated as circular, hence JOKER2 is moved to the 1st
    index positon if it's the last card, and 0th index if it's found at the
    second last position

    REQ: card_list must be a valid list of integers numbered from 1-28

    >>> card_list = [1, 2, 3, JOKER2, 5, 6, 7]
    >>> move_joker_2(card_list)
    >>> expected = [1, 2, 3, 5, 6, 28, 7]
    >>> card_list == expected
    True
    >>> card_list = [1, 2, 3, 4, 5, 6, JOKER2]
    >>> move_joker_2(card_list)
    >>> expected = [2, 28, 3, 4, 5, 6, 1]
    >>> card_list == expected
    True
    >>> card_list = [1, 2, 3, 5, 6, JOKER2, 7]
    >>> move_joker_2(card_list)
    >>> expected = [28, 2, 3, 5, 6, 7, 1]
    >>> card_list == expected
    True
    '''
    # run the swap_card function twice
    for count in range(0, 2):
        # locate the index position of JOKER2 in the list of cards
        joker_2_index = card_list.index(JOKER2)
        # swap_cards once so it moves back one place
        swap_cards(card_list, joker_2_index)


def triple_cut(card_list):
    ''' (list of int) -> NoneType
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28. It then looks for the index position of JOKER1 and
    JOKER2. Next it will splice the list at these indext positions, and
    rearrange everything before the first JOKER to the bottom, and everything
    after the second JOKER to the top, what's in between the two jokers are
    kept intact

    REQ: card_list must be a valid list of integers numbered from 1 to 28

    >>> card_list = [1, 2, 3, 4, JOKER2, 5, 6, JOKER1, 7, 8, 9]
    >>> triple_cut(card_list)
    >>> card_list == [7, 8, 9, 28, 5, 6, 27, 1, 2, 3, 4]
    True
    >>> card_list = [1, 2, 3, 4, JOKER2, 5, 6, 7, 8, 9, JOKER1]
    >>> triple_cut(card_list)
    >>> card_list == [28, 5, 6, 7, 8, 9, 27, 1, 2, 3, 4]
    True
    >>> card_list = [JOKER1, 1, 2, 3, 4, 5, 6, 7, 8, 9, JOKER2]
    >>> triple_cut(card_list)
    >>> card_list == [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 28]
    True
    >>> card_list = [1, 2, 3, JOKER1, JOKER2, 4, 5, 6, 7, 8, 9]
    >>> triple_cut(card_list)
    >>> card_list == [4, 5, 6, 7, 8, 9, 27, 28, 1, 2, 3]
    True
    '''
    # locate JOKER1 in the list of cards
    joker_1_index = card_list.index(JOKER1)
    # locate JOKER2 in the list of cards
    joker_2_index = card_list.index(JOKER2)
    # if JOKER1 is found before JOKER2
    if joker_1_index < joker_2_index:
        # slice the list from after JOKER2, between JOKER1 and JOKER2
        # and from before JOKER1. Then join the new pieces together
        card_list[:] = (card_list[joker_2_index + 1:] +
                        card_list[joker_1_index: joker_2_index + 1] +
                        card_list[: joker_1_index])
    # if JOKER1 is found after JOKER2
    else:
        # slice the list from after JOKER1, between JOKER2 and JOKER1,
        # and from before JOKER2. Then reform the list from the new pieces
        card_list[:] = (card_list[joker_1_index + 1:] +
                        card_list[joker_2_index: joker_1_index + 1] +
                        card_list[: joker_2_index])


def insert_top_to_bottom(card_list):
    ''' (list of int) -> NoneType
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28. It will then check the last card in the list, if
    the last card is JOKER2, it will use JOKER1 as the number of cards to move
    if last card is JOKER1 or smaller, it will then take move this number of
    cards. The function will take the previously determined number of cards,
    remove them from the top of the deck, and insert them just before the
    bottom card.

    REQ: card_list must be a valid list of integers numbered from 1 to 28

    >>> card_list = [1, 2, 3, JOKER1, JOKER2, 4, 5, 6, 7, 8, 3]
    >>> insert_top_to_bottom(card_list)
    >>> card_list == [27, 28, 4, 5, 6, 7, 8, 1, 2, 3, 3]
    True
    >>> card_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER2, 3, 6, 9, 12, 15,\
                     18, 21, 24, JOKER1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> insert_top_to_bottom(card_list)
    >>> card_list == [23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,\
                      15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    True
    >>> card_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER2, 3, 6, 9, 12, 15,\
                     18, 21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, JOKER1]
    >>> insert_top_to_bottom(card_list)
    >>> card_list == [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
                      18, 21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    True
    >>> card_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER1, 3, 6, 9, 12, 15,\
                     18, 21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, JOKER2]
    >>> insert_top_to_bottom(card_list)
    >>> card_list == [1, 4, 7, 10, 13, 16, 19, 22, 25, 27, 3, 6, 9, 12, 15,\
                      18, 21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    True
    '''
    # check the value of the last card in the given list
    last_card_num = card_list[-1]
    # if last card is JOKER1 or smaller
    if last_card_num <= JOKER1:
        # slice the list, using the last_card_num as the index
        # everything from the index to the second last card gets
        # placed at the front, followed by the first cards up to
        # the index, the last card stays in place
        card_list[:] = (card_list[last_card_num: -1] +
                        card_list[: last_card_num] +
                        card_list[-1:])
    # if the last card is JOKER2
    else:
        # the function will use the value of JOKER1 as our new index
        # and repeat the previous slicing operations
        card_list[:] = (card_list[JOKER1: -1] +
                        card_list[: JOKER1] +
                        card_list[-1:])


def get_card_at_top_index(card_list):
    ''' (list of int) -> int
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28. It will then check the value of the first card and
    uses it as the index for the list. If the first card is JOKER2, it will
    use the value of JOKER1 as the index. With the new index, the function
    then finds the card at the index position and returns it as the keystream
    value

    REQ: card_list must be a valid list of integers numbered from 1 to 28

    >>> card_list = [9, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 23, 12,\
                     15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> get_card_at_top_index(card_list)
    25
    >>> card_list = [28, 7, 10, 13, 16, 19, 22, 25, 8, 3, 6, 9, 1, 12, 15,\
                     18, 21, 24, 26, 2, 5, 4, 11, 14, 17, 20, 23, 27]
    >>> get_card_at_top_index(card_list)
    27
    >>> card_list = [8, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 1, 12, 15,\
                     18, 21, 24, 26, 2, 5, 4, 11, 14, 17, 20, 27, 23]
    >>> get_card_at_top_index(card_list)
    28
    '''
    # the function will check the value of the first card in the deck
    first_card_value = card_list[0]
    # if the top card is smaller or equal to JOKER1
    if first_card_value <= JOKER1:
        # use the first_card_value as the index of the list
        # and get the value of that card as keystream value
        keystream_value = card_list[first_card_value]
    # if the top card is JOKER2
    else:
        # use JOKER1 as the index of the list
        # and return the value of that card as keystream value
        keystream_value = card_list[JOKER1]
    return keystream_value


def get_next_value(card_list):
    ''' (list of int) -> int
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28. It will then generate a keystream value using the
    previous 5 functions

    REQ: card_list must be a valid list of integers numbered from 1 to 28

    >>> card_list = [6, 9, 1, 12, 15, 18, 21, 24, 26, 2, 10, 27, 3, 11, 14,\
                     28, 5, 4, 23, 17, 20, 13, 16, 19, 22, 25, 7, 8]
    >>> get_next_value(card_list)
    6
    >>> card_list = [13, 16, 19, 22, 25, 7, 8, 27, 11, 14, 5, 4, 28, 6, 9, 1,\
                     12, 15, 18, 21, 24, 26, 2, 10, 23, 17, 20, 3]
    >>> get_next_value(card_list)
    21
    >>> card_list = [28, 27, 28, 27, 5, 27, 28, 27, 28, 1, 28, 27, 3, 27,\
                     28, 27, 28, 27, 5, 28, 27, 28, 27, 3, 28, 27, 28, 6]
    >>> get_next_value(card_list)
    27
    '''
    # first the function swaps JOKER1 with the card following it
    move_joker_1(card_list)
    # second it will move JOKER2 two cards down
    move_joker_2(card_list)
    # next it will perform a triple cut
    triple_cut(card_list)
    # next it perform the insert_top_to_bottom function
    insert_top_to_bottom(card_list)
    # at last it will return a keystream value by using the top card
    keystream_value = get_card_at_top_index(card_list)
    return keystream_value


def get_next_keystream_value(card_list):
    ''' (list of int) -> int
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28. Then it will return the keystream_value if the value
    generate is between 1 and 26. Otherwise it will rerun the get_next_value
    function until it produces a keystream_value between 1 and 26

    REQ: card_list must be a valid list of integers numbered from 1 to 28

    >>> card_list = [6, 9, 1, 12, 15, 18, 21, 24, 26, 2, 10, 27, 3, 11, 14,\
                     28, 5, 4, 23, 17, 20, 13, 16, 19, 22, 25, 7, 8]
    >>> get_next_keystream_value(card_list)
    6
    >>> card_list = [28, 27, 28, 6, 28, 28, 27, 27, 27, 27, 28, 28, 1, 28,\
                     27, 3, 5, 27, 27, 28, 27, 28, 28, 27, 28, 27, 3, 5]
    >>> get_next_keystream_value(card_list)
    6
    '''
    # set the baseline for invalid results at 26
    invalid_val = 26
    # get the initial value generated by the algorithm
    initial_value = get_next_value(card_list)
    # check to see if this value is greater than 26
    while initial_value > invalid_val:
        # funtion will re-run the algorithm until the condition returns False
        initial_value = get_next_value(card_list)
    # the result is assigned as the keystream_value
    keystream_value = initial_value
    return keystream_value


def process_message(card_list, input_str, func_command):
    '''(list of int, str, str) -> str
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28; it also takes in a string of text to encrypt or
    decrypt depending on the command given. The function will first clean the
    input str by converting all letter to uppercase and striping out any
    non-alphabetical characters, and if the command is 'e', the function will
    encrypt the message letter by letter, if the command is 'd', the function
    will decrypt the message one letter at a time. The deck of cards is used
    to generate the keystream value(s) necessary for the procedure

    REQ: card_list must be a valid list of integers numbered from 1 to 28
    REQ: the input_str must be a single line of str
    REQ: func_command must be either 'e', for encryption;
                                  or 'd', for decryption

    >>> card_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER2, 3, 6, 9, 12, 15,\
                     18, 21, 24, JOKER1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(card_list, 'Hello there!', 'e')
    'SNISYSSPYM'
    >>> card_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, JOKER2, 3, 6, 9, 12, 15,\
                     18, 21, 24, JOKER1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(card_list, 'SNISYSSPYM', 'd')
    'HELLOTHERE'
    '''
    # call the clean_message function to ready the input_str for processing
    input_clean = clean_message(input_str)
    # start up an empty str for the result
    processed_message = ''
    # if command is 'e'
    if func_command == 'e':
        # encrypt each letter from the input_str
        for character in input_clean:
            # first generate a keystream value for each character
            keystream = get_next_keystream_value(card_list)
            # append each new letter to the string
            processed_message += (encrypt_letter(character, keystream))
    # if command is 'd'
    elif func_command == 'd':
        # decrypt each letter from the input_str
        for character in input_clean:
            # first generate a keystream value for each character
            keystream = get_next_keystream_value(card_list)
            # append the new letter to the string
            processed_message += (decrypt_letter(character, keystream))
    return processed_message


def process_messages(card_list, msg_str_list, func_command):
    '''(list of int, list of str, str) -> list of str
    This function takes in a list of cards, represented by a list of integers
    numbered from 1 to 28; it also takes a list of strings and a function
    command. Depending on the command, which is either 'e' for encryption,
    or 'd' for decryption, the function will process each string from the list
    and return a encrypted or decrypted string

    REQ: card_list must be a valid list of integers numbered from 1 to 28
    REQ: msg_str_list must be a valid list of strings
    REQ: func_command must be either 'e', for encryption;
                                  or 'd', for decryption

    >>> card_list = [13, 16, 19, 22, 25, 7, 8, 27, 11, 14, 5, 4, 28, 6, 9, 1,\
                     12, 15, 18, 21, 24, 26, 2, 10, 23, 17, 20, 3]
    >>> process_messages(card_list, ['hello', 'How are you?'], 'e')
    ['CCXBE', 'SAAFDSWMW']
    >>> card_list = [13, 16, 19, 22, 25, 7, 8, 27, 11, 14, 5, 4, 28, 6, 9, 1,\
                     12, 15, 18, 21, 24, 26, 2, 10, 23, 17, 20, 3]
    >>> process_messages(card_list, ['CCXBE', 'SAAFDSWMW'], 'd')
    ['HELLO', 'HOWAREYOU']
    '''
    # build a new list for processed messages
    processed_msgs = []
    # perform the encryption algorithm on each string from input list
    for a_string in msg_str_list:
        # append the processed strings to the new list
        processed_msgs.append(process_message(card_list, a_string,
                                              func_command))
    return processed_msgs


def read_messages(original_txt_file):
    ''' (io.TextIOWrapper) -> list of str
    This function analyzes an opened .txt file and returns each individual
    line from the .txt file as an element in a list of strings. It strips any
    newline from each line
    '''
    # first the function organizes each indidual line in a list of string
    raw_str_list = original_txt_file.readlines()
    # build an empty list for the strings the function will return
    str_list = []
    # use a for loop to remove all newlines from the list of strings
    for a_string in raw_str_list:
        str_list.append(a_string.strip('\n'))
    return str_list


def read_deck(original_deck_file):
    ''' (io.TextIOWrapper) -> list of int
    This function reads an opened .txt containing a list of integers ranging
    from 1 to 28, representing a deck of cards. It then returns the list of
    integers
    '''
    # first the function organizes each element in a list of strings
    raw_str_list = original_deck_file.readlines()
    # make one long string with from the lists
    deck_str = ''.join(raw_str_list)
    # split each number into a list of individual elements
    card_deck_str = deck_str.split()
    # create a new list of integers for the cards
    card_deck_int = []
    # loop through each element in the deck_str and change
    # them into an int, and append to the deck_int_list
    for element in card_deck_str:
        card_deck_int.append(int(element))
    # the deck of cards is returned as a list of integers
    return card_deck_int
