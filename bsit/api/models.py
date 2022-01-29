import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class paymentScheme(models.Model):
    pilotPayout = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    crewPayout = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    scoutPayout = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    securityPayout = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

class ore(models.Model):
    type = models.CharField(max_length=120)
    rawPrice = models.IntegerField()
    refinedPrice = models.IntegerField()
    refineTime = models.FloatField()
    refineCost = models.FloatField()
    refineYield = models.FloatField()

    def __str__(self):
        return self.type
    
class oreCollected(models.Model):
        ore = models.ManyToManyField(ore)
        amount = models.IntegerField(validators=[MinValueValidator(0)])

class refineryOreMod(models.Model):
    yieldMod = models.FloatField()
    timeMod = models.FloatField()
    costMod = models.FloatField()

class refinery(models.Model):
    name = models.CharField(max_length=120, null=False)
    agrMod = models.ManyToManyField(refineryOreMod)
    aluMod = models.ManyToManyField(refineryOreMod)
    berMod = models.ManyToManyField(refineryOreMod)
    bexMod = models.ManyToManyField(refineryOreMod)
    borMod = models.ManyToManyField(refineryOreMod)
    copMod = models.ManyToManyField(refineryOreMod)
    corMod = models.ManyToManyField(refineryOreMod)
    diaMod = models.ManyToManyField(refineryOreMod)
    golMod = models.ManyToManyField(refineryOreMod)
    hepMod = models.ManyToManyField(refineryOreMod)
    larMod = models.ManyToManyField(refineryOreMod)
    quanMod = models.ManyToManyField(refineryOreMod)
    quarMod = models.ManyToManyField(refineryOreMod)
    tarMod = models.ManyToManyField(refineryOreMod)
    titMod = models.ManyToManyField(refineryOreMod)
    tunMod = models.ManyToManyField(refineryOreMod)

    def __str__(self):
        return self.name
    

class refineryMethod(models.Model):
    name = models.CharField(max_length=120, null=False)
    yieldMod = models.FloatField()
    costMod = models.FloatField()
    timeMod = models.FloatField()

    def __str__(self):
        return self.name


class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    authorizedPilots = models.ManyToManyField(User)

class refineryJob(models.Model):

    class statusOpt(models.IntegerChoices):
        mining = 1, 'Mining'
        refining = 2, 'Refining'
        ready = 3, 'Ready'
        delivered = 4, 'Delivered'
        failed = 5, 'Failed'
    
    ores = models.ManyToManyField(oreCollected)
    method = models.ForeignKey(refineryMethod)
    refinery = models.ForeignKey(refinery)
    pilot = models.ForeignKey(User)
    crew = models.ManyToManyField(User, null=True)      # Find way to limit to only 3 members
    scouts = models.ManyToManyField(User, null=True)
    security = models.ManyToManyField(User, null=True)
    status = models.PositiveSmallIntegerField(choices=statusOpt.choices, default=statusOpt.mining)
    cscuYield = models.IntegerField(validators=[MinValueValidator(0)])
    time = models.IntegerField()
    cost = models.IntegerField()
    note = models.CharField(max_length=560, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.id
