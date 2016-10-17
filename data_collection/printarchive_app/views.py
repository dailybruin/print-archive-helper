from django.shortcuts import render


def show_pdf(request):
    return render(request, 'printarchive_app/show_pdf.html', {})