import string

def checkState1(word):
    if len(word) > 0 and word[0] == 'a':
        return stateA(word[1:])
    elif len(word) > 0 and word[0] == 'b':
        return stateB(word[1:])
    elif len(word) > 0 and word[0] == 'c':
        return stateC(word[1:])
    elif len(word) > 0 and word[0] == 'f':
        return stateF(word[1:])
    elif len(word) > 0 and word[0] == 'h':
        return stateH(word[1:])
    elif len(word) > 0 and word[0] == 'i':
        return stateI(word[1:])
    elif len(word) > 0 and word[0] == 'm':
        return stateM(word[1:])
    elif len(word) > 0 and word[0] == 'o':
        return stateO(word[1:])
    elif len(word) > 0 and word[0] == 's':
        return stateS(word[1:])
    elif len(word) > 0 and word[0] == 't':
        return stateT(word[1:])
    elif len(word) > 0 and word[0] == 'w':
        return stateW(word[1:])
    elif len(word) > 0 and word[0] == 'y':
        return stateY(word[1:])
    return False

def stateA(word):
    if len(word) == 0:
        return True
    elif len(word) > 0 and word[0] == 'n':
        return stateA2(word[1:])
    elif len(word) == 1 and word[0] == 't':
        return True
    return False

def stateA2(word):
    if len(word) == 0:
        return True
    elif len(word) > 0 and word[0] == 'd':
        return True
    return False

def stateB(word):
    if len(word) > 0 and word[0] == 'u':
        return stateB2(word[1:])
    return False

def stateB2(word):
    if len(word) == 1 and word[0] == 't':
        return True
    return False

def stateC(word):
    if len(word) > 0 and word[0] == 'a':
        return stateC2(word[1:])
    return False

def stateC2(word):
    if len(word) == 1 and word[0] == 'n':
        return True
    return False

def stateF(word):
    if len(word) > 0 and word[0] == 'r':
        return stateF2(word[1:])
    return False

def stateF2(word):
    if len(word) > 0 and word[0] == 'o':
        return stateF3(word[1:])
    return False

def stateF3(word):
    if len(word) == 1 and word[0] == 'm': # "from"
        return True
    return False

def stateH(word):
    if len(word) == 1 and word[0] == 'e': # "he"
        return True
    return False

def stateI(word):
    if len(word) == 0:
        return True # "i"
    elif len(word) == 1 and word[0] == 'n': # "in"
        return True
    return False

def stateM(word):
    if len(word) == 1 and word[0] == 'y':  
        return True # "my"
    elif len(word) > 0 and word[0] == 'a':
        return stateM_A(word[1:]) 
    elif len(word) > 0 and word[0] == 'u':
        return stateM_U(word[1:]) 
    return False

def stateM_A(word):
    if len(word) == 1 and word[0] == 'y': # "may"
        return True 
    return False

def stateM_U(word):
    if len(word) > 0 and word[0] == 's':
        return stateM_U2(word[1:])
    return False

def stateM_U2(word):
    if len(word) == 1 and word[0] == 't': # "must"
        return True 
    return False

def stateO(word):
    if len(word) == 1 and word[0] == 'n': # "on"
        return True 
    elif len(word) == 1 and word[0] == 'r': # "or"
        return True 
    return False

def stateS(word):
    if len(word) > 0 and word[0] == 'h':
        return stateS_H(word[1:]) 
    elif len(word) == 1 and word[0] == 'o': # "so"
        return True 
    return False

def stateS_H(word):
    if len(word) == 1 and word[0] == 'e': # "she"
        return True 
    elif len(word) > 0 and word[0] == 'o': 
        return stateS_H2(word[1:]) 
    return False

def stateS_H2(word):
    if len(word) > 0 and word[0] == 'u':
        return stateS_H3(word[1:])
    return False

def stateS_H3(word):
    if len(word) > 0 and word[0] == 'l':
        return stateS_H4(word[1:])
    return False

def stateS_H4(word):
    if len(word) == 1 and word[0] == 'd': # "should"
        return True 
    return False

def stateT(word):
    if len(word) > 0 and word[0] == 'h':
        return stateT_H(word[1:]) 
    elif len(word) == 1 and word[0] == 'o': # "to"
        return True 
    return False

def stateT_H(word):
    if len(word) > 0 and word[0] == 'e':
        return stateT_HE(word[1:])
    elif len(word) > 0 and word[0] == 'i':
        return stateT_HI(word[1:])
    return False

def stateT_HE(word):
    if len(word) == 0:
        return True # "the"
    elif len(word) == 1 and word[0] == 'y': # "they"
        return True 
    return False

def stateT_HI(word):
    if len(word) == 1 and word[0] == 's': # "this"
        return True 
    return False

def stateW(word):
    if len(word) == 1 and word[0] == 'e': # "we"
        return True 
    elif len(word) > 0 and word[0] == 'i': 
        return stateW_I(word[1:]) 
    return False

def stateW_I(word):
    if len(word) > 0 and word[0] == 'l':
        return stateW_IL(word[1:])
    return False

def stateW_IL(word):
    if len(word) == 1 and word[0] == 'l': # "will"
        return True 
    return False

def stateY(word):
    if len(word) > 0 and word[0] == 'o':
        return stateY_O(word[1:])
    return False

def stateY_O(word):
    if len(word) == 1 and word[0] == 'u': # "you"
        return True 
    return False

# take input
filename = "text3.txt"
try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        
        # 1. separate each word from the text paragraph
        words = text.split()
        
        for w in words:
            # Stripping punctuation around the word and converting to lowercase
            clean_word = w.strip(string.punctuation).lower()
            if not clean_word:
                continue
            
            # 2. tokenize into character, separate by space bar.
            # Example: "and" -> "a n d"
            tokens = " ".join(list(clean_word))
            print(f"Word: {clean_word}")
            print(f"Tokens: {tokens}")
            
            # 3. create state if its string "and" ONLY.
            # accept or reject
            if checkState1(clean_word):
                print("Status: accept\n")
            else:
                print("Status: reject\n")

except FileNotFoundError:
    print("File not found.")