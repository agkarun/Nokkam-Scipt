import json
import requests
import os
##Subjects to be downloaded as per Json file
subjects=['Biology','Chemistry','CurrentAffairs','Economics','English',
         'Geography','History','Physics','Polity','Psycology','Tamil']
for subject in subjects:
    print(subject)
##if the download is interrupted we can continue from the interrupted subject
##    if subject=='Biology' or subject=='Chemistry' or subject=='CurrentAffairs' or subject=='Economics' or subject=='English' or subject=='Geography' or subject=='History' or subject=='Physics' or subject=='Polity':
##        continue
##    else:
##
##Creating folder for each subject
    os.mkdir('C:\\Users\\Karun\\Desktop\\Nokkam_Notes\\'+subject)
##Opening dowloaded json file
    json_file = open('C:\\Users\\Karun\\Desktop\\Nokkam_Notes\\'+subject+'.json',encoding="utf-8")
#loading json as dictionary
    data = json.load(json_file)
##Getting all data inside items tag
    urls=data['data']['getAllExamOrderedNotes']['items']
##Traversing into items tag and getting url for pdf
    for i in range(len(urls)):
        try:
            url=str(urls[i]['exam_note']['url'])
            filename='C:\\Users\\Karun\\Desktop\\Nokkam_Notes\\'+subject+'\\'+str(urls[i]['exam_note']['name'])
            response = requests.get(url)
            with open(filename+'.pdf','wb') as f:
                f.write(response.content)
                print('Downloaded===>'+subject+':'+str(urls[i]['exam_note']['name']))
        except Exception as exception:
            print(exception)
