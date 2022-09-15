file = open("/Users/leouev/PycharmProjects/pythonCodes/data.txt", "rt")
data = file.read()
words = data.split()
print('Number of words in text file :', len(words))