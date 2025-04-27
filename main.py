import csv

data = []

#anything that needs to use the csv file needs to live indented under with because it closes the file after the with block ends
with open('sampledata.csv', mode= 'r') as file: 

    reader = csv.reader(file)
    

    for row in reader: 
        data.append(row)

        

print(data[2])
hex= data[2][0].split()
print(hex[2])
#print(data[2][1])
