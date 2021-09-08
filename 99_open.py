# create TextIOWrapper object w/ open()
fileData = open('filedata.txt')

# print(type(fileData))
# print(fileData)

# read content as str() using read()
fileDataContent = fileData.read()
fileDataLength = len(fileDataContent)

print(type(fileDataContent))
print(fileDataLength)

userData = input()

# did not match because of newline char in file...
if fileDataContent == userData:
    print('data match')
else:
    print('no match', fileDataContent, fileDataLength, '!=', userData, len(userData))
