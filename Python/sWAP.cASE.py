def swap_case(s):
    palabra = ''
    if len(s) > 1000:
        return
    else:
        palabra = s.swapcase()
        print(palabra)

    return 0

if __name__ == '__main__': # viene por defecto en hackerrank
    s = input()
    result = swap_case(s)
    print(result)



