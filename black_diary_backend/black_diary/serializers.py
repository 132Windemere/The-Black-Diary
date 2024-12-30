import rest_framework
from .models import Entrie


class EntrieSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Entrie
        fileds = [
            "id",
            "title",
            "text",
            "image",
            "timestamp",
        ]
