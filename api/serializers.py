from rest_framework import serializers


try:

    from home.models import (SnapShopOrders, DartilOrders)

except:
    pass 

class SnapShopOrdersSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = SnapShopOrders
        except:
            pass    
        fields = '__all__'


class DartilOrdersSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = DartilOrders
        except:
            pass    
        fields = '__all__'

