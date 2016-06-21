# -*- coding: utf-8 -*-
from datetime import date

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from .querysets import MetricItemQuerySet, DayMetricQuerySet, WeekMetricQuerySet, MonthMetricQuerySet, QuarterMetricQuerySet, YearMetricQuerySet


class Metric(TimeStampedModel):
    name = models.CharField(max_length=90)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('metric')
        verbose_name_plural = _('metrics')


class AbstractMetric(models.Model):
    metric = models.ForeignKey(Metric)
    count = models.IntegerField(default=0)
    date_up = models.DateField(default=date.today)

    site = models.ForeignKey(Site)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        values = dict(
            name=self.metric,
            count=self.count,
            date_up=self.date_up.strftime("%b. %d %Y")
        )
        if self.content_object:
            string = u"%(count)s '%(name)s' for '%(content_object)s' on %(date_up)s"
            values["content_object"] = self.content_object
        elif self.content_type and self.object_id:
            string = u"%(count)s '%(name)s' for ('%(content_type)s', '%(object_id)s') on %(date_up)s"
            values["content_type"] = self.content_type
            values["object_id"] = self.object_id
        else:
            string = u"%(count)s '%(name)s' for %(date_up)s"
        return string % values

    class Meta:
        abstract = True
        verbose_name = _('abstract metric item')
        verbose_name_plural = _('abstract metric items')


class MetricItem(AbstractMetric):
    objects = MetricItemQuerySet.as_manager()

    def save(self, *args, **kwargs):
        if self.count == 0:
            self.count = 1
        return super(MetricItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('metric item')
        verbose_name_plural = _('metric items')


class DayMetric(AbstractMetric):
    objects = DayMetricQuerySet.as_manager()

    def __str__(self):
        values = dict(
            name=self.metric.name,
            date_up=self.date_up.strftime("%b. %d %Y")
        )
        if self.content_object:
            string = u"'%(name)s' for '%(content_object)s' on %(date_up)s"
            values["content_object"] = self.content_object
        elif self.content_type and self.object_id:
            string = u"'%(name)s' for ('%(content_type)s', '%(object_id)s') on %(date_up)s"
            values["content_type"] = self.content_type
            values["object_id"] = self.object_id
        else:
            string = "'%(name)s' for '%(date_up)s'"
        return string % values

    class Meta:
        verbose_name = _('day metric')
        verbose_name_plural = _('day metrics')


class WeekMetric(AbstractMetric):
    objects = WeekMetricQuerySet.as_manager()

    def __str__(self):
        values = dict(
            name=self.metric.name,
            week=self.date_up.strftime("%U"),
            year=self.date_up.strftime("%Y")
        )
        if self.content_object:
            string = u"'%(name)s' for '%(content_object)s' on week %(week)s of year %(year)s"
            values["content_object"] = self.content_object
        elif self.content_type and self.object_id:
            string = u"'%(name)s' for ('%(content_type)s', '%(object_id)s') on week %(week)s of year %(year)s"
            values["content_type"] = self.content_type
            values["object_id"] = self.object_id
        else:
            string = "'%(name)s' for week %(week)s of year %(year)s"
        return string % values

    class Meta:
        verbose_name = _('week metric')
        verbose_name_plural = _('week metrics')


class MonthMetric(AbstractMetric):
    objects = MonthMetricQuerySet.as_manager()

    def __str__(self):
        values = dict(
            name=self.metric.name,
            month=self.date_up.strftime("%B"),
            year=self.date_up.strftime("%Y")
        )
        if self.content_object:
            string = u"'%(name)s' for '%(content_object)s' on %(month)s %(year)s"
            values["content_object"] = self.content_object
        elif self.content_type and self.object_id:
            string = u"'%(name)s' for ('%(content_type)s', '%(object_id)s') on %(month)s %(year)s"
            values["content_type"] = self.content_type
            values["object_id"] = self.object_id
        else:
            string = "'%(name)s' for %(month)s %(year)s"
        return string % values

    class Meta:
        verbose_name = _('month metric')
        verbose_name_plural = _('month metrics')


class QuarterMetric(AbstractMetric):
    objects = QuarterMetricQuerySet.as_manager()

    def __str__(self):
        values = dict(
            name=self.metric.name,
            quarter=get_quarter_number(self.date_up, True),
            year=self.date_up.strftime("%Y")
        )
        if self.content_object:
            string = u"'%(name)s' for '%(content_object)s' on quarter %(quarter)s of year %(year)s"
            values["content_object"] = self.content_object
        elif self.content_type and self.object_id:
            string = u"'%(name)s' for ('%(content_type)s', '%(object_id)s') on quarter %(quarter)s of year %(year)s"
            values["content_type"] = self.content_type
            values["object_id"] = self.object_id
        else:
            string = "'%(name)s' for %(year)s"
        return string % values

    class Meta:
        verbose_name = _('querter metric')
        verbose_name_plural = _('quarter metrics')


class YearMetric(AbstractMetric):
    objects = YearMetricQuerySet.as_manager()

    def __str__(self):
        values = dict(
            name=self.metric.name,
            year=self.date_up.strftime("%Y")
        )
        if self.content_object:
            string = u"'%(name)s' for '%(content_object)s' on %(year)s"
            values["content_object"] = self.content_object
        elif self.content_type and self.object_id:
            string = u"'%(name)s' for ('%(content_type)s', '%(object_id)s') on %(year)s"
            values["content_type"] = self.content_type
            values["object_id"] = self.object_id
        else:
            string = "'%(name)s' for %(year)s"
        return string % values

    class Meta:
        verbose_name = _('year metric')
        verbose_name_plural = _('year metrics')



