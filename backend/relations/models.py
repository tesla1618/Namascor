from django.db import models

class Relation(models.Model):
    description = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    invoice_address = models.TextField()  
    delivery_address = models.TextField()  
    visiting_address = models.TextField()  
    general_phone = models.CharField(max_length=20)  
    general_email = models.EmailField()
    headoffice = models.CharField(max_length=255, blank=True, null=True)
    our_reference = models.CharField(max_length=255)

    
    customer = models.BooleanField(default=False)
    customer_number = models.IntegerField(blank=True, null=True)
    supplier = models.BooleanField(default=False)
    supplier_number = models.IntegerField(blank=True, null=True)
    partner = models.BooleanField(default=False)
    private_contact = models.BooleanField(default=False)
    status_choices = [
        ('Lead', 'Lead'),
        ('Prospect', 'Prospect'),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    industry_choices = [
        
    ]
    industry = models.CharField(max_length=100, choices=industry_choices)
    category_choices = [
        
    ]
    category = models.CharField(max_length=100, choices=category_choices)
    group = models.CharField(max_length=255)  
    notes = models.TextField(blank=True)

class Contact(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='contacts')
    description = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    direct_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    language = models.CharField(max_length=50, blank=True)
    title_choices = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Ing', 'Ing'),
    ]
    title = models.CharField(max_length=10, choices=title_choices)
    job_function = models.CharField(max_length=255)
    key_contact_person = models.BooleanField(default=False)
    no_longer_works_here = models.BooleanField(default=False)
    do_not_send_mailings = models.BooleanField(default=False)
    note = models.TextField(blank=True)

class Activity(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='activities')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='activities')
    

class Document(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='documents')
    

class OrderInvoice(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='orders_invoices')
    

class Quotation(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='quotations')
    

class Product(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='products')
    

class Financial(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='financial_info')
    

class Freight(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='freight_info')
    

class General(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='general_info')
    non_active = models.BooleanField(default=False)
    www_address = models.URLField(blank=True)
    invoice_email = models.EmailField(blank=True)
    main_language = models.CharField(max_length=50, blank=True)
    date_of_first_order = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.non_active:
            self.relation.status = 'Inactive'
            self.relation.save()
        super().save(*args, **kwargs)
