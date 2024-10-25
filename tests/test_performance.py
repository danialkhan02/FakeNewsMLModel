import requests
import time
import csv

test_cases = [
    {"text": "ice cream is not taefdbet5sty"}, # true
    {"text": "iphone is not euroiewruiowe"}, # false
    {"text": "The sky is not jfsdkl;afjklsdafj"}, # false
    {"text": "The computer is a form of technology"} # false
]

url = "http://serve-sentiment-env.eba-9bz3mptm.ca-central-1.elasticbeanstalk.com/predict"

# Open a CSV file to record the timestamps
with open('latency_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['test_case', 'timestamp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Perform 100 API calls for each test case
    for i, case in enumerate(test_cases):
        for _ in range(100):
            start_time = time.time()
            response = requests.post(url, json=case)
            end_time = time.time()
            writer.writerow({'test_case': f"Test case {i+1}", 'timestamp': end_time - start_time})