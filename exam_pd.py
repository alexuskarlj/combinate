import requests
import pandas as pd
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

        df = pd.DataFrame(sorted_data, columns=['Name', 'Age'])

        df.to_csv('sorted_birthdays.csv', index=False)

        print("Data successfully written to sorted_birthdays.csv")
    else:
        print("Failed to retrieve data from the API. Status code:", response.status_code)

if __name__ == "__main__":
    main()
