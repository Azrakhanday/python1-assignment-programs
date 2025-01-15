def is_vowel(char):
    char=char.lower()

    return char in 'aeiou'
def main():
    char=input("enter a char")
    if is_vowel(char):
        print("The character is vowel")
    else:
        print("The char is not vowel")
main()






