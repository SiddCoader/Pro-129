import csv

dataset_1 = []
dataset_2 = []

with open("C127.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("C128.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
browndwarfs_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
browndwarfs_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
browndwarfs_data = []
for index, data_row in enumerate(browndwarfs_data_1):
    browndwarfs_data.append(browndwarfs_data_1[index] + browndwarfs_data_2[index])

with open("C128.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(browndwarfs_data)
