vowels = {'a','e','i','u','o'}
x = str(input("Enter a Letter: "))
if not (vowels.intersection(set(x))):
    print("Not a Vowel")
else:
    print("A vowel!")