import csv

with open('ml_raw.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['Index'], row['Title'])
#f = open('ml_raw.csv', 'r')
#newFile = open('newFile', 'a')
#for row in csv.reader(f):
#    print row
#f.close()



