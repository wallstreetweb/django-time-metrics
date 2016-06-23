from .models import Metric, MetricItem, DayMetric, WeekMetric, MonthMetric, QuarterMetric, YearMetric
from .utils import week_for_date, month_for_date, quarter_for_date, year_for_date


def put_metric(slug, object=None, count=1, **kwargs):
    from django.conf import settings
    from django.contrib.sites.models import Site

    try:
        metric = Metric.objects.get(slug=slug)
    except Metric.DoesNotExist:
        metric = Metric.objects.create(slug=slug, name=slug)

    site = Site.objects.get(pk=settings.SITE_ID)

    MetricItem.objects.create(
        metric=metric,
        content_object=object,
        site=site,
        count=count
    )


def metrics_aggregate():
    items = MetricItem.objects.all()

    for item in items:
        metric_day, create = DayMetric.objects.get_or_create(
            metric=item.metric,
            content_type=item.content_type,
            object_id=item.object_id,
            site=item.site,
            date_up=item.date_up
        )
        metric_day.count = metric_day.count + item.count
        metric_day.save()

        # Weekly Aggregation
        week_date = week_for_date(item.date_up)
        metric_week, create = WeekMetric.objects.get_or_create(
            metric=item.metric,
            content_type=item.content_type,
            object_id=item.object_id,
            site=item.site,
            date_up=week_date
        )
        metric_week.count = metric_week.count + item.count
        metric_week.save()

        # Monthly aggregation
        month_date = month_for_date(item.date_up)
        metric_month, create = MonthMetric.objects.get_or_create(
            metric=item.metric,
            content_type=item.content_type,
            object_id=item.object_id,
            site=item.site,
            date_up=month_date
        )
        metric_month.count = metric_month.count + item.count
        metric_month.save()

        # Quarter aggregation
        quarter_date = quarter_for_date(item.date_up)
        metric_quarter, create = QuarterMetric.objects.get_or_create(
            metric=item.metric,
            content_type=item.content_type,
            object_id=item.object_id,
            site=item.site,
            date_up=quarter_date
        )
        metric_quarter.count = metric_quarter.count + item.count
        metric_quarter.save()

        # Yearly aggregation
        year_date = year_for_date(item.date_up)
        metric_year, create = YearMetric.objects.get_or_create(
            metric=item.metric,
            content_type=item.content_type,
            object_id=item.object_id,
            site=item.site,
            date_up=year_date
        )
        metric_year.count = metric_year.count + item.count
        metric_year.save()

    # remove all metric items
    items.delete()
