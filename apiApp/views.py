from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from pymongo import MongoClient
from apiApp.models import (
    find_patterns,
    find_single_pattern,
    find_users,
    find_single_user,
    find_patterns_by_username,
    insert_pattern,
    insert_user,
    update_pattern,
    update_user,
    delete_items,
    find_comments,
    insert_comment,
    delete_comment
)
import json
from apiApp.endpoints import endpoints

from mongo_auth.permissions import AuthenticatedOnly
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import os
import urllib.parse 
from dotenv import load_dotenv
load_dotenv()

mongo_uri = str(os.getenv('MONGO_URI'))
client = MongoClient(mongo_uri)

db = client["multiply_till_you_die_db"]
patterns_collection = db["patterns"]
users_collection = db["users"]
comments_collection = db["comments"]

# Create your views here.
@api_view(["GET", "POST"])
def get_comments(request):
    if request.method == "GET":
        return Response({"comments": json.loads(find_comments(request, comments_collection))}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return insert_comment(request, comments_collection)

@api_view(["DELETE"])
def single_comment(request, id):
    if request.method == "DELETE":
        return delete_comment(id, comments_collection)

@api_view(["GET", "POST"])
def get_patterns(request):
    if request.method == "GET":
        return Response(
            {"patterns": json.loads(find_patterns(request, patterns_collection))},
            status=status.HTTP_200_OK,
        )
    elif request.method == "POST":
        return insert_pattern(request, patterns_collection, users_collection)


@api_view(["GET", "PUT", "DELETE"])
def single_pattern(request, id):
    if request.method == "GET":
        return find_single_pattern(request, id, patterns_collection)
    elif request.method == "PUT":
        return update_pattern(request, id, patterns_collection)
    elif request.method == "DELETE":
        return delete_items(id,patterns_collection)


@api_view(["GET", "POST"])
def get_users(request):
    if request.method == "GET":
        return Response(
            {"users": json.loads(find_users(request, users_collection))},
            status=status.HTTP_200_OK,
        )
    elif request.method == "POST":
        return insert_user(request, users_collection)

@api_view(["GET", "PUT", "DELETE"])
def get_single_user(request, id):
    if request.method == "GET":
        return find_single_user(id, users_collection)
    elif request.method == "PUT":
        return update_user(request, id, users_collection, patterns_collection)
    elif request.method == "DELETE":
        return delete_items(id,users_collection)


@api_view(["GET"])
def get_patterns_by_username(request, username):
    return find_patterns_by_username(username, patterns_collection, users_collection)

@api_view(["GET"])
def api_endpoints(request): return Response(endpoints)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def page_not_found(request, exception):
    return Response({"msg": "HTTP 404: not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def internal_server_error(arg):
    return Response({"msg": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
@permission_classes([AuthenticatedOnly])
def get_test(request):
   try:
       print(request.user)
       return Response(status=status.HTTP_200_OK,
                       data={"data": {"msg": "User Authenticated"}})
   except:
       return Response(status=status.HTTP_404_NOT_FOUND)