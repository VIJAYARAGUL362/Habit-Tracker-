import requests,os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("MYNAME")
PIXELA_URL = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN":TOKEN
}

# creating user
params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(url=PIXELA_URL,json=params)
print(response.json())

# CREATING A GRAPH

data = {
    "id":"graph1",
    "name":"Leetcode problems",
    "unit":"commit",
    "type":"int",
    "color":"sora",
}




graph_response = requests.post(url=f"{PIXELA_URL}/{USERNAME}/graphs",json=data,headers=headers)
print(graph_response.text)


# PUTTING A ENTRY IN THE GRAPH


today = datetime(year=2025,month=5,day=7)

graph_entry = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"8"
}

graph_entry_response = requests.post(url=f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}",json=graph_entry,headers=headers)
print(graph_entry_response.text)

#  UPDATING A ENTRY IN THE GRAPH

today = datetime.now()
pixela_format_date = today.strftime("%Y%m%d")

graph_update_entry = {
    "date":pixela_format_date,
    "quantity":"50"
}

graph_update_response = requests.delete(url=f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}/{pixela_format_date}",json=graph_update_entry,headers=headers)
print(graph_update_response.text)


