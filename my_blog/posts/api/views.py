from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import  Post
from posts.api.serializers import PostSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly
class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = ['get']



#class PostApiViewSet(ViewSet):
#    def list(self, request):
#        #posts = Post.objects.all()
#        serializer = PostSerializer(Post.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#    def retrieve(self, request, pk: int):
#        post = PostSerializer(Post.objects.get(pk=pk))
#        return Response(status=status.HTTP_200_OK, data=post.data)
#    
#    def create(self, request):
#        serializer = PostSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_200_OK, data=serializer.data)

#class PostApiView(APIView):
#    def get(self, request):
#        #posts = Post.objects.all()
#        serializer = PostSerializer(Post.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#    
#    def post(self, request):
#        serializer = PostSerializer(data=request.POST)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(status=status.HTTP_200_OK, data=serializer.data)