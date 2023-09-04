import requests
import json

url = 'https://91haoka.cn/api/gth/order-pages/for-web?_page_size=20&page=1&share_id=514446'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

# 发起带有头部字段的HTTP GET请求
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    products = data['data']

    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
        print("产品信息已保存为products.json文件")
else:
    print("请求失败，状态码：", response.status_code)
