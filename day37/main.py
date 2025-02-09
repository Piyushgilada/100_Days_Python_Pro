import requests
from datetime import datetime

pixela_endpoint='https://pixe.la/v1/users'
USERNAME='piyushgilada'
TOKEN='piyushishere12345'
user_params={
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f'https://pixe.la/v1/users/{USERNAME}/graphs'
graph_config={
    'id':"graph1",
    'name':"cyclic graph",
    'unit':'km',
    'type':'float',
    'color':'sora'
}
headers={
    'X-USER-TOKEN':TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
today=datetime.now()

# today=datetime(year=2024,month=12,day=1)

PIXEL_ENDPOINT=f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1'
PIXEL_CONFIG={
    'date':today.strftime('%Y%m%d'),
    'quantity':input('How many killometer you cycle today ?')
}
post_response=requests.post(url=PIXEL_ENDPOINT,json=PIXEL_CONFIG,headers=headers)
print(post_response.text)

PIXEL_CONFIG1={
    'quantity':'20',
    'color':'kuro',
    'name':'Cyclic karo',

}
# updated_response=requests.put(url=f'{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}',json=PIXEL_CONFIG1,headers=headers)
# print(updated_response.text)

# deleted_response=requests.delete(url=f'{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}',headers=headers)
# print(deleted_response.text)