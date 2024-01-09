import unittest
import requests
import json
import os

class TestGetProducts(unittest.TestCase):
    base_url = "https://49w223owx0.execute-api.ap-southeast-1.amazonaws.com/dev" 
    results_folder = "results" 

    def test_get_products(self):
        response = requests.get(f"{self.base_url}/products")
        self.assertEqual(response.status_code, 200)

        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)

        json_file_path = os.path.join(self.results_folder, "response.json")

        try:
            data = response.json()
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
        except json.JSONDecodeError:
            self.fail("Response content is not valid JSON")

if __name__ == '__main__':
    unittest.main()
