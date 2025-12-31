import textwrap

def wrap(string, max_width):

    lineas = []
    for i in range(0, len(string), max_width):
        lineas.append(string[i:i+max_width])
    return '\n'.join(lineas)

    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    