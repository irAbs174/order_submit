from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from .models import (SnapShopOrders, DartilOrders)
from django.http import JsonResponse
from django.views.generic import CreateView
from django.db.models.functions import TruncDay, TruncMonth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from datetime import date
from django.utils.timezone import now
from django.db.models import Count

from .models import *

@csrf_exempt
def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

@csrf_exempt
def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

@csrf_exempt
def count_day_sall_snappshop(request):
    if request.method == "POST":
        # Get today's date
        today = date.today()

        # Query to count daily sales
        daily_sales = SnapShopOrders.objects.filter(
            product_created_at__date=today
        ).annotate(
            day=TruncDay('product_created_at')
        ).values('day').annotate(
            sales_count=Count('id')
        ).order_by('day')

        return JsonResponse({'status': [sale['sales_count'] for sale in daily_sales], 'success': True})

@csrf_exempt
def count_day_sall_dartil(request):
    if request.method == "POST":
        # Get today's date
        today = date.today()

        # Query to count daily sales
        daily_sales = DartilOrders.objects.filter(
            product_created_at__date=today
        ).annotate(
            day=TruncDay('product_created_at')
        ).values('day').annotate(
            sales_count=Count('id')
        ).order_by('day')

        return JsonResponse({'status': [sale['sales_count'] for sale in daily_sales], 'success': True})

@csrf_exempt
def count_monthly_sales_snappshop(request):
    if request.method == "POST":
        # Get the current month
        current_month = now().month

        # Query to count monthly sales
        monthly_sales = SnapShopOrders.objects.filter(
            product_created_at__month=current_month
        ).annotate(
            month=TruncMonth('product_created_at')
        ).values('month').annotate(
            sales_count=Count('id')
        ).order_by('month')

        return JsonResponse({'status': [sale['sales_count'] for sale in monthly_sales], 'success': True})

@csrf_exempt
def count_monthly_sales_dartil(request):
    if request.method == "POST":
        # Get the current month
        current_month = now().month

        # Query to count monthly sales
        monthly_sales = DartilOrders.objects.filter(
            product_created_at__month=current_month
        ).annotate(
            month=TruncMonth('product_created_at')
        ).values('month').annotate(
            sales_count=Count('id')
        ).order_by('month')

        return JsonResponse({'status': [sale['sales_count'] for sale in monthly_sales], 'success': True})