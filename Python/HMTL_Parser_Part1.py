# Problema: HTML Parser - Part 1 (HackerRank)



'''
no se porque no me acepta hackerrank este codigo
en mi terminal si funciona perfectamente
pero en hackerrank no
'''



from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):  
    def handle_starttag(self, tag, attrs):
        if attrs:
            print("Start :", tag)
            for name,value in attrs:
                print(f"-> {name} > {value if value is not None else 'None'}")
        else:
            print("Start :", tag)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag,attrs):
        if attrs:
            print("Empty   :", tag)
            for name,value in attrs:
                print(f"-> {name} > {value if value is not None else 'None'}")
        else:
            print("Empty   :", tag)




parser = MyHTMLParser()
cantidad_delinea = int(input())
for _ in range(cantidad_delinea):
    parser.feed(input())

