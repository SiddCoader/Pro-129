import csv

data = []

with open("C127.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
browndwarfs_data = data[1:]

#Converting all planet names to lower case
for data_point in browndwarfs_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
browndwarfs_data.sort(key=lambda browndwarfs_data: browndwarfs_data[2])


with open("C128.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(browndwarfs_data)
