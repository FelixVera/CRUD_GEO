from django.db import models



class client(models.Model):
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('B', 'Blocked'),
        ('S', 'Special'),
        ('R', 'Blocked by Resignation'),
    ]
    SEX_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    
    CLIENT_NUMBER   = models.IntegerField(primary_key=True, verbose_name="Client Number", db_column="CLIENT_NUMBER")
    CLIENT_LNAME    = models.CharField(max_length=40,verbose_name="Last Name", db_column="CLIENT_LNAME", blank=True, null=True)
    CLIENT_FNAME    = models.CharField(max_length=20,verbose_name="First Name", db_column="CLIENT_FNAME", blank=True, null=True)
    CLIENT_STATUS   = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="Client Status", db_column="CLIENT_STATUS", blank=True, null=True)
    CLIENT_DMYADM   = models.DateField(verbose_name="Date of Admission", db_column="CLIENT_DMYADM", blank=True, null=True)
    CLIENT_ID       = models.CharField(max_length=15, verbose_name="Client ID", db_column="CLIENT_ID", blank=False)
    CLIENT_DMYBIR   = models.DateField(verbose_name="Date of Birth", db_column="CLIENT_DMYBIR", blank=True, null=True)
    CLIENT_SEX      = models.CharField(max_length=1,choices=SEX_CHOICES, verbose_name= "Client Sex", db_column="CLIENT_SEX", blank=True, null=True)
    CLIENT_ADDRESS  = models.CharField(max_length=120, verbose_name="Client Address", db_column="CLIENT_ADDRESS", blank=True, null=True)
    CLIENT_PHONE    = models.CharField(max_length=15, verbose_name="Client Phone", db_column="CLIENT_PHONE", blank=True, null=True)
    CLIENT_CITY     = models.CharField(max_length=30, verbose_name="Client City", db_column="CLIENT_CITY", blank=True, null=True)
    CLIENT_IDORIGIN = models.CharField(max_length=30, verbose_name="ID Client Origin", db_column="CLIENT_IDORIGIN", blank=True, null=True)
    
    class Meta:
        db_table = 'client'
        verbose_name = 'client'
        ordering = ['CLIENT_NUMBER']
        
        
        
        
class cligeopos(models.Model):
    TIPOS_CLIGEO_CHOICES = (
        ('D','home/dwelling'),
        ('J','Job/ bussiness'),
    )
    CLIGEO_NUMBER   = models.ForeignKey(client, to_field="CLIENT_NUMBER" , related_name='CLIGEO_NUMBER', verbose_name='Client Number', db_column='CLIGEO_NUMBER', blank=True, null=True, on_delete=models.SET_NULL )
    CLIGEO_TYPPOS   = models.CharField(max_length=50, choices=TIPOS_CLIGEO_CHOICES, verbose_name='Position Type', db_column='CLIGEO_TYPPOS', blank=True, null=True)
    CLIGEO_LATITUDE = models.CharField(max_length=150, verbose_name='Latitude', db_column='CLIGEO_LATITUDE', blank=True, null=True)
    CLIGEO_LENGHT   = models.CharField(max_length=120, verbose_name='Length', db_column='CLIGEO_LENGHT', blank=True, null=True)
    CLIGEO_OBSER    = models.TextField( verbose_name='Observation', db_column='CLIGEO_OBSER', blank=True, null=True)

    