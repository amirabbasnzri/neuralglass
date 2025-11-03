from django.db import models


# messages:
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

# -----------------------------------------------------------------------------------------------------------------
    
# contact:   
class SocialLink(models.Model):
    orders = [
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'forth')
    ]
    
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=False)
    icon = models.ImageField(upload_to='media/social_links_img', blank=False, null=False)
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
   
# -----------------------------------------------------------------------------------------------------------------
 
    
# sections:
class Section(models.Model):
    orders = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
    ]
    section_name = models.CharField(max_length=60, unique=True)
    order = models.PositiveSmallIntegerField(choices=orders)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f'{self.order} - {self.section_name}'
    
class Section2(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, editable=False, default=2)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    emoji = models.CharField(max_length=2)
    image = models.ImageField(upload_to='media/quantum_capabilities_img')
    
    class Meta:
        verbose_name = 'Section2'
        verbose_name_plural = 'Section2'
    
    def __str__(self):
        return f'{self.title} - {self.emoji}'    
 
class Section3(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, editable=False, default=3)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=80)
    emoji = models.CharField(max_length=2)
    
    class Meta:
        verbose_name = 'Section3'
        verbose_name_plural = 'Section3'
    
    def __str__(self):
        return f'{self.title} - {self.emoji}'
   
class Section4(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, editable=False, default=4)
    year = models.CharField(max_length=4)
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Section4'
        verbose_name_plural = 'Section4'
        ordering = ['year']
        
    def __str__(self):
        return f'{self.year} - {self.title}'
    
# ----------------------------------------------------------------------------------------------------------------
 
# footer: 
class FooterInfo(models.Model):
    year = models.CharField(max_length=4, default="2025")
    company_name = models.CharField(max_length=100)
    rights_text = models.CharField(max_length=200)
    design_by = models.CharField(max_length=100)
    designer_url = models.URLField()
    enhanced_by = models.CharField(max_length=100)
    framework = models.CharField(
        max_length=100,
        default="Django-Framework"
    )
    framework_url = models.URLField(default='https://www.djangoproject.com')
    
    def get_default_github():
        return SocialLink.objects.filter(name__iexact='GitHub').first()
    
    github_url = models.ForeignKey(SocialLink, on_delete=models.SET_NULL, null=True, blank=True, default=get_default_github)
    
    class Meta:
        verbose_name = 'FooterInfo'
        verbose_name_plural = 'FooterInfo'
    
    def __str__(self):
        return f"Footer ({self.year})"
    
# ---------------------------------------------------------------------------------------------------------------