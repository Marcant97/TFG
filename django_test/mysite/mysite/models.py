from django.db import models

class TuModelo(models.Model):
    # Define los campos necesarios para tu modelo
    opcion1 = models.BooleanField(default=False)
    opcion2 = models.BooleanField(default=False)
    opcion3 = models.BooleanField(default=False)

    def __str__(self):
        return f"TuModelo #{self.pk}"
