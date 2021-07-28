# more variable methods in classes
class Label:
    # add class.__doc__ 
    """methods in classes w/ positional arguments"""
    def __init__(self, name, releases, owned, spent):
        self.name = name
        self.releases = releases
        self.owned = int(owned)
        self.spent = int(spent)
        #self.amount = None
        #self.price = None

    # useful for debug printing every set argument value 
    def __setattr__(self, name, value):
        # print special attributes stored in __dict__
        print(f"[debug:]>>> {name} = {value}\n")
        self.__dict__[name] = value

    def __getattr__(self, name):
        # print special attributes stored in __dict__
        print(f"[debug:]>>> get the '{name}' attribute")
        # build return values based on condition or raise error
        if name == 'total':
            return f"{self.name} {self.spent}"
        else:
            raise AttributeError(f"no attribute named {name}")

    # set default resturn string if no arguments called
    def __str__(self):
        return f"{self.name} {self.spent}"

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
""" 
    def checkout(self):
        self.owned += int(label1.amount)
        self.spent += int(label1.price)
"""

# print __doc__ object if class description is given
print(f"\n[debug:] Print class doc \'print(Label.__doc__)\'")
print(f"[debug:] {Label.__doc__}\n")

# set attributes for object
print(f"set default values \'label1.name, label1.releases, label1.owned, label1.spent\'\n")
label1 = Label("critical", "100+", "\t10", "\t100")
label2 = Label("othercide","100+", "\t1", "\t10")

# print dictionary object as json
""" print(f"[debug:] print given object as json")
print(f"[debug:] label1: {label1.__dict__})
print(f"[debug:] label2:",{label2.__dict__}\n") """

# print some attrs
#print(" Label\t\t Releases\t Owned:\n\n",label1.name,"\t",label1.releases,"\t\t",label1.owned,"\n",label2.name,"\t",label2.releases,"\t\t",label2.owned,"\n")

# print f method is little shorter and removes heading/trailing whitespaces
print(f"Label\t\tReleases\tOwned\t\tSpent:\n\n{label1.name}\t{label1.releases}\t\t{label1.owned}\t\t{label1.spent}\n{label2.name}\t{label2.releases}\t\t{label2.owned}\t\t{label2.spent}\n")

# print attrs before buy
print(f"base values:")

# print using normal and f method, different syntax
print(f"{label1.name} owned: {label1.owned} spent total: {label1.spent}")
print(f"{label2.name} owned: {label2.owned} spent total: {label2.spent}\n")

# call function, change attributes
print(f"[call: ] label1.autobuy(), label2.autobuy() 1 critical for 10, buy 2 othercide for 36\n")
label1.autobuy(1,10)
label2.autobuy(2,36)

# doesn't work with return value condition, maybe too much bash thinking
"""
if label1.autobuy(1,10):
    #print(f"autobuy: {label1.amount} for {label1.price} [success]")
    print(f"autobuy: {amount} for {price} [success]")
else:
    #print(f"autobuy: {label1.amount} for {label1.price} [failed]")
    print(f"autobuy: {amount} for {price} [failed]") 
"""

# use user input for method buy() arguments
print(f"how much {label1.name} bought?")
label1.amount = int(input("amount: "))
label1.price = int(input("price: "))

label1.buy()
#label1.checkout()

# after buy
print(f"\nvalues after increment label1.owned parameter in label1.buy() method")
print(f"{label1.name} owned: {label1.owned} spent total: {label1.spent}")
print(f"{label2.name} owned: {label2.owned} spent total: {label2.spent}\n")

# print dictionary object as json
print(f"[debug:] print given objects as json, note additional fields")
print(f"[debug:] {label1.__dict__}")
print(f"[debug:] {label2.__dict__}\n")

# __getattr__ method
print(f"get 'total' attribute which does not exist")
print(f"build attribute on the fly using __getattr__ condition")
print('return f"{name} {spent}"\n')
print(label1.total)

# call default __str__ method which set 'total' as well
print(f"call object with no args, default __str__ set to total")
print(label1)
