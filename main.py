import csv

file_name = "oscar_age_female.csv"
data = []

with open(file_name, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)

    for line in reader:
        index = int(line[0])
        year = int(line[1])
        age = int(line[2])
        name = str(line[3])
        movie = str(line[4])

        data.append([index, year, age, name, movie])

write_file_name = open("results.csv", "w")
writer = csv.writer(write_file_name)
writer.writerow(["Name", "Age"])

# Youngest actress
youngest_age = 100
youngest_name = ""

for line in data:
    if line[2] < youngest_age:
        youngest_age = line[2]
        youngest_name = line[3]

print(youngest_name, youngest_age)
writer.writerow([youngest_name, youngest_age])

# Oldest Actrees
oldest_age = 0
oldest_name = ""

for line in data:
    if line[2] > oldest_age:
        oldest_age = line[2]
        oldest_name = line[3]

print(oldest_name, oldest_age)
writer.writerow([oldest_name, oldest_age])
