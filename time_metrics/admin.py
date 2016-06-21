from django.contrib import admin
from django.utils import dateformat
from django.utils.translation import ugettext_lazy as _

from .models import Metric, MetricItem, DayMetric, WeekMetric, MonthMetric, QuarterMetric, YearMetric
from .utils import get_quarter_number


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MetricItem)
class MetricItemAdmin(admin.ModelAdmin):
    list_display = ('metric', 'content_type', 'object_id', 'content_object', 'count', 'date_up')
    list_filter = ('metric', 'content_type', 'object_id',)


@admin.register(DayMetric)
class DayMetricAdmin(admin.ModelAdmin):
    list_display = ('metric', 'content_type', 'object_id', 'content_object', 'count', 'when', )
    list_filter = ('metric', 'content_type', 'object_id', )

    def when(self, obj):
        return dateformat.format(obj.date_up, "d b. Y")
    when.short_description = _('When')
    when.admin_order_field = 'date_up'


@admin.register(WeekMetric)
class WeekMetricAdmin(admin.ModelAdmin):
    list_display = ('metric', 'content_type', 'object_id', 'content_object', 'count', 'when', )
    list_filter = ('metric', 'content_type', 'object_id', )

    def when(self, obj):
        return _("Week %(week)s of year %(year)s") % {
            'week': dateformat.format(obj.date_up, "W"),
            'year': dateformat.format(obj.date_up, "Y")
        }
    when.short_description = _('When')
    when.admin_order_field = 'date_up'


@admin.register(MonthMetric)
class MonthMetricAdmin(admin.ModelAdmin):
    list_display = ('metric', 'content_type', 'object_id', 'content_object', 'count', 'when', )
    list_filter = ('metric', 'content_type', 'object_id', )

    def when(self, obj):
        return dateformat.format(obj.date_up, "F Y")
    when.short_description = _('When')
    when.admin_order_field = 'date_up'


@admin.register(QuarterMetric)
class QuarterMetricAdmin(admin.ModelAdmin):
    list_display = ('metric', 'content_type', 'object_id', 'content_object', 'count', 'when', )
    list_filter = ('metric', 'content_type', 'object_id', )

    def when(self, obj):
        return _("Quarter %(quarter)s of %(year)s") % {
            'quarter': get_quarter_number(obj.date_up, True),
            'year': dateformat.format(obj.date_up, "Y")
        }
    when.short_description = _('When')
    when.admin_order_field = 'date_up'


@admin.register(YearMetric)
class YearMetricAdmin(admin.ModelAdmin):
    list_display = ('metric', 'content_type', 'object_id', 'content_object', 'count', 'when', )
    list_filter = ('metric', 'content_type', 'object_id', )

    def when(self, obj):
        return dateformat.format(obj.date_up, "Y")
    when.short_description = _('When')
    when.admin_order_field = 'date_up'
