class Father:
    def show(self):
        print("I am the Father.")

class Son(Father):
    def display(self):
        print("I am the Son.")

# Create object of Son
s = Son()

# Call methods
s.show()     # Inherited from Father
s.display()  # Defined in Son
