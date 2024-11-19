class Book(models.Model):
    title = models.CharField(max_length = 40)
    author = models.CharField(max_length = 40)
