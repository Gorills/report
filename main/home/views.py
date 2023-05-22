



from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum

import requests

from django.http import HttpResponse
from django.views.decorators.http import require_GET
from home.models import Dates, Project, Report, SearchEngine, Works, Group, Word, Position, Rek, Files

from pytils.translit import slugify
from bs4 import BeautifulSoup
import csv
from metrika.views import get_met

import urllib
import os

# get_met()





def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def home(request):

    context = {
       'projects': Project.objects.all()
    }

    return render(request, 'home/index.html', context)




headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
def add(request):

    if request.method == 'POST':

        name = request.POST['name']
        link = request.POST['link']
        slug = slugify(name)
        
               

        model = Project(name=name, link=link, slug=slug)
        model.save()


        return redirect(model.get_absolute_url())


    return render(request, 'home/project_add.html')


def delete(request, pk):


    model = Project.objects.get(id=pk)
    model.delete()

    return redirect('/')


def project_detail(request, slug):



    if request.method == "POST":
        project = Project.objects.get(slug=slug)

        start = request.POST['start']
        end = request.POST['end']
        work_name = request.POST.getlist('work_name')
        work_date = request.POST.getlist('work_date')
        work_time = request.POST.getlist('work_time')
        rek = request.POST.getlist('rek')
        files = request.FILES.getlist('images')

        report = Report(parent=project, start=start, end=end)
        report.save()


        for file in files:
            if file != '':
                file_model = Files(file=file, parent=report)
                file_model.save()

        for r in rek:
            if r != '':
                rek = Rek(parent=report, text=r)
                rek.save()

        c = 0
        for t in work_time:
            if t != '':
                work = Works(parent=report, name=work_name[c], date=work_date[c], time=t)
                work.save()
                c += 1

        google = request.FILES['google']
        yandex = request.FILES['yandex']

        with open('google.csv','wb') as output:
            output.write(google.read())

        with open('yandex.csv','wb') as output:
            output.write(yandex.read())
       
        try:
            with open('google.csv', encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter = ";")
                count = 0
                group_id = ''
                search = SearchEngine(name='Google', parent=report)
                search.save()
                for row in file_reader:

                    if count == 0:
                        
                        count += 1
                        for r in row[1:]:
                            dates = Dates(parent=search, date=r)
                            dates.save()
   
                    if row[0] != '':
                     
                        if 'Группа' in row[0]:

                            group = Group(name=row[0], parent=search)
                            
                            group.save()
                            group_id = group.id

                        else:

                            word = Word(name=row[0], parent_id=group_id)
                            word.save()
                            word_id = word.id 
                            
                            for r in row[1:]:

                                if r == '-':
                                    position = Position(pos=100, parent_id=word_id, color='none')
                                    position.save()
                                else:
                                    position = Position(pos=r, parent_id=word_id, color='none')
                                    position.save()
                            

                        count += 1
                    

                print(f'Всего в файле {count} строк.')

        except Exception as e:
            print(e)

        try:
            with open('yandex.csv', encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter = ";")
                count = 0
                group_id = ''
                search = SearchEngine(name='Yandex', parent=report)
                search.save()
                for row in file_reader:

                    if count == 0:
                        
                        count += 1
                        for r in row[1:]:
                            dates = Dates(parent=search, date=r)
                            dates.save()
   
                    if row[0] != '':
                     
                        if 'Группа' in row[0]:

                            group = Group(name=row[0], parent=search)
                            
                            group.save()
                            group_id = group.id

                        else:

                            word = Word(name=row[0], parent_id=group_id)
                            word.save()
                            word_id = word.id 
                            
                            for r in row[1:]:

                                if r == '-':
                                    position = Position(pos=100, parent_id=word_id, color='none')
                                    position.save()
                                else:
                                    position = Position(pos=r, parent_id=word_id, color='none')
                                    position.save()
                            

                        count += 1
                    

                print(f'Всего в файле {count} строк.')

        except Exception as e:
            print(e)

    context = {

        'project': Project.objects.get(slug=slug)
    }


    return render(request, 'home/project.html', context)


def report_edit(request, pk):


    context = {
        'report': Report.objects.get(id=pk)
    }


    return render(request, 'home/report_edit.html', context=context)


def report_detail(request, parent, pk):

    report = Report.objects.get(pk=pk)
    search = SearchEngine.objects.filter(parent_id=pk).first()

    count = Dates.objects.filter(parent=search).count()

    hours = Works.objects.filter(parent=report)

    hour = 0
    for h in hours:
        hour = hour + int(h.time)
    

    context = {

        'report': report,
        # добавляем два столбца к таблице мониторинга позиций
        'count' : count + 2,
        'hours': hour

    }



    return render(request, 'home/report.html', context=context)




def img_remove(request, pk):


    file = Files.objects.get(id=pk)
    parent = file.parent.id

    file.delete()

    return redirect('/report/edit/' + str(parent) + '/')