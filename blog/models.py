from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

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
