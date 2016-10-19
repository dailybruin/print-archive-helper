from django.shortcuts import render
from .models import Pdf
import csv

def show_pdf(request):
	pdfs = Pdf.objects.all()
	# Pdf.objects.create(url="https://archive.org/stream/ucladailybruin01losa#page/n6/mode/1up")
	return render(request, 'printarchive_app/show_pdf.html', {'pdfs': pdfs})
