import csv
from cryptography.fernet import Fernet
from faker import Faker  

def generate_key():
    return Fernet.generate_key()

def generate_file(output_csv):
    fake = Faker()
    data = []

    for i in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.street_address()
        date_of_birth = fake.date_of_birth()
        data.append([first_name, last_name, address, date_of_birth])
        
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['first_name','last_name','address','date_of_birth'])
        writer.writerows(data)

def encrypt_csv(input_csv, output_csv):
    key = generate_key()
    fernet = Fernet(key)

    with open('key.txt', 'w') as file:
        file.write(key.decode("utf-8"))

    with open(input_csv, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for i in range(len(rows)):
            if i != 0:
                rows[i][0] = fernet.encrypt(rows[i][0].encode()).decode()
                rows[i][1] = fernet.encrypt(rows[i][1].encode()).decode()
                rows[i][2] = fernet.encrypt(rows[i][2].encode()).decode()

    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

if __name__ == "__main__":
    generate_file('data.csv')
    encrypt_csv('data.csv', 'data_enc.csv')
