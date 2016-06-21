from wsw_stats.utils import get_backend


def put_metric(slug, object=None, count=1, **kwargs):
    backend = get_backend()
    backend.put_metric(slug, object=object, count=count, **kwargs)