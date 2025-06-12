from django.db import models
from django.utils import timezone
from datetime import timedelta


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(blank=True,default=None)

    class Meta :
        abstract = True

    
    def is__deleted(self):

        self.is__deleted=True
        self.save()

    def soft_delete(self):
        self.is_deleted = True
        self.save(update_fields=['is_deleted', 'updated_at'])

    def restore(self):
        self.is__deleted=False
        self.save()
