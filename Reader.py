import csv

def load_csv(csvfilename):
    data = []
    #anything that needs to use the csv file needs to live indented under with because it closes the file after the with block ends
    with open(csvfilename, mode= 'r') as file: 

        reader = csv.reader(file)

        #Note reader is an iterable object, so we can loop through it to get each row of data
        #This is set up by the csv module, so we don't need to do anything special to get the data
        #when you use for ... in ..(iterator)... it auto iterates and stores the value from the index in the first variable. 
        for row in reader: 
            data.append(row)



    print('1:',data[2])
    hex= data[2][0].split()
    print(hex)

