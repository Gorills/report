
from django.db import models
from django.urls import reverse


from urllib.parse import unquote


class Project(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    logo = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


    def get_link(self):

        res = unquote(self.link, 'idna')
        
        return res



class ProjectWords(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    word = models.CharField(max_length=250)
    parent = models.ForeignKey(Project, on_delete=models.CASCADE)
    


class Report(models.Model):
    parent = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reports')
    date = models.DateTimeField(auto_now_add=True)

    start = models.DateField()
    end = models.DateField()

    def get_absolute_url(self):
        return reverse("report_detail", kwargs={"parent": self.parent.slug, "pk": self.pk})
    


class Rek(models.Model):

    parent = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='reks')
    text = models.TextField()


    

class SearchEngine(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='search')


class Dates(models.Model):
    parent = models.ForeignKey(SearchEngine, on_delete=models.CASCADE, related_name='dates')
    date = models.CharField(max_length=250)

class Group(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(SearchEngine, on_delete=models.CASCADE, related_name='groups')
    

class Word(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='words')


    def last_null(self):

        last = Position.objects.filter(parent_id=self.id).last()
        pos = last.pos
        
        return pos
    

class Position(models.Model):
    
    pos = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='positions')
    date = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=200, null=True, blank=True)

    def position_prev(self):
        main_id = self.id
        old_id = main_id - 1

        pos = self.pos
        old_pos = Position.objects.get(id=old_id).pos
        if old_pos > pos:
            res = 'True'
            return res
        if old_pos < pos:
            res = 'False'
            return res
        else:
            res = 'None'
            return res
        




class Works(models.Model):
    parent = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='works')
    name = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=200)



class Files(models.Model):
    file = models.ImageField(upload_to='report')
    parent = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='files')