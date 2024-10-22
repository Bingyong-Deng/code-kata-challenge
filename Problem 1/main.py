import csv
import json
import string
import random

def generate_fixed(spec_name, file_name):
    with open(spec_name) as file:
        spec = json.load(file)

    with open(file_name, 'w') as file:
        for i in range(len(spec['ColumnNames'])):
            file.write(spec['ColumnNames'][i])
            for j in range(int(spec['Offsets'][i]) - len(spec['ColumnNames'][i])):
                file.write(" ")
        for k in range(100):
            file.write("\n")
            for i in range(len(spec['ColumnNames'])):
                for j in range(int(spec['Offsets'][i])):
                    file.write(random.choice(string.ascii_letters))

        

def parse(spec_name, file_name):
    with open(spec_name) as file:
        spec = json.load(file)

    data = []

    with open(file_name, 'r') as file:
        content = file.readline()
        while content:
            parsed = []
            count = 0
            for i in range(len(spec['Offsets'])):
                parsed.append(content[count:count + int(spec["Offsets"][i])].rstrip())
                count += int(spec["Offsets"][i])

            data.append(parsed)
            content = file.readline()
    
    return data

def generate_delimited(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__=="__main__":
    generate_fixed('spec.json', 'data.txt')
    data = parse('spec.json', 'data.txt')

    generate_delimited('data.csv', data)
