# open a file in write mode
fo = open('test.txt', 'w')
print('Name:', fo.name)
print('Mode:', fo.mode)
print('is Closed:', fo.closed)

# write to file
fo.write('Bonjour monsieur Python')
fo.write(' and ML.')

# close file
fo.close()

# append in file
fo = open('test.txt', 'a')
fo.write(" J'aime aussi javascript.")
fo.close()

# read from file
fo = open('test.txt', 'r')
text = fo.read()
print(text)
fo.close()

# create a file
fo = open('test2.txt', 'w+')
fo.write('Ceci est mon nouveau fichier.')
fo.close()

# for list of file mode visit link
# https://www.tutorialspoint.com/python/python_files_io.htm