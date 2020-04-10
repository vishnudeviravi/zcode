from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    hashtags1 = models.TextField(blank = True)
    hashtags2 = models.TextField(blank = True)
    hashtags3 = models.TextField(blank = True)
    hashtags4 = models.TextField(blank = True)
    hashtags5 = models.TextField(blank = True)
    caption = models.TextField()
    icon = models.ImageField(upload_to='icons/')
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.TextField()
    image = models.ImageField(upload_to='image/', blank = True, null=True )
    code = models.FileField(upload_to='documents/')
    upvote = models.IntegerField(default=1)


    def __str__(self):
        return self.product_name

    def date(self):
        return self.pub_date.strftime('%b %e %Y')

    def hash1(self):
        k = "#"+self.hashtags1
        if k != "#":
            return k
    def hash2(self):
        k = "#" + self.hashtags2
        if k != "#":
            return k
    def hash3(self):
        k = "#" + self.hashtags3
        if k != "#":
            return k
    def hash4(self):
        k = "#" + self.hashtags4
        if k != "#":
            return k
    def hash5(self):
        k = "#" + self.hashtags5
        if k != "#":
            return k

    class Meta:
        ordering = ['-pub_date']




