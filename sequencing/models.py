from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Sequence (models.Model):
    sample_id = models.CharField(max_length=255)
    sequence_data_file = models.FileField(upload_to='sequencing/files',blank=True,validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    quality_scores = models.DecimalField(max_digits=6,decimal_places=2,blank=True)

    def __str__(self) -> str:
        return self.sample_id
    
class Reference (models.Model):
    reference_id = models.CharField(max_length=255)
    reference_file = models.FileField(upload_to='references/files', validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    

    def __str__(self) -> str:
        return self.reference_id

class AnalysisStatus(models.Model):
    sequence = models.ForeignKey(Sequence,on_delete=models.CASCADE)
    reference = models.ForeignKey(Reference,on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    result_file = models.FileField(upload_to='sequencing/results',blank=True,validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.status