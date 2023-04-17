from rest_framework.serializers import ModelSerializer

from .models import Contacts


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contacts
        fields = ['id','countery_code','phone_number','first_name','last_name','contact_img','is_favorite']