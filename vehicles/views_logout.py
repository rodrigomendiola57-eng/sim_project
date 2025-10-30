from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')
    
    def get(self, request):
        logout(request)
        return redirect('login')
