# a. Count lines, words, and characters in the file
file_path = r"D:\python.other\Nishith Rajwar.txt"

lines_count = 0
words_count = 0
chars_count = 0

with open(file_path, 'r') as file:
    for line in file:
        lines_count += 1
        words_count += len(line.split())
        chars_count += len(line)

print(f"Lines: {lines_count}")
print(f"Words: {words_count}")
print(f"Characters: {chars_count}")

# b. Read the file line by line and store each line in a list
lines_list = []

with open(file_path, 'r') as file:
    for line in file:
        lines_list.append(line.rstrip('\n'))

print(lines_list)


# c. Read data from a CSV file and print each row
import csv

csv_path = r"C:\Users\LENOVO\Downloads\data-1.csv"

with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# d. Merge contents of two files into a third file
file1_path = r"D:\python.other\Nishith Rajwar.txt"
file2_path = r"D:\python.other\Nishith.txt"
merged_path = r"D:\python.other\merged.txt"

with open(merged_path, 'w') as merged_file:
    with open(file1_path, 'r') as file1:
        merged_file.write(file1.read())
    with open(file2_path, 'r') as file2:
        merged_file.write(file2.read())

print("Files merged successfully.")