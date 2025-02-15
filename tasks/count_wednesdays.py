import datetime

def count_wednesdays(input_file="data/dates.txt", output_file="data/dates-wednesdays.txt"):
    try:
        with open(input_file, "r") as file:
            dates = file.readlines()

        # Convert each date string to a weekday
        wednesday_count = sum(1 for date in dates if datetime.datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)

        # Write the count to the output file
        with open(output_file, "w") as file:
            file.write(str(wednesday_count))

        print(f"Successfully counted {wednesday_count} Wednesdays.")
    except Exception as e:
        print(f"Error processing dates: {e}")

if __name__ == "__main__":
    count_wednesdays()
