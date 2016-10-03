import pdb

TYPECASE = "/home/maki/GPOAC.typecase"
VOCABULARY = "/usr/share/dict/words"

letters = []
with open(TYPECASE,'r') as f:
    for letter in f:
        letters.append(set(letter.strip().split(',')))

def is_makeable_recursive(word,used):
    if word=='':
        return True

    for i,letter in enumerate(letters):
        if (not used[i]) and (word[0] in letter):
            next = tuple(used[:i]+(True,)+used[i+1:])
            if is_makeable_recursive(word[1:],next):
                return True

    return False

def is_makeable(word):
    return is_makeable_recursive(word,len(letters)*(False,))

with open(VOCABULARY,'r') as f:
    for word in f:
        if is_makeable(word.strip().upper()):
            print word.strip().upper()
