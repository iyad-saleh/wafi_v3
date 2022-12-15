from django.db import models
from django.conf import settings
from account.models  import Sub_account
from common.models import BaseModel, SoftDeleteModel


class Box(BaseModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    account = models.OneToOneField(Sub_account, on_delete=models.CASCADE )


    def __str__(self):
        return self.name