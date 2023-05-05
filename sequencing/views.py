from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import analyze_files_task
from .models import Sequence, Reference, AnalysisStatus
from .serializers import SequenceSerializer, ReferenceSerializer, AnalysisStatusSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
# Create your views here.

def load_reference_sequence(request):
    analyze_files_task.delay('Hello')

    return render(request,'home.html',{'name':'Vaibhao'})

class SequenceViewSet(ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        if instance.analysisstatus_set.count() > 0:
            return Response({'error':'Cannot delete sequence with analysis status'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReferenceViewSet(ReadOnlyModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    
class AnalysisStatusViewSet(ModelViewSet):
    queryset = AnalysisStatus.objects.all()
    serializer_class = AnalysisStatusSerializer


class AnalyzeFilesView(APIView):
    def post(self,request):
        sequence_id = request.data['sequence_id']
        reference_id = request.data['reference_id']
        sequence = get_object_or_404(Sequence,pk=sequence_id)
        reference = get_object_or_404(Reference,pk=reference_id)
        # if sequence.analysisstatus_set.count() > 0:
        #     return Response({'error':'Sequence already analyzed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        analyze_files_task.delay(sequence_id,reference_id)
        return Response(status=status.HTTP_202_ACCEPTED)


    

