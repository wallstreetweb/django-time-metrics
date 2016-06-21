# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel


class Metric(TimeStampedModel):
    pass
    

class AbstractMetric(TimeStampedModel):
    pass
    

class DayMetric(TimeStampedModel):
    pass
    

class WeekMetric(TimeStampedModel):
    pass
    

class MonthMetric(TimeStampedModel):
    pass
    

class QuarterMetric(TimeStampedModel):
    pass
    

class YearMetric(TimeStampedModel):
    pass
    


