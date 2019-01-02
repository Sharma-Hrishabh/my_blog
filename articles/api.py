from .models import Articles
from .serializers import ArticleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleList(APIView):
    def get(self,request,format=None):
        articles = Articles.objects.all()
        serialized_articles = ArticleSerializer(articles,many=True)
        return Response(serialized_articles.data)


class ArticleDetail(APIView):
    def get_object(self,pk):
        try:
            return Articles.objects.get(pk=pk)
        except Articles.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        article = self.get_object(pk)
        serialized_article = ArticleSerializer(article)
        return Response(serialized_article.data)
