from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import EntrieSerializer
from .models import NewPage
from django.db.models import Q
from datetime import datetime


class EntrieLlistCreateView(generics.ListCreateAPIView):
    serializer_class = EntrieSerializer

    def get_queryset(self):
        queryset = NewPage.objects.all().order_by("-timestamp")
        search_query = self.request.query_params.get("search", None)
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)
        month = self.request.query_params.get("month", None)
        year = self.request.query_params.get("year", None)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(text__icontains=search_query)
            )
            try:
                search_date = datetime.strptime(search_query, "%Y-%m-%d")
                queryset = queryset.filter(timestamp__date=search_date.date())
            except ValueError:
                pass

        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                queryset = queryset.filter(timestamp__gte=start_date_obj)
            except ValueError:
                pass

        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                queryset = queryset.filter(timestamp__lte=end_date_obj)
            except ValueError:
                pass

        if month:
            try:
                month = int(month)
                queryset = queryset.filter(timestamp__month=month)
            except ValueError:
                pass

        if year:
            try:
                year = int(year)
                queryset = queryset.filter(timestamp__year=year)
            except ValueError:
                pass

        return queryset


class EntrieDetailView(generics.RetrieveAPIView):
    queryset = NewPage.objects.all()
    serializer_class = EntrieSerializer


class EntryDeleteView(generics.DestroyAPIView):
    queryset = NewPage.objects.all()
    serializer_class = EntrieSerializer
