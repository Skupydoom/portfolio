import requests


url = "http://localhost:9696/predict"

student = {
    "gender": "girl",
    "age": "21-25",
    "education_level": "university",
    "institution_type": "government",
    "it_student": "no",
    "location": "no",
    "load-shedding": "low",
    "financial_condition": "mid",
    "internet_type": "wifi",
    "network_type": "4g",
    "class_duration": "1-3",
    "self_lms": "no",
    "device": "mobile",
}

response = requests.post(url, json=student).json()
print(response)
