# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Metric,
	AbstractMetric,
	DayMetric,
	WeekMetric,
	MonthMetric,
	QuarterMetric,
	YearMetric,
)


class MetricCreateView(CreateView):

    model = Metric


class MetricDeleteView(DeleteView):

    model = Metric


class MetricDetailView(DetailView):

    model = Metric


class MetricUpdateView(UpdateView):

    model = Metric


class MetricListView(ListView):

    model = Metric


class AbstractMetricCreateView(CreateView):

    model = AbstractMetric


class AbstractMetricDeleteView(DeleteView):

    model = AbstractMetric


class AbstractMetricDetailView(DetailView):

    model = AbstractMetric


class AbstractMetricUpdateView(UpdateView):

    model = AbstractMetric


class AbstractMetricListView(ListView):

    model = AbstractMetric


class DayMetricCreateView(CreateView):

    model = DayMetric


class DayMetricDeleteView(DeleteView):

    model = DayMetric


class DayMetricDetailView(DetailView):

    model = DayMetric


class DayMetricUpdateView(UpdateView):

    model = DayMetric


class DayMetricListView(ListView):

    model = DayMetric


class WeekMetricCreateView(CreateView):

    model = WeekMetric


class WeekMetricDeleteView(DeleteView):

    model = WeekMetric


class WeekMetricDetailView(DetailView):

    model = WeekMetric


class WeekMetricUpdateView(UpdateView):

    model = WeekMetric


class WeekMetricListView(ListView):

    model = WeekMetric


class MonthMetricCreateView(CreateView):

    model = MonthMetric


class MonthMetricDeleteView(DeleteView):

    model = MonthMetric


class MonthMetricDetailView(DetailView):

    model = MonthMetric


class MonthMetricUpdateView(UpdateView):

    model = MonthMetric


class MonthMetricListView(ListView):

    model = MonthMetric


class QuarterMetricCreateView(CreateView):

    model = QuarterMetric


class QuarterMetricDeleteView(DeleteView):

    model = QuarterMetric


class QuarterMetricDetailView(DetailView):

    model = QuarterMetric


class QuarterMetricUpdateView(UpdateView):

    model = QuarterMetric


class QuarterMetricListView(ListView):

    model = QuarterMetric


class YearMetricCreateView(CreateView):

    model = YearMetric


class YearMetricDeleteView(DeleteView):

    model = YearMetric


class YearMetricDetailView(DetailView):

    model = YearMetric


class YearMetricUpdateView(UpdateView):

    model = YearMetric


class YearMetricListView(ListView):

    model = YearMetric

