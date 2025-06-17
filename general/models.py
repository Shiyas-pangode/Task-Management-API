from django.db import models
from django.utils import timezone
from datetime import timedelta


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    is_deleted = models.BooleanField(blank=True,default=None)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True

    
    def is_deleted(self):

        self.is__deleted=True
        self.save()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'updated_at'])

    def restore(self):
        self.is__deleted=False
        self.deleted_at=None
        self.save(update_fields=['is_deleted', 'deleted_at'])
