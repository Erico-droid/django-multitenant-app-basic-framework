import uuid
import os
from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    # REQUIRED_FIELDS = ('tenant_name', 'paid_until', 'schema_name', 'on_trial', 'domain_url')
    tenant_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    schema_name = models.CharField(max_length = 100, unique = True, blank = False, null = False)
    domain_url = models.CharField(max_length = 100, unique = True, blank = False, null = False)
    # tenant_uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
