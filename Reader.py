import csv

def load_csv(csvfilename):
    
    
    data = []

    #anything that needs to use the csv file needs to live indented under with because it closes the file after the with block ends
    with open(csvfilename, mode= 'r') as file: 

        reader = csv.reader(file)
        

        for row in reader: 
            data.append(row)



    print('1:',data[2])
    hex= data[2][0].split()
    print(hex)

