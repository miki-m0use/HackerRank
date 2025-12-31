def main(s):

    for i in range(len(s)):
        if s[i].isalnum():
            print(True)
            break
    else:
        print(False)

    for i in range(len(s)):
        if s[i].isalpha():
            print(True)
            break
    else:
        print(False)    
    
    for i in range(len(s)):
        if s[i].isdigit():
            print(True)
            break
    else:
        print(False)    
    
    for i in range(len(s)):
        if s[i].islower():
            print(True)
            break
    else:
        print(False)    

    for i in range(len(s)):
        if s[i].isupper():
            print(True)
            break
    else:
        print(False)  


if __name__ == '__main__':
    s = input()
    main(s)    
