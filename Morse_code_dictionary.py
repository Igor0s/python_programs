MORSE_CODE_DICT = { 'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-',
                    '(':'-.--.',
                    ')':'-.--.-'
                    }
#from ENG to Morse code
def encrypt(message):
    message = message.upper()
    morse_code = []
    letter_encode = ""
    i = 0
    
    for i in range(len(message)):
        #encode current letter and add it to list
        letter_encode = MORSE_CODE_DICT[message[i]]
        morse_code += [letter_encode]

    for i in morse_code:
        print(i, end=" ")

#from Morse code to ENG
def decrypt(message):
    #reverse the dictionary
    reversedDict = dict()
    for key in MORSE_CODE_DICT:
        val = MORSE_CODE_DICT[key]
        reversedDict[val] = key
    
    message = message.upper()
    message = message.split()
    letter_decode = ""
    decoded_text = []
    
    i=0
    for i in range(len(message)):
        letter_decode = reversedDict[message[i]]
        decoded_text += [letter_decode]
    for i in decoded_text:
        print(i, end=" ")
       
index = str(input("Enter '0' for converting to Morse code  OR  '1' for converting to ENG: "))
message = str(input("Enter a message to encrypt or decrypt: "))

if index == "0":
    encrypt(message)
elif index == "1":
    decrypt(message)


