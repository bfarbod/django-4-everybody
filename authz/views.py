from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode

# Create your views here.
class OpenView(View):

    def get(self, request):
        return render(request, 'authz/main.html')


class ManualProtect(View):

    def get(self, request):
        if not request.user.is_authenticated:
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)

        return render(request, 'authz/main.html')


class ProtectView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'authz/main.html')