from geopy.distance import geodesic
import csv
import re


def mrt_latlon_process(mrt, len_mrt, temp):
    top = 0
    pattern = re.compile(r"\d+\.\d+")
    for i in range(len_mrt):
        print(mrt[i][1])
        result = pattern.finditer(mrt[i][1])
        for j in result:
            temp.append(j.group())
    # print(len(temp))
    for row in mrt:
        if "lat & lon" not in row:
            row[1] = temp[top]
            row.append(temp[top+1])
            top += 2
            # print(row)


subway_file = "./get_data/subway_data.csv"
mrt_file = "./get_data/MRT_data.csv"
result_file = "./get_data/subway_MRT_distance.csv"

# read subway file
with open(subway_file, 'r', newline='', encoding='utf-8') as file1:
    reader = csv.reader(file1)
    subway = list(reader)
with open(mrt_file, 'r', newline='', encoding='utf-8') as file2:
    reader = csv.reader(file2)
    mrt = list(reader)

len_subway = len(subway)
len_mrt = len(mrt)
temp = []
min_distence = [[None, None, None, None, None, None, None]
                for i in range(len_subway)]

mrt_latlon_process(mrt, len_mrt, temp)


for p in range(1, len_subway):
    min = geodesic((float(mrt[1][2]), float(mrt[1][1])),
                   (float(subway[p][2]), float(subway[p][3])))
    print(f"{subway[p][0]} and {mrt[1][0]} init distence: {min}")
    for q in range(1, len_mrt):
        distance = geodesic((float(mrt[q][2]), float(mrt[q][1])),
                            (float(subway[p][2]), float(subway[p][3]))).kilometers
        if distance < min:
            print(f"update distance {distance}")
            min = distance
            mrt_index = q
    min_distence[p][0] = subway[p][0]
    min_distence[p][1] = subway[p][2]
    min_distence[p][2] = subway[p][3]
    min_distence[p][3] = mrt[mrt_index][0]
    min_distence[p][4] = mrt[mrt_index][1]
    min_distence[p][5] = mrt[mrt_index][2]
    min_distence[p][6] = min
    q = 0
with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in min_distence:
        writer.writerow(row)
