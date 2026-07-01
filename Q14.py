#CS PRACTICAL
#Q-14
import csv
def CopyRec(file1, file2):
    try:
        with open(file1, mode = "r", newline = "\n") as f1, open(file2, mode = "a", newline = "\n") as f2:
            r = csv.reader(f1)
            w = csv.writer(f2)

            next(r)
            c = 0
            for i in r:
                if (int(float(i[3])) > 75000 and i[2].upper() == "ACCOUNT"):
                    w.writerow(i)
                    c += 1
            print("Number of records copied from file1 to file2 is", c)
    except FileNotFoundError:
        print(f"Error: The file (file1) does not exist.")
    except EOFError:
        print(f"Error: The file (file1) has endded.")

f1 = input("Enter the name of file 1 to read from: ")
f2 = input("Enter the name of file 2 to be written:")
CopyRec(f1, f2)
