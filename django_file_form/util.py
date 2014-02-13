from django.db import models


class ModelManager(models.Manager):
    def try_get(self, **kwargs):
        qs = self.get_query_set().filter(**kwargs)
        if qs.exists():
            return qs.get()
        else:
            return None
