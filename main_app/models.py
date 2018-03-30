from django.db import models

PROVINCE_CHOICE = (
    ('AB','Alberta'),
    ('BC','British Columbia'),
    ('MB','Manitoba'),
    ('NB','New brunswick'),
    ('NL','Newfoundland and Labrador'),
    ('NS','Nova Scotia'),
    ('NT','Northwest Territories'),
    ('ON','Ontario'),
    ('PE','PEI'),
    ('QC','Quebec'),
    ('SK','Saskatchewan'),
    ('YT','Yukon'),
)

class MyModel(models.Model):
  province = models.CharField(max_length=12, choices=PROVINCE_CHOICE , default='Alberta')
