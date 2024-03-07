#Capital letter or small letter

char=input("Enter a character")   

if 'A'<=char<='Z':
    print(f"{char}is a capital letter.")
elif 'a'<=char<='z':
    print(f"{char}is a small letter.")
else:
    print(f"{char}is not a letter.")
    