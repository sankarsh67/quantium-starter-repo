import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["sales", "date", "region"])

    for file_name in os.listdir(DATA_DIRECTORY):
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            next(reader)  # skip header row

            for row in reader:
                product = row[0]
                raw_price = row[1]
                quantity = row[2]
                transaction_date = row[3]
                region = row[4]

                if product == "pink morsel":
                    price = float(raw_price[1:])
                    sale = price * int(quantity)

                    writer.writerow([sale, transaction_date, region])

print("formatted_data.csv created successfully")