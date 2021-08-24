import requests
import json
import urllib3

f2 = open("output.txt","w")




# Added by me.
f = open("inputs.txt", "r")
string = f.read().rstrip().split()
# print (string)

for x in string:
	# print (x)
	headers = {
			'Origin': 'https://172.27.26.181:9998',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
			'Content-Type': 'text/plain',
			'Accept': '*/*',
			'Referer': 'https://172.27.26.181:9998/eaeae',
			'X-Requested-With': 'ShockwaveFlash/32.0.0.142',
			'Connection': 'keep-alive',
	}
	data = '{"password":"f6e39f49461e278158f51a92e8ca0d84","teamname":"Obfuscated","plaintext":"'+str(x)+'"}'
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	response = requests.post('https://172.27.26.181:9998/eaeae', headers=headers, data=data, verify=False)
	json_data = json.loads(response.content)
	f2.write(json_data["ciphertext"])
	
	f2.write(" ")
	# p = re.search('name="clear_text">(.*)</textarea>', str(resp.content))
	# print(p.group(1))
	print ("Alive\n");

f.close()
f2.close()






