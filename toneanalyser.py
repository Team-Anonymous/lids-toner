import requests
import json
from audiorecord import *

wav_file_creator()
tone_ids=["anger","disgust","fear","sadness"]
data = open('src/wav/test.wav', 'rb').read()
resp = requests.post(url='http://lidsccsmartindiahackathon2017.mybluemix.net/speech',
                    data=data,
                    headers={'Content-Type': 'application/octet-stream'})
print("S")
getdata=json.loads(resp.content.decode('utf-8'))
tones=getdata["tone_categories"]
vals=''
for val in tones:
    if(val["category_id"]=="emotion_tone"):
        for scores in val["tones"]:
            if (scores["tone_id"] in tone_ids):
                print(str(scores["tone_id"])+" "+str(scores["score"]))
                vals+=str(scores["tone_id"])+" "+str(scores["score"])
        break;
date={}
data["violation"]=vals.decode
data["number"]="109"
data["action"]=1
data["alertpriority"]=100
userdata=json.dumps(data)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
resp=requests.post("http://lidsmysqldb.clouadpp.net/sih2017/lids-api/sendAlert.php",data)
