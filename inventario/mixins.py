from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy


class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now()
        context['title'] = 'Nuevo Producto'
        return context


class ValidatePermissionRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        permission_required = ''
        url_redirect = None

        def get_perms(self):
            if isinstance(self.permission_required, str):
                perms = (self.permission_required,)
            else:
                perms = self.permission_required
            return perms

        def get_url_redirect(self):
            if self.url_redirect is None:
                return reverse_lazy('index')
            return self.url_redirect

        def dispatch(self, request, *args, **kwargs):
            if request.user.has_perms(self.get_perms()):
                return super().dispatch(request, *args, **kwargs)
            messages.error(request, 'No tiene permiso para ingresar a este módulo')
            return HttpResponseRedirect(self.get_url_redirect())

