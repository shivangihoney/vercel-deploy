from rest_framework import serializers
from .models import company

class companyserialzer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = [ 'id', 'com_name', 'email_id']