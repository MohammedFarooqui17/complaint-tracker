from rest_framework import serializers

class ComplaintSerializer(serializers.Serializer):
    department = serializers.CharField(max_length=100)
    complaint_type = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=1000)
