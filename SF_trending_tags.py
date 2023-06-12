# if u return in json object 
from flask import Flask, jsonify
import json
import requests
import boto3

app = Flask(__name__)

@app.route('/api/tags', methods=['GET'])
def fetch_tags():
    # Set the desired date in Unix timestamp format
    from_date = 1686182400

    # Fetch data from Stack Overflow API
    stackoverflow_url = "https://api.stackexchange.com/2.3/tags"
    params = {
        "site": "stackoverflow",
        "order": "desc",
        "sort": "popular",
        "pagesize": 100,
        "fromdate": from_date
    }
    response = requests.get(stackoverflow_url, params=params)
    data = response.json()

    # Extract tag names from the response
    tags = [tag["name"] for tag in data["items"]]

    # Return JSON response
    response_data = {"tags": tags}
    return jsonify(response_data)

# Run the app
if __name__ == '__main__':
    app.run()


#if u return in s3 bucket 
from flask import Flask, jsonify
import json
import requests
import boto3

app = Flask(__name__)

@app.route('/api/tags', methods=['GET'])
def fetch_tags():
    # Set the desired date in Unix timestamp format
    from_date = 1686182400

    # Fetch data from Stack Overflow API
    stackoverflow_url = "https://api.stackexchange.com/2.3/tags"
    params = {
        "site": "stackoverflow",
        "order": "desc",
        "sort": "popular",
        "pagesize": 100,
        "fromdate": from_date
    }
    response = requests.get(stackoverflow_url, params=params)
    data = response.json()

    # Extract tag names from the response
    tags = [tag["name"] for tag in data["items"]]

    # Convert tag list to JSON
    json_data = json.dumps(tags, indent=2)

    # Upload data to S3 bucket
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    object_key = 'tags.json'

    s3.put_object(
        Body=json_data,
        Bucket=bucket_name,
        Key=object_key
    )

    return "Tags uploaded to S3 successfully!"

# Run the app
if __name__ == '__main__':
    app.run()