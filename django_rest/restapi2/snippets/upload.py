import requests

url="http://localhost:8000/snippets/1/"
params={
	"id":1,
}
data={
	"title":"helll",
	"code":"regex",
	"linenos":True,
}

r=requests.get(url=url,params=params)
print(r.text)
