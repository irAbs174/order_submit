from django.db import models 

class SnapShopOrders(models.Model):
    order_code = models.CharField(max_length=50, verbose_name='شماره سفارش',null=True, blank=True, unique=True)
    corp_order_code = models.CharField(max_length=50, verbose_name='شماره فاکتور شرکت',null=True, blank=True, unique=True)
    full_name = models.CharField(max_length=50, verbose_name='نام کامل',null=True, blank=True )
    pdf_file = models.FileField(upload_to='snappshop_pdfs', verbose_name='فاکتور', blank=True, null=True)
    no_pack = 'بسته بندی نشده'
    pack = 'بسته بندی شده'
    sended = 'ارسال شده'
    cancel = 'لغو شده'

    STATUS_CHOICES = [
        (no_pack, 'بسته بندی نشده'),
        (pack, 'بسته بندی شده'),
        (sended, 'ارسال شده'),
        ( cancel, 'لغو شده'),
    ]
    order_status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='وضعیت سفارش')
    normal = 'عادی'
    express = 'اکسپرس'
    SEND_STATUS_CHOICES = [
        (normal, 'عادی'),
        (express, 'اکسپرس'),
    ]
    send_status = models.CharField(max_length=50, choices=SEND_STATUS_CHOICES, verbose_name='نوع ارسال')
    price = models.CharField(max_length=300, verbose_name='ارزش سفارش',null=True, blank=True )
    product_created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', blank=True, null=True)
    product_updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی', blank=True, null=True)

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'سفارش اسنپ شاپ'
        verbose_name_plural = 'سفارشات اسنپ شاپ'

    def __str__(self):
        return self.order_code


class DartilOrders(models.Model):
    corp_order_code = models.CharField(max_length=50, verbose_name='شماره فاکتور شرکت',null=True, blank=True, unique=True)
    full_name = models.CharField(max_length=50, verbose_name='نام کامل',null=True, blank=True )
    no_pack = 'بسته بندی نشده'
    pack = 'بسته بندی شده'
    sended = 'ارسال شده'
    cancel = 'لغو شده'

    STATUS_CHOICES = [
        (no_pack, 'بسته بندی نشده'),
        (pack, 'بسته بندی شده'),
        (sended, 'ارسال شده'),
        ( cancel, 'لغو شده'),
    ]
    order_status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='وضعیت سفارش')
    price = models.CharField(max_length=300, verbose_name='ارزش سفارش',null=True, blank=True )
    pdf_file = models.FileField(upload_to='dartil_pdfs', verbose_name='فاکتور', blank=True, null=True)
    product_created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', blank=True, null=True)
    product_updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی', blank=True, null=True)

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'سفارش دارتیل '
        verbose_name_plural = 'سفارشات دارتیل'

    def __str__(self):
        return self.full_name