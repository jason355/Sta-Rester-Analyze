import csv

f = open("MRT_data.txt", "r", encoding="utf-8")

j = 0


text = f.readlines()
with open("MRT_data.csv", "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["station", "lat & lon"])
    for i in text:
        len_text = len(i)
        print(i[2:len_text-3])
        while i[j:j+1] != ",":
            j += 1
            if j >= len_text:
                break
        first = i[2:j-1]
        second = i[j+3:len_text-3]
        print(first, second)
        j = 0
        writer.writerow([first, second])
