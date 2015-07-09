from models import Page, PageTranslation
from rest_framework import viewsets
from serializers import PageSerializer, PageTranslationSerializer
 
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
 
from rest_framework.views import APIView
from rest_framework.response import Response

class PageView(APIView):
    def get(self, request, lang, format=None):
        print lang
        pages = PageTranslation.objects.get(language='en')
        serializer = PageTranslationSerializer(pages, many=True)
        return Response(serializer.data)
    
class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageTranslationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PageTranslation.objects.all()
    serializer_class = PageTranslationSerializer