from django.shortcuts import render
from dj_docker_drf.postgres_db import Postgres_db

from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse


class HomeView(APIView):

    def get(self, request, format=None):
        print(request)
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
            # print(json)
            return HttpResponse(f"""
            <div>
                <h1>Home</h1>
            {json}
            </div>
            """)
        return JsonResponse({"message":
                             'Error getting ddata from server'})
