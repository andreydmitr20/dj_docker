from django.shortcuts import render
from dj_docker_drf.postgres_db import Postgres_db

from rest_framework.views import APIView
from django.http import JsonResponse


class HomeView(APIView):

    def get(self, request, format=None):
        print(request)
        # return JsonResponse({"message":
        #  'HELLO D112 FROM DJANGO AND DOCKER'})
        d = Postgres_db('postgres',
                        'postgres',
                        'changeme')
        d.connect()
        json = {}
        if (d.is_connected()):
            json = d.get_json(
                '''SELECT * from "user"''',
                'user_id',
                ['name', 'api_key'])
            d.disconnect()
            print(json)
            return JsonResponse(json)
        return JsonResponse({"message":
                             'Error getting ddata from server'})
