from django.db import models
from django.utils import timezone


class Pdf(models.Model):
	url = models.CharField(max_length=200,default="")
	page_num = models.PositiveSmallIntegerField(default=0)
	page_date = models.DateField(blank=True, null=True)
	checked = models.BooleanField(default=False)


	def publish(self, page_num, page_date):
		self.page_num = page_num
		self.page_date = page_date
		self.save()

