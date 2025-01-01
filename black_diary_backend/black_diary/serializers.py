import rest_framework
from .models import NewPage


class EntrieSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = NewPage
        fileds = [
            "id",
            "title",
            "text",
            "image",
            "timestamp",
        ]
