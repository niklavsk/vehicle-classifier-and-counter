DIRECTORY_PATH = 'image-dataset/train/annotations/'

import os
entries = os.listdir(DIRECTORY_PATH)

for entry in entries:
    #read input file
    fin = open(DIRECTORY_PATH + entry, 'rt')

    #read file contents to string
    data = fin.read()

    #replace all occurrences of the required string
    data = data.replace('1.0000000000000002', '1.0')
    data = data.replace('1.0000000000000004', '1.0')
    data = data.replace('1.0000000000000007', '1.0')    
    
    if data.find('1.00') != -1:
        print(entry)
        print(data)

    #close the input file
    fin.close()

    #open the input file in write mode
    fin = open(DIRECTORY_PATH + entry, 'wt')

    #overrite the input file with the resulting data
    fin.write(data)

    #close the file
    fin.close()