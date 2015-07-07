from django.db import models

# Create your models here.

class Language:
    ENGLISH = 'en'
    CHINESE = 'zh'
    
    # TRANSMISSION: Automatic,MANUAL,other
    LANGUAGES = (
        (ENGLISH, 'English'),
        (CHINESE, 'Chinese'),
    )
    
    

class Page(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
class PageTranslation(models.Model):
    LANGUAGE_CHOICE = Language.LANGUAGES
    
    title = models.CharField(max_length=150, db_index=True)
    language = models.CharField(max_length=2,
                                      choices=LANGUAGE_CHOICE,
                                      default=Language.ENGLISH)
    page = models.ForeignKey('Page')
    
    def __unicode__(self):
        return self.title