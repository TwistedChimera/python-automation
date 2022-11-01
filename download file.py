import requests

address = r'https://automatetheboringstuff.com/files/rj.txt'

res = requests.get(address)
res.raise_for_status()
file = open('owo.txt', 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)
file.close()
print('done')
