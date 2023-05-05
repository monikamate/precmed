from time import sleep
from celery import shared_task
from .models import AnalysisStatus, Sequence, Reference
import os
from django.conf import settings
from precmed.querymatching import findQueryMatches

@shared_task
def analyze_files_task(sequence_id,reference_id):
    # initiate analysis status
    analysisStatus = AnalysisStatus()
    analysisStatus.sequence_id = sequence_id
    analysisStatus.reference_id = reference_id
    analysisStatus.status = "In progress"
    analysisStatus.result_file = ""
    analysisStatus.save()

    # create file path
    filePath = os.path.join(settings.MEDIA_ROOT,"sequencing","results","result_"+str(sequence_id)+"_"+str(reference_id)+".txt")

    # simulate analysis

    try:

        sequenceFileData = Sequence.objects.get(id=sequence_id).sequence_data_file.read().decode("utf-8")
        referenceFileData = Reference.objects.get(id=reference_id).reference_file.read().decode("utf-8")
        #perform analysis
        matches = findQueryMatches(str(sequenceFileData),str(referenceFileData))

        fileOutput = ""

        if len(matches) == 0:
            fileOutput = "No matches found"
        else:
            fileOutput = f'Found {len(matches)} matches at positions: {matches}'

        # create new text file and insert data
        result_file = open(filePath,"w")
        result_file.write(fileOutput+"\n")
        result_file.close()

        # update analysis status
        analysisStatus.result_file = filePath
        analysisStatus.status = "Completed"
        print("Task completed")
        analysisStatus.save()
    except Exception as e:
        print(e)
        # create error file
        result_file = open(filePath,"w")
        result_file.write("Error: "+str(e)+"\n")
        result_file.close()

        # update analysis status
        analysisStatus.result_file = filePath
        analysisStatus.status = "Failed"
        analysisStatus.save()
    
    return sequence_id,reference_id
    