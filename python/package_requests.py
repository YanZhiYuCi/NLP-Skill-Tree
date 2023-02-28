import requests

# get
r = requests.get('https://www.runoob.com/')
print(type(r.text))
print(r.json())
print(type(r.json()))

kw = {'s': 'python 教程'}
# 设置请求头
headers = {"User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
r = requests.get("https://www.runoob.com/", params=kw, headers=headers)
print(r.text)

# post
url = 'http://192.168.206.102:12321/predict'
source = '不良反应】1.发生率较多者为视力模糊、眼痛、红绿色盲或视力减退、视野缩小（视神经炎每日按体重剂量25mg／kg以上时易发生）。'
temp_result = requests.post(url, json={"input": source})
print(temp_result)
