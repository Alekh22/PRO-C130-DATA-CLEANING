import csv
import pandas as pd
data1=[]
data2=[]
with open("final.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open("sorted1.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data2.append(row)

headers1=data1[0]
headers2=data2[0]
planet_data1=data1[1:]
planet_data2=data2[1:]
headers=headers1+headers2

planet_data=[]
for index,row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("merge_data.csv","a+")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)