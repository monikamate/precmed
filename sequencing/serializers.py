from rest_framework import serializers
from .models import Sequence, Reference, AnalysisStatus

class SequenceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Sequence.objects.create(**validated_data)
    
    class Meta:
        model = Sequence
        fields = ['id','sample_id' ,'sequence_data_file','quality_scores']

class ReferenceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Reference.objects.create(**validated_data)
    
    class Meta:
        model = Reference
        fields = ['id','reference_id','reference_file']

class AnalysisStatusSerializer(serializers.ModelSerializer):
   
    def create(self, validated_data):
        return AnalysisStatus.objects.create(**validated_data)
    
    class Meta:
        model = AnalysisStatus
        fields = ['id','sequence','reference','status','result_file','created_at','updated_at']

class AnalyzeFilesSerializer(serializers.Serializer):
    sequence_id = serializers.IntegerField()
    reference_id = serializers.IntegerField()