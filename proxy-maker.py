import json

proxy_list = [
    "91.246.195.9:6778:rahul222:rahul222",
"103.37.183.170:5869:rahul222:rahul222",
"154.85.126.123:5130:rahul222:rahul222",
"216.173.88.13:6362:rahul222:rahul222",
"64.137.89.78:6151:rahul222:rahul222",
"104.239.41.212:6567:rahul222:rahul222",
"45.192.143.170:5243:rahul222:rahul222",
"104.239.37.121:5773:rahul222:rahul222",
"64.137.62.135:5780:rahul222:rahul222",
"104.239.23.118:5879:rahul222:rahul222",
"161.123.208.240:6484:rahul222:rahul222",
"109.196.163.132:6230:rahul222:rahul222",
"64.137.75.132:6052:rahul222:rahul222",
"93.120.32.13:9197:rahul222:rahul222",
"45.192.146.180:6191:rahul222:rahul222",
"45.192.140.47:6637:rahul222:rahul222",
"107.181.130.236:5857:rahul222:rahul222",
"161.123.93.244:5974:rahul222:rahul222",
"192.241.112.107:7609:rahul222:rahul222",
"104.239.76.176:6835:rahul222:rahul222",
"188.74.168.148:5189:rahul222:rahul222",
"154.85.125.52:6263:rahul222:rahul222",
"103.53.216.62:5146:rahul222:rahul222",
"103.99.33.128:6123:rahul222:rahul222",
"64.137.65.63:6742:rahul222:rahul222",
"64.137.65.88:6767:rahul222:rahul222",
"64.137.104.93:5703:rahul222:rahul222",
"64.137.88.39:6278:rahul222:rahul222",
"104.143.229.197:6125:rahul222:rahul222",
"109.207.130.12:8019:rahul222:rahul222",
"104.239.0.11:5712:rahul222:rahul222",
"161.123.65.204:6913:rahul222:rahul222",
"104.239.84.176:6211:rahul222:rahul222",
"103.75.228.9:6088:rahul222:rahul222",
"216.19.205.155:6476:rahul222:rahul222",
"103.99.33.232:6227:rahul222:rahul222",
"43.245.116.157:6672:rahul222:rahul222",
"216.173.103.141:6655:rahul222:rahul222",
"45.192.155.198:7209:rahul222:rahul222",
"103.101.88.222:5946:rahul222:rahul222",
"104.239.86.37:5947:rahul222:rahul222",
"185.48.55.162:6638:rahul222:rahul222",
"216.173.105.208:6065:rahul222:rahul222",
"103.101.88.197:5921:rahul222:rahul222",
"103.101.90.119:6384:rahul222:rahul222",
"207.244.217.10:6557:rahul222:rahul222",
"103.101.90.159:6424:rahul222:rahul222",
"119.42.36.134:6034:rahul222:rahul222",
"45.249.106.66:5763:rahul222:rahul222",
"207.244.217.81:6628:rahul222:rahul222"
]

proxies = [{"http": f"http://{''.join(proxy.split(':')[2:])}@{proxy.split(':')[0]}:{proxy.split(':')[1]}"} for proxy in proxy_list]


# proxies = []

# for proxy in proxy_list :
#     proxies.append(f"http://{proxy.split(':')[2]}:{proxy.split(':')[3]}@{proxy.split(':')[0]}:{proxy.split(':')[1]}")



# print(proxies)

# # save proxies to a json file
with open('proxies.json', 'w') as f:
    json.dump(proxies, f)
