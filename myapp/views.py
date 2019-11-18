from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h2>Hello,Welcome to Django..!</h2>")


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)  # rendering the template in HttpResponse


# ----------------------------------------------------------------------

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound


def error(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')  # rendering the template in HttpResponse


# --------------------------------------------------------

# from django.shortcuts import render
# from django.http import HttpResponse,HttpResponseNotFound
# from django.views.decorators.http import require_http_methods

# @require_http_methods(["GET","POST"])
# def show(request):
# return HttpResponse("<h1>This is the GET request..!</h1>")

# -----------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader


def cust(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def cust1(request):
    template=loader.get_template('index.html')
    name={
        'student':'rahul'
    }
    return HttpResponse(template.render(name))
"""


def image(request):
    return render(request, 'index.html')


def css(request):
    return render(request, 'index1.html')

#-----------------------------------------------------------
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response

from django.http import HttpResponse
from django.shortcuts import render

def setsession(request):
    request.session['sname']='rahul'
    request.session['semail'] = 'vibhuterahuls@gmail.com'
    return HttpResponse("session is set..!")

def getsession(request):
    studentname=request.session['sname']
    studentemail=request.session['semail']
    return HttpResponse(studentname+" - "+studentemail)

"""
from django.shortcuts import render
from django.http import HttpResponse


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response


def getcookie(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: " + tutorial)