import json
from datetime import datetime

outputFile=open('output.json')
data=json.load(outputFile)
jsonGenerator=[]
summaryFile=open('summaryFile.json','w')
for i in range(0,len(data)-1,2):

        sessionRecord = {}
        sessionRecord['sessionStart']=data[i]['timestamp']
        sessionRecord['sessionEnd']=data[i+1]['timestamp']
        sessionRecord['sessionDuration']=str(int(data[i+1]['timestamp'])-int(data[i]['timestamp']))
        dt = datetime.fromtimestamp(int(sessionRecord['sessionStart']))
        dt2=datetime.fromtimestamp(int(sessionRecord['sessionEnd']))
        dt3=dt2-dt
        if(dt3.total_seconds()/3600>24):
                sessionRecord['ReturnedLate']=True
        else:
                sessionRecord['ReturnedLate'] = False
        if data[i+1]['comments']!="":
                sessionRecord["CarDamaged"]=True
        else:
                sessionRecord["CarDamaged"]=False




        jsonGenerator.append(sessionRecord)
json.dump(jsonGenerator,summaryFile,indent=5)
summaryFile.close()
outputFile.close()