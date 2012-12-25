from django.db import models,IntegrityError,transaction
from django.template.defaultfilters import slugify

class TestSet(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    test_date = models.DateTimeField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(TestSet, self).save(*args, **kwargs)


class Scenario(models.Model):	
    test_case = models.CharField(max_length=255)
    purpose	= models.TextField()
    pre_requisite = models.TextField(null=True,blank=True)	
    test_data = models.TextField(null=True,blank=True)
    test_step= models.TextField()
    expected_result = models.TextField()
    actual_result = models.TextField(null=True,blank=True)
    test_date = models.DateTimeField(null=True,blank=True)
    tester_accepted = models.BooleanField()	
    note = models.TextField(null=True,blank=True)
    case_order = models.PositiveIntegerField(null=True,blank=True)
    
    def __unicode__(self):
        return self.test_case
    
    def test_case_id(self):
        return "case-%s" % self.case_order.__str__().zfill(3)
    
    def save(self, *args, **kwargs):
        try:
            super(Scenario, self).save(*args, **kwargs)
        except IntegrityError:
            transaction.rollback()
            case_order = Scenario.objects.filter(case_order__gte=self.case_order)
            for i in case_order.order_by("-case_order"):
                i.case_order=i.case_order+1
                super(Scenario, i).save(*args, **kwargs)
            super(Scenario, self).save(*args, **kwargs)

    class Meta: 
        ordering = ['case_order']

        