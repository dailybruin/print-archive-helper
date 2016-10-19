import os
from .models import Pdf

print("Populating db")
Pdf.objects.create(url="https://archive.org/stream/ucladailybruin01losa#page/n6/mode/1up")
