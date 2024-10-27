import requests

# so in the below code getting my ip from check ip then 
my_url = "http://checkip.dyndns.org"
requests = requests.get(my_url)
print(requests)
print(type(requests))
result = requests.text.split(': ', 1)[1]
print(result)
my_ip = result.split('</body></html>', 1)[0]
print(my_ip)
