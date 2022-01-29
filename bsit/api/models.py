from turtle import title
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
    type = models.CharField()
    rawPrice = models.IntegerField()
    refinedPrice = models.IntegerField()
    refineTime = models.FloatField()
    refineCost = models.FloatField()
    refineYield = models.FloatField()

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
    

class refineryMethod(models.Model):
    name = models.CharField(max_length=120, null=False)
    yieldMod = models.FloatField()
    costMod = models.FloatField()
    timeMod = models.FloatField()


class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #authorizedPilots = list of people

class refineryJob(models.Model):

    class statusOpt(models.IntegerChoices):
        mining = 1, 'Mining'
        refining = 2, 'Refining'
        ready = 3, 'Ready'
        delivered = 4, 'Delivered'
        failed = 5, 'Failed'

    #ore = orestuff
    #method = method stuff
    #refinery = refinery location
    #pilot = user
    #crew = 0-3 users
    #scouts = users
    #security = users
    #payout = something, not sure how to handel this yet
    status = models.PositiveSmallIntegerField(choices=statusOpt.choices, default=statusOpt.mining)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
