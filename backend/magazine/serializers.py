from .models import Magazine
from rest_framework import serializers

class MagazineSerializer(serializers.ModelSerializer):
    cover_image_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Magazine
        fields = ['id', 'title', 'date', 'cover_image_url', 'pdf_url']

    def get_cover_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url)
        return None

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        if request and obj.pdf_file:
            return request.build_absolute_uri(obj.pdf_file.url)
        return None
