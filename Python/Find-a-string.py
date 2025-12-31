def count_sub_string(string, sub_string):
    k = len(sub_string)
    contador = 0
    for i in range(0,len(string)):
        if i+k > len(string):
            return contador
        elif string[i:i+k] == sub_string:
            contador += 1
            continue

if __name__ == '__main__': # viene por defecto en hackerrank
    string = input().strip()
    sub_string = input().strip()

    count = count_sub_string(string, sub_string)
    print(count)