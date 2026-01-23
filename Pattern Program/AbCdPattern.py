for row in range(26):
    for col in range(26):
        if(col % 2==0):
            print(chr(65 + col), end = " ")
        else:
            print(chr(97 + col), end = " ")
    print()