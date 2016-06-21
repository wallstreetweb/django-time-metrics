from django.contrib.contenttypes.models import ContentType
from django.db import models

from .utils import week_for_date, month_for_date, quarter_for_date, year_for_date


class MetricAbstractQuerySet(models.query.QuerySet):
    def filter_for_object(self, object):
        object_content_type = ContentType.objects.get_for_model(object)
        return self.filter(content_type__pk=object_content_type.id, object_id=object.id)


class MetricItemQuerySet(MetricAbstractQuerySet):
    pass


class DayMetricQuerySet(MetricAbstractQuerySet):
    def filter_by_date(self, date):
        return self.filter(date_up=date)


class WeekMetricQuerySet(MetricAbstractQuerySet):
    def filter_by_date(self, date):
        return self.filter(date_up=week_for_date(date))


class MonthMetricQuerySet(MetricAbstractQuerySet):
    def filter_by_date(self, date):
        return self.filter(date_up=month_for_date(date))


class QuarterMetricQuerySet(MetricAbstractQuerySet):
    def filter_by_date(self, date):
        return self.filter(date_up=quarter_for_date(date))


class YearMetricQuerySet(MetricAbstractQuerySet):
    def filter_by_date(self, date):
        return self.filter(date_up=year_for_date(date))
