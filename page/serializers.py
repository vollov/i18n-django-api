from models import Page, PageTranslation
from rest_framework import serializers


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title', 'slug', 'posted')

class PageTranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageTranslation
        fields = ('id', 'title', 'page', 'language')