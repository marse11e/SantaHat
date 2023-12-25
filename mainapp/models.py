from django.db import models

class PhotoEdit(models.Model):
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Изображение объявления",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    
    # def save(self, *args, **kwargs):
    #     self.image.name = f"photo_{self.id}.jpg"
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.created_at}"
    
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"