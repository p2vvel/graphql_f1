from tortoise import models, fields


class Drivers(models.Model):
    driver_id = fields.IntField(pk=True, source_field="driverId")
    driver_ref = fields.CharField(max_length=255, source_field="driverRef")
    number = fields.IntField(null=True)
    code = fields.CharField(max_length=3, null=True)
    forename = fields.CharField(max_length=255)
    surname = fields.CharField(max_length=255)
    dob = fields.DateField(null=True)
    nationality = fields.CharField(max_length=255, null=True)
    url = fields.CharField(max_length=255)

    class Meta:
        table = "drivers"
