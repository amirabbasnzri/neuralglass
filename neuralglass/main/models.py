from django.db import models

class MessageModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return f'{self.name} - {self.subject}'
    
    
class SocialLink(models.Model):
    orders = [
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'forth')
    ]
    
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=False)
    icon = models.ImageField(upload_to='media/social_links', blank=False, null=False)
    order = models.PositiveSmallIntegerField(choices=orders)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.url or not self.icon:
            self.is_active = False

        if self.pk:
            old_order = SocialLink.objects.get(pk=self.pk).order
            if old_order != self.order:
                if self.order < old_order:
                    SocialLink.objects.filter(order__gte=self.order, order__lt=old_order).update(order=models.F('order') + 1)
                else:
                    SocialLink.objects.filter(order__gt=old_order, order__lte=self.order).update(order=models.F('order') - 1)
        else:
            last = SocialLink.objects.aggregate(max_order=models.Max('order'))['max_order'] or 0
            self.order = last + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class ContactText(models.Model):
    subtitle = models.CharField(max_length=150)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    
    class Meta:
        verbose_name = 'ContactText'
    
    def __str__(self):
        return self.subtitle[:70]