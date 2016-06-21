from .models import Metric, MetricItem


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
