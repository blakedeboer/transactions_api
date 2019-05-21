import csv

def get_row_objects(file_name):
    rows = []
    with open(file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                print(row)
                rows.append(row)
            except Exception:
                print('exeception')
    return rows
