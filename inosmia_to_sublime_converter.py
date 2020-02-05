import json,requests,time
finaldata=[]
headers = "',headers = headers"
f= open('/home/aditya/Downloads/ltm31jan.json')
data = json.load(f)
for item in data["resources"]:
	if item.get("url") is not None and item.get("method") is not None and item.get("body") is not None and item.get("headers") is not None:
		_body = item.get("body")
		if _body.get('text') is not None or _body.get('text') =='{}':  
			try:
				url=item.get("url")
				
				http_method=item.get("method").lower()    #to change Upper letters to lower letters
				
				body=json.loads(_body["text"])
				url = url.replace("{{host}}","http://13.233.111.6:3500")
				url=url.replace("{{ host  }}","http://13.233.111.6:3500")
				jsonPayload = json.loads(_body["text"])
				# print(jsonPayload)
				strPayload = json.dumps(jsonPayload , indent=4)
				# strPayload = strPayload.replace('\\n','')
				# print(json.dumps(jsonPayload , indent=4)) #pretty print
				# strPayload = strPayload.replace("'",'"').replace('u"','"')
				proper_data=http_method+"('"+url+headers+","+"json ="+strPayload+")"

				finaldata.append(proper_data)
				
			except Exception as e:
				print(e)
try:
	with open('demo1.txt', 'w') as f:
	    for item in finaldata:
	        f.write("%s\n" % item)
	        print("%s\n" % item)

	print("completed")
except Exception as e:
	print(e)

