    #open a file
with open("C:\SCHOOL\programing\sets_HW_text.txt" , encoding= "utf-8") as source_file:
    content = source_file.readline()
    content = content.lower()
    print(content)
    
    #remove unwanted symbols from text
    unwanted_symbols = []  
    single_letter = []
    for i in range(len(content)):
        single_letter.append(content[i])            
    for letter in single_letter:
        if letter.isalpha() or letter.isspace():
            pass
        else:
            unwanted_symbols.append(single_letter.pop(single_letter.index(letter)))            
    text = ""
    for string in single_letter:
        text += string
    #create a list of words from file without punctuation  
    text = text.split()
    
    print(text)
    words = set(text)
    print(words)
    
    
    print(f"Unwanted symbols in text: {unwanted_symbols}")
    print(f"The number of words is: {len(text)}")
