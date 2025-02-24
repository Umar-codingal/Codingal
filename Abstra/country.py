class India:

    def capital(self):
        print("New delhi is the capital of India")

    def type(self):
        print("India is a developing country")

    def lang(self):
        print("Hindi is widely spoken in India.")

    
class USA:

    def capital(self):
        print("Washington D.C is the capital of India")

    def type(self):
        print("USA is a developed country")

    def lang(self):
        print("English is widely spoken in India.")

i=India()
u=USA()

for c in (i,u):
    c.capital()
    c.type()
    c.lang()
