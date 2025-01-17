from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


# Create your views here.


class LoginFormView(LoginView):
    template_name = 'login/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('inventario')
        return super().dispatch(request, *args, **kwargs )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context