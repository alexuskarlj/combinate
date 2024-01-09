import unittest
import requests
import json

class TestCreateProduct(unittest.TestCase):
    base_url = "https://49w223owx0.execute-api.ap-southeast-1.amazonaws.com/dev" 

    def test_create_product(self):
        payload = {
            "Id": "123456",
            "name": "Sample Product",
            "description": "A sample product description",
            "colour": "blue",
            "price_cents": 999
        }

        json_payload = json.dumps(payload)

        headers = {"Content-Type": "application/json"}

        response = requests.post(f"{self.base_url}/products", data=json_payload, headers=headers)

        self.assertEqual(response.status_code, 201, f"Expected status code 201, but received {response.status_code}")

        self.assertIn("application/json", response.headers.get("Content-Type"), "Expected 'Content-Type' header to be 'application/json'")
        self.assertTrue(len(response.text) > 0, "Response content is empty")
