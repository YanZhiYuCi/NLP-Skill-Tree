import requests

# post
url = 'http://192.168.206.102:12321/predict'
source = '不良反应】1.发生率较多者为视力模糊、眼痛、红绿色盲或视力减退、视野缩小（视神经炎每日按体重剂量25mg／kg以上时易发生）。'
temp_result = requests.post(url, json={"input": source})
print(temp_result)

# get
r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
