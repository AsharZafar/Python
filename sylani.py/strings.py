#capitalize() – changes all string letters to capitals;
#center() – centers the string inside the field of a known length;
#count() – counts the occurrences of a given character;
#join() – joins all items of a tuple/list into one string;
#lower() – converts all the string's letters into lower-case letters;
##lstrip() – removes the white characters from the beginning of the string;
##replace() – replaces a given substring with another;
##rfind() – finds a substring starting from the end of the string;
##rstrip() – removes the trailing white spaces from the end of the string;
##split() – splits the string into a substring using a given delimiter;
##strip() – removes the leading and trailing white spaces;
##swapcase() – swaps the letters' cases (lower to upper and vice versa)
##title() – makes the first letter in each word upper-case;
##upper() – converts all the string's letter into upper-case letters.

#2. String content can be determined using the following methods (all of them return Boolean values):

##endswith() – does the string end with a given substring?
##isalnum() – does the string consist only of letters and digits?
##isalpha() – does the string consist only of letters?
##islower() – does the string consists only of lower-case letters?
##isspace() – does the string consists only of white spaces?
##isupper() – does the string consists only of upper-case letters?
##startswith() – does the string begin with a given substring?


def mysplit(strng):
    # return [] if string is empty or contains whitespaces only
    if strng == '' or strng.isspace():
        return [ ]
    # prepare a list to return
    lst = []
    # prepare a word to build subsequent words
    word = ''
    # check if we are currently inside a word (i.e., if the string starts with a word)
    inword = not strng[0].isspace()
    # iterate through all the characters in string
    for x in strng:
        # if we are currently inside a string...
        if inword:
            # ... and current character is not a space...
            if not x.isspace():
                # ... update current word
                word = word + x
            else:
                # ... otherwise, we reached the end of the word so we need to append it to the list...
                lst.append(word)
                # ... and signal a fact that we are outside the word now
                inword = False
        else:
            # if we are outside the word and we reached a non-white character...
            if not x.isspace():
                # ... it means that a new word has begun so we need to remember it and...
                inword = True
                # ... store the first letter of the new word
                word = x
            else:
                pass
    # if we left the string and there is a non-empty string in word, we need to update the list
    if inword:
        lst.append(word)
    # return the list to invoker
    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
