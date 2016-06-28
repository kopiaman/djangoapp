from rest_framework import serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


serializer = SnippetSerializer()
print(repr(serializer))        