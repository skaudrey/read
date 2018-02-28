from django.shortcuts import render
from .models import Student
from django.shortcuts import HttpResponse
from django.db.models.aggregates import Count
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template

# Create your views here.
#定义公用模块的位置
def index(request):
    # 爱心人士获取学生信息列表
    studentList = Student.objects.filter(status=0)
    return render(request,'shareRead/students.html', {'studentList': studentList, 'size': len(studentList)})
def about(request):
    return render(request,'shareRead/aboutus.html')
def error(request):
    return render(request, 'shareRead/error.html')

@csrf_exempt
def regDiv(request):
    if request.is_ajax():
        cityList = Student.objects.values("schoolCity").annotate(cities=Count("schoolCity")).filter(status=0).order_by("schoolCity")
        regList = Student.objects.filter(status=0).order_by('schoolCity')
        print(cityList)
        t = get_template('shareRead/regList.html') # get the contex of html
        content_html = t.render({'regList': regList, 'cityList': cityList}) # render the template to the local html you want,rather than return a variable
        return HttpResponse(content_html)

# def intologin(request):
#     return render(request, 'shareRead/login.html')


