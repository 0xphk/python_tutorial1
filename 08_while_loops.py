# while loop using user input with default value if no input

count = 0
# count = int(input("enter count lt 10: [0] ") or 0)
# print("base count is:", count, "but increased by 1 using count += 1")
# print("while loops starts")
# while count < 10:
#     print("count is:", count, "of 10")
#     count += 1
# else:
#     print("count exceeded")
#     print("while loop ends")

# break and continue keywords in while loops
while count < 10:
    # break loop if 5 is reached
    if count == 5:
        print('number is 5, break')
        break
    print(count, "of 10")
    count += 1
else:
    print("count exceeded")

while count < 10:
    count += 1
    # do nothing until 5 is reached
    if count < 5:
        continue
    print(count,'of 10(5)')
