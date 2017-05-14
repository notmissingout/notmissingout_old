from django.db import models
from django.core.files.storage import default_storage

ATTACHMENT_UPLOAD_TO = 'attachment'

class Attachment(models.Model):
    name = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="Defaults to filename, if left blank"
    )

    file = models.FileField(
        upload_to=ATTACHMENT_UPLOAD_TO,
        storage=default_storage
    )

    uploaded = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % (self.name)

    class Meta:
        abstract = True
