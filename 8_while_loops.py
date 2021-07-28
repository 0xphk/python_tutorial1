# while loop using user input with default value if no input

count = 0
count = int(input("enter count lt 10: [0] ") or 0)
print("base count is:", count, "but increased by 1 using count += 1")
print("while loops starts")
while count < 10:
    print("count is:", count, "of 10")
    count += 1
else:
    print("count exceeded")
    print("while loop ends")