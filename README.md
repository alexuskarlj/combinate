
# Combinate

#### Back-End Developer Examination

#### Part 1 - Python

Instructions:

Write Python code to retrieve a list of names and birthdays from the following endpoint:
```
https://tr148rto1k.execute-api.ap-southeast-2.amazonaws.com/dev/birthdays.
```
-  Determine the age of each person and arrange them in ascending order from
youngest to oldest.

-  Generate an output file in CSV or text format containing the sorted list of names and
their respective ages.

#### Part 2 - AWS

Instructions:
- Make sure you have an AWS Account (personal account)
- Create a serverless application:
```
Tech Stack
    ■ DynamoDB
    ■ API Gateway
    ■ Lambda
    ■ CloudFormation / SAM Template (optional)
```
-  Create Endpoints in API Gateway (Sample CRUD Application)
```
    ■ Create / Save (new) product
    ■ Get / Load (existing) product
    ■ List all products
```
- Create a Table in DynamoDB
```
Name: “Model”
    Fields:
        ■ Id
        ■ name
        ■ description
        ■ colour (red / green / blue)
        ■ price_cents (integer)
```

##
## Installation

Clone the project or download the zip file and go to the directory

```bash
  cd combinate
```
**(Optional)**: You can create virtual environment by running this in the Command Prompt:
```
  python -m venv .venv
  cd .venv/scripts
  activate
```
**Library Dependency:** Install the requirements.txt

*Make sure you're on the directory where the requirements.txt is.*
```bash
  pip install -r requirements.txt
```
##
#### For the First Part:

You can use either exam.py or exam_pd

`exam.py` - without Pandas

`exam_pd.py` - with Pandas 

You can run them by running this in the Command Prompt:
```
// This is to run the exam.py
python exam.py

// This is to run the exam_pd.py
python exam_pd.py
```

It will generate a csv file for the results
##
#### For the Second Part:

You can find the codes I used for my zipped Lambda functions inside
`lambda` folder. 

Files:
`createProduct.zip`, `listProduct.zip`,`loadProduct.zip`.

You can extract them and check them.
## Running Tests

### Unit Tests

To run tests, make sure you're inside the `unittests` folder

**Create Product Test**
```bash
  python -m test_create_product
```

**Get Products Test**
```bash
  python -m test_get_products
```

**Create Product by ID Test**
```bash
  python -m test_get_product_by_id
```
## 
### Postman

You can find `postman` folder and you can see the Postman collection as well.

File name: `Combinate.postman_collection`

You can directly import it to Postman and test it.

##
## Documentation


### ProductsAPI Documentation

#### /products (GET)
**Description**: Get a list of all products.

**Request**:

**Method**: `GET`

**URL**: `/products`

#### Response:

**Status Code**: `200 OK`

**Content**: JSON array with product objects.
##

#### /products (POST)
**Description**:  Create a new product.

**Request**:

**Method**: `POST`

**URL**: `/products`

**Body**: JSON object with product details.

#### Response:

**Status Code**: `201 Created`

**Content**: JSON object of the newly created product.

##

#### /products (GET)
**Description**:  Get a specific product by its ID.

**Request**:

**Method**: GET

**URL**: `/products/{id}`

**Parameter**: id (integer) - ID of the product to retrieve.

#### Response:

**Status Code**: 200 OK

**Content**: JSON object with the product of the specified ID.

##