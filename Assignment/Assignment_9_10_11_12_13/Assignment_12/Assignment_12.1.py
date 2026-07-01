# 1. Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def isVowel(character):
    if character == "a" or character == "e" or character == "i"  or character == "o" or character == "u":
        return True
    else:
        return False

def main():
    character = input("Enter character").lower()
    result = isVowel(character)
    print("Vowel" if result else "Consonent")

if __name__ == "__main__":
    main()