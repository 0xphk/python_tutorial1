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
        self.owned += amount
        self.spent += price

    # does not work for user input
    def buy(self):
        self.amount = label1.amount
        self.price = label1.price
        self.owned += label1.amount
        self.spent += label1.price

"""     def checkout(self):
        self.owned += int(label1.amount)
        self.spent += int(label1.price) """

# print __doc__ object if class description is given
print("\n[debug:] Print class doc \'print(Label.__doc__)\'")
print("[debug:]",Label.__doc__,"\n")

# set attributes for object
print("set default values \'label1.name, label1.releases, label1.owned, label1.spent\'\n")
label1 = Label("critical", "100+", "\t10", "\t100")
label2 = Label("othercide","100+", "\t1", "\t10")

# print dictionary object as json
print("[debug:] print given object as json")
print("[debug:] label1:",label1.__dict__)
print("[debug:] label2:",label2.__dict__,"\n")

# print some attrs
print(" Label\t\t Releases\t Owned:\n\n",label1.name,"\t",label1.releases,"\t\t",label1.owned,"\n",label2.name,"\t",label2.releases,"\t\t",label2.owned,"\n")

# print attrs before buy
print("base values:")
print(label1.name,"owned:",label1.owned,"spent total:",label1.spent)
print(label2.name,"owned:",label2.owned,"spent total:",label2.spent)

# call function, change attributes
print("autobuy 1 critical for 10, buy 2 othercide for 36\n")
label1.autobuy(1,10)
label2.autobuy(2,36)

# use user input for method buy() arguments
print("how much", label1.name, "bought?")
label1.amount = int(input("amount: "))
label1.price = int(input("price: "))

label1.buy()
#label1.checkout()

# after buy
print("values after increment buy parameter in buy() method")
print(label1.name,"owned:",label1.owned,"spent total:",label1.spent)
print(label2.name,"owned:",label2.owned,"spent total:",label2.spent)

# print dictionary object as json
print("print given object as json")
print("label1:",label1.__dict__)
print("label2:",label2.__dict__)

