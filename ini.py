file = open('my_defaults.ini', 'r')

data = file.read()

letterCount = sum(c.isalpha() for c in data)
numberCount = sum(c.isnumeric() for c in data)

with open('outputs.txt', 'w') as outputFile:
    outputFile.write(f"Letter count: {letterCount}\n")
    outputFile.write(f"Number count: {numberCount}\n")