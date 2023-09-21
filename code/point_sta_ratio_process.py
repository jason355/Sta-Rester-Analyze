import csv


Mcd_distance_file = './get_data/Mcd_MRT_distance.csv'
Subway_distance_file = './get_data/Subway_MRT_distance.csv'
conclution_file = './get_data/conclution.csv'

data = []
data2 = []

with open(Mcd_distance_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

with open(Subway_distance_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data2 = list(reader)

distance = []  # km
temp = 0.1

for l in range(15):
    distance.append(temp)
    print(distance)
    temp = round(temp + 0.1, 2)
count = 0

del data2[0]
print(data2)
print(f"{Mcd_distance_file}: n(U) = {len(data)}")
print(f"{Subway_distance_file}: n(U) = {len(data2)}")

with open(conclution_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Distance", "Mcdonalcs-n(S)", "Mcdonalcs-ratio"])
    for l in distance:
        for row in data:
            if float(row[8][0:len(row[8])-2]) <= l:
                count += 1
        # print(f" n(S) = {count}")
        ratio = count / len(data)
        text = [l, count, ratio]
        writer.writerow(text)
        count = 0

    writer.writerow([])
    writer.writerow(["Distance", "Subway-n(S)", "Subway-ratio"])
    for l in distance:
        for row in data2:
            if float(row[6][0:len(row[6])-2]) <= l:
                # print(float(row[6][0:len(row[6])-2]))
                count += 1
        # print(f" n(S) = {count}")
        ratio = count / len(data2)
        text = [l, count, ratio]
        writer.writerow(text)
        count = 0
