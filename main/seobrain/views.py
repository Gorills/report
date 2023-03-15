from django.shortcuts import render, redirect
import requests

from home.models import Project
# Create your views here.



API_KEY = '7e48bee7-9c47-412c-bb1f-989829265777'

hed = {
   'Authorization': API_KEY
}

url = 'http://api.seobrain.ru/v1_1/projects'
data = {'key': 'value'}

import json

site = 'flowerskam.ru'

def get_w(site):
    response = requests.get(url=url, json=data, headers=hed)
    items = response.json()

    for item in items['projects']:
        key = str(item)
        projectIdHash = key
        domain = items['projects'][key]['site']['cleanDomain']
        active = items['projects'][key]['active']
        # print(key, domain, active)

        
        if domain == site and active == 1:
            pr_dates = requests.get(url=f'http://api.seobrain.ru/v1_1/projects/{projectIdHash}/parsingDates', headers=hed)
            all_dates = pr_dates.json()

            data_first = all_dates['parsingDates'][-2]
            data_last = all_dates['parsingDates'][-1]
            

            data_get = {'dates': data_first+','+data_last}

            pos_request = requests.get(url=f'http://api.seobrain.ru/v1_1/projects/{projectIdHash}/positions', params=data_get, headers=hed)


            for gr in pos_request.json()['groups']:
                
                # Имя группы запросов
                group_name = pos_request.json()['groups'][gr]['groupName']
                positions = pos_request.json()['groups'][gr]['positions']

                for pos in positions:
                    # id ключевого слова
                    req_id = pos

                    # Текущая позиция 
                    tec_pos_ya = positions[req_id]['yandex'][data_first]['position']
                    tec_pos_go = positions[req_id]['google'][data_first]['position']


                    print(tec_pos_ya)
                    print(tec_pos_go)


            # print(pos_request.json())
        
        # for all in all_requests['groups']:
            
        #     print(all_requests['groups'][all]['groupName'])
            


    

# get_w(site)


def seo(request):
    pass


def seo_update(request, pk):
    if request.method == 'POST':
        
        project = Project.objects.get(id=pk)
        project_url = project.link


        response = requests.get(url=url, json=data, headers=hed)
        items = response.json()

        print(items)

        for item in items['projects']:
            key = str(item)
            projectIdHash = key
            domain = items['projects'][key]['site']['cleanDomain']
            active = items['projects'][key]['active']

            print(domain)
            print(project_url)

            if str(domain) == str(project_url):
                print('!!!')
            
                


        

        return redirect('/')





