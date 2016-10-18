from django.db import models
from django.utils import timezone


class Pdf(models.Model):
	url = models.CharField(max_length=200,default="")
	date_1_page_num = models.PositiveSmallIntegerField(default=0)
	date_1_page_date = models.DateField(blank=True, null=True)
	date_2_page_num = models.PositiveSmallIntegerField(default=0)
	date_2_page_date = models.DateField(blank=True, null=True)
	checked = models.BooleanField(default=False)


	def publish(self, date_1_page_num,date_1_page_date, date_2_page_num, date_2_page_date):
		self.date_1_page_num = date_1_page_num
		self.date_1_page_date = date_1_page_date
		self.date_2_page_num = date_2_page_num
		self.date_2_page_date = date_2_page_date
		self.checked = True
		self.save()

