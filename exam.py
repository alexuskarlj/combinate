import requests
import csv
from datetime import datetime

def calculate_age(birthday):
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def main():
    url = "https://tr148rto1k.execute-api.ap-southeast-2.amazonaws.com/dev/birthdays"
    response = requests.get(url)

    if response.status_code == 200:
        response_data = response.json()
        data = response_data.get('body', []) 

        sorted_data = sorted(
            [(person['name'], calculate_age(datetime.strptime(person['birthday'], '%Y-%m-%d'))) for person in data],
            key=lambda x: x[1]
        )

        with open('sorted_birthdays.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age'])
            writer.writerows(sorted_data)

        print("Data successfully written to sorted_birthdays.csv")
    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)

if __name__ == "__main__":
    main()