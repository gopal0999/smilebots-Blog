from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, PostActionSerializer, PostCreateSerializer

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html", context={}, status=200)

@api_view(['POST'])
# @authentication_classes([SessionAuthentication]) # by default in rest_framework
# @permission_classes([IsAuthenticated])
def post_create_view(request):
    serializer = PostCreateSerializer(data=request.POST or None)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return JsonResponse(serializer.data, status = 201)
    return JsonResponse({}, status=400)

@api_view(['GET'])
def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    serializedPosts = PostSerializer(qs, many=True)
    return Response(serializedPosts.data, status=200)