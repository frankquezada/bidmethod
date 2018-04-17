from django.db import models


class Bid(models.Model):
    bid_entity = models.CharField(max_length=50)
    bid_number = models.CharField(max_length=50)
    bid_title = models.CharField(max_length=50)
    bid_due = models.DateField(auto_now=False, auto_now_add=False)
    bid_time = models.TimeField(auto_now=False, auto_now_add=False)
    bid_question = models.DateField(auto_now=False, auto_now_add=False)
    bid_issue = models.DateField(auto_now=False, auto_now_add=False)
    bid_contact_name = models.CharField(max_length=50)
    bid_contact_email = models.EmailField(max_length=254)
    branch = models.CharField(max_length=50)
    branch_region = models.CharField(max_length=50)
    branch_contact = models.CharField(max_length=50)

    def __str__(self):
        return str(self.bid_entity)