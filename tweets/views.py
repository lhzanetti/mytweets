from django.views.generic import View
from django.shortcuts import render
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django Teste"
        return render(request, 'base.html', params)

