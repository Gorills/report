from django.shortcuts import render
import requests

# Create your views here.


def metrika(request):

    pass



ID = '5867e645e92b4eaaa346db90da388c6e'
pswd = '90f13a08cafb414c9c283179d9778a8d'
token = 'AQAAAAA7FE4_AAgNEuafgpWJdkediO2fjYuVmts'

hed = {
    'Host': 'api-metrika.yandex.net',
    'Authorization': 'OAuth ' + token,
    'Content-Type': 'application/x-yametrika+json',
    'Content-Length': '123'

}

url = 'https://api-metrika.yandex.net/stat/v1/data?preset=sources_summary&id='+'89234114'

def get_met():

    response = requests.get(url, headers = hed)
    print(response.text)




# get_met()
