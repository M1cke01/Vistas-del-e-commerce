from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Venta

class SalesView(LoginRequiredMixin, TemplateView):
    template_name = "analytics/sales.html"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No tienes acceso", status=401)
        return super(SalesView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ventas'] = Venta.objects.select_related('producto').all()
        return context