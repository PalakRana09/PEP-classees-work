class Grandfather:
    def show_grandfather(self):
        print("I am the Grandfather.")

class Father(Grandfather):
    def show_father(self):
        print("I am the Father.")

class Son(Father):
    def show_son(self):
        print("I am the Son.")

# Create object of Son
s = Son()

# Call all methods
s.show_grandfather()
s.show_father()
s.show_son()
