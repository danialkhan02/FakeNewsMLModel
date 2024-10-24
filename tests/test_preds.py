import requests

test_cases = [
    {"text": "ice cream is not taefdbet5sty"}, # true
    {"text": "iphone is not euroiewruiowe"}, # true
    {"text": "The sky is not jfsdkl;afjklsdafj"}, # false
    {"text": "The computer is a form of technology"} # false
]

url = "http://serve-sentiment-env.eba-9bz3mptm.ca-central-1.elasticbeanstalk.com/predict"

# Test each case
for i, case in enumerate(test_cases):
    response = requests.post(url, json=case)
    print(f"Test case {i+1}: {response.json()}")