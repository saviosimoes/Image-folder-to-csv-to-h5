import os
import csv
#print(os.name)

path = os.listdir('/home/savio/Desktop/final project/224by224product/test')
objects = os.listdir('/home/savio/Desktop/final project/224by224product/test/Real')

label = 'Real'
names = []
    

with open('image-Real.csv','w',newline="") as file:
    fieldnames = ['image','label']
    writer = csv.DictWriter(file , fieldnames = fieldnames)
    writer.writeheader()
    for j in objects:
        writer.writerow({'image':j,'label':label})
        
#print(image-data.csv)


    