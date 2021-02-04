from django.db import models
# Create your models here.
class Upload(models.Model):
    upload_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add =True)

    def filename(self):
        return os.path.basename(self.file.name)


