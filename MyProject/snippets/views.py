# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False, status=200)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk = pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data, status=200)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
#
#     elif request.method == 'PATCH':
#         data = JSONParser().parse(request)
#         #부분 업데이트 허용 partial=True
#         serializer = SnippetSerializer(snippet, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)


# 뷰셋 방식
from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # 뷰셋을 사용하면 기본적인 CRUD를 제공함
    #•	목록 조회 (GET): http://127.0.0.1:8000/api/snippets/
    #   •	모든 Snippet 객체의 목록을 조회합니다.
    #•	상세 조회 (GET): http://127.0.0.1:8000/api/snippets/1/
    #   •	특정 Snippet 객체의 상세 정보를 조회합니다.
    #•	생성 (POST): http://127.0.0.1:8000/api/snippets/
    #   •	새로운 Snippet 객체를 생성합니다.
    #•	수정 (PUT): http://127.0.0.1:8000/api/snippets/1/
    #   •	특정 Snippet 객체를 수정합니다.
    #•	부분 수정 (PATCH): http://127.0.0.1:8000/api/snippets/1/
    #   •	특정 Snippet 객체를 부분적으로 수정합니다.
    #•	삭제 (DELETE): http://127.0.0.1:8000/api/snippets/1/
    #   •	특정 Snippet 객체를 삭제합니다.