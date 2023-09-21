from geopy.distance import geodesic
import csv
import re

mcd_file = "./get_data/Mcdonalcs_taipei_addr.csv"
metro_file = "./get_data/MRT_data.csv"
result_file = "./get_data/Mcd_MRT_distance.csv"


mrt = []
mcd = []
# process mrt data
with open(metro_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    mrt = list(reader)

patter = re.compile(r"\d+\.\d+")

for row in mrt:
    get = patter.finditer(row[1])
    for l in get:
        row.append(l.group())
    print(row)


# open mcd file
with open(mcd_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    mcd = list(reader)

len_mcd = 0
for row in mcd:
    if '' not in row:
        len_mcd += 1
print(len_mcd)

final_data = [[None, None, None, None, None, None, None, None, None]
              for m in range(len_mcd)]

for i in range(len_mcd):
    min = geodesic((float(mcd[i][3]), float(mcd[i][4])),
                   (float(mrt[1][3]), float(mrt[1][2])))
    min_index = i
    print(f"{mcd[i][0]} and {mrt[1][0]} init distence: {min}")
    for j in range(1, len(mrt)):
        dis = geodesic((float(mcd[i][3]), float(mcd[i][4])),
                       (float(mrt[j][3]), float(mrt[j][2])))
        if dis < min:
            print(f"New minma distance: {dis}, {mrt[j][0]}")
            min = dis
            min_index = j
    for k in range(5):
        final_data[i][k] = mcd[i][k]
    final_data[i][5] = mrt[min_index][0]
    final_data[i][6] = mrt[min_index][2]
    final_data[i][7] = mrt[min_index][3]
    final_data[i][8] = min
with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in final_data:
        writer.writerow(row)
