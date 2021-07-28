# more variable methods in classes
class Label:
    # add class.__doc__ 
    """methods in classes w/ positional arguments"""
    def __init__(self, name, releases, owned, spent):
        self.name = name
        self.releases = releases
        self.owned = int(owned)
        self.spent = int(spent)
        self.amount = None
        self.price = None

    # works as parameters are given
    def autobuy(self, amount, price):
        self.owned += int(amount)
        self.spent += int(price)

    # does not work for user input
    def buy(self):
        self.amount = None
        self.price = None

    def checkout(self):
        self.owned += int(amount)
        self.spent += int(price)

# print __doc__ object if class description is given
print("Print class doc \'print(Label.__doc__)\'")
print(Label.__doc__)

# set attributes for object
label1 = Label("critical", "100+", "10", "100")
label2 = Label("othercide","100+", "1", "10")

# print dictionary object as json
print("print given object as json")
print("label1")
print(label1.__dict__)
print("label2")
print(label2.__dict__)

# print some attrs
print("\nLables - Releases:\n",label1.name, label1.releases, label1.owned,"\n",label2.name, label2.releases, label2.owned,"\n")

# print attrs before buy
print("base values:")
print(label1.name,"owned:",label1.owned,"spent total:",label1.spent)
print(label2.name,"owned:",label2.owned,"spent total:",label2.spent)

# call function, change attributes
#print("buy 1 critical for 10, buy 2 othercide for 36")
#label1.autobuy(1,10)
#label2.autobuy(2,36)

label1.amount = int(input("amount: "))
label1.price = int(input("price: "))
# does not work, expecting parameters are taken from user input
#print("how much to buy?")
label1.buy()
label1.checkout()

# after buy
print("values after increment buy parameter in buy() method")
print(label1.name,"owned:",label1.owned,"spent total:",label1.spent)
print(label2.name,"owned:",label2.owned,"spent total:",label2.spent)

