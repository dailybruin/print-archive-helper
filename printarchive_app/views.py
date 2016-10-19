from django.shortcuts import render
from .models import Pdf

def show_pdf(request):
	pdfs = Pdf.objects.all()
	return render(request, 'printarchive_app/show_pdf.html', {'pdfs': pdfs})