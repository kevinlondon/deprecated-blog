from django.db import models
from django.template.defaultfilters import slugify
from django import forms

from tinymce.widgets import TinyMCE
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    slug = models.SlugField(max_length=40, editable=False)
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        url_name = "blog_post_detail"
        self.save()
        kwargs = {"slug": self.slug,
                  "year": self.created.year,
                  "month": str(self.created.month),
                  "day": str(self.created.day),}
        return (url_name, (), kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows':30})
        }
