# object orientation - classes, objects, methods (functions in classes)

# create class
print("create class 'Music'")
class Music:
    # for class 'Music', define __init__() method with 'self' parameter for attributes
    # as more objects may exist, using only attribute artist = won't work
    # self defines attributes to match reference class.object.self.attributes
    def __init__(self):
        # define attributes and type
        self.artist = None
        self.title = None
        self.year = None

# create object with None attributes at start memory 0xaddr (defaults to self as it is the called object)
track1 = Music()
# print type
print("get data type")
print(type(track1))

# print still "empty" attribute from class
print(track1.artist)

# define attribute
track1.artist = "No Name"
track1.title = "Unknown"
track1.year = 1970

# print all attributes with little formatting
print("track1:", track1.artist, "-", track1.title, "/", track1.year)

# print object address reference
print("get object reference (start memory address)")
print(track1)

# reference object as variable, like hardlinks in memory
print("reference object 'track1' as variable 'track2'")
track2 = track1
print("print type")
print(type(track2))

# references to same memory addr
print("print references")
print("track1")
print(track1)
print("track2")
print(track2)

# same content
print("track2")
print("track2:", track2.artist, "-", track2.title, "/", track2.year)

class Label:
    def __init__(self, name, releases):
        self.name = name
        self.releases = releases
label1 = Label("critical", "over 100")
label2 = Label("othercide","maybe 100")
print("Lables - Releases:\n",label1.name, label1.releases,"\n",label2.name, label2.releases)
