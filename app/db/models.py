from datetime import date

from tortoise import fields, models


class Circuits(models.Model):
    circuitId = fields.IntField(pk=True)
    circuitRef = fields.CharField(max_length=255, default="")
    name = fields.CharField(max_length=255, default="")
    location = fields.CharField(max_length=255, null=True)
    country = fields.CharField(max_length=255, null=True)
    lat = fields.FloatField(null=True)
    lng = fields.FloatField(null=True)
    alt = fields.IntField(null=True)
    url = fields.CharField(max_length=255, default="")


class ConstructorResults(models.Model):
    constructorResultsId = fields.IntField(pk=True)
    raceId = fields.IntField(default=0)
    constructorId = fields.IntField(default=0)
    points = fields.FloatField(null=True)
    status = fields.CharField(max_length=255, null=True)


class ConstructorStandings(models.Model):
    constructorStandingsId = fields.IntField(pk=True)
    raceId = fields.IntField(default=0)
    constructorId = fields.IntField(default=0)
    points = fields.FloatField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(max_length=255, null=True)
    wins = fields.IntField(default=0)


class Constructors(models.Model):
    constructorId = fields.IntField(pk=True)
    constructorRef = fields.CharField(max_length=255, default="")
    name = fields.CharField(max_length=255, default="")
    nationality = fields.CharField(max_length=255, null=True)
    url = fields.CharField(max_length=255, default="")


class DriverStandings(models.Model):
    driverStandingsId = fields.IntField(pk=True)
    raceId = fields.IntField(default=0)
    driverId = fields.IntField(default=0)
    points = fields.FloatField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(max_length=255, null=True)
    wins = fields.IntField(default=0)


class Drivers(models.Model):
    driverId = fields.IntField(pk=True, source_field="driverId")
    driverRef = fields.CharField(max_length=255, default="", source_field="driverRef")
    number = fields.IntField(null=True)
    code = fields.CharField(max_length=3, null=True)
    forename = fields.CharField(max_length=255, default="")
    surname = fields.CharField(max_length=255, default="")
    dob = fields.DateField(null=True)
    nationality = fields.CharField(max_length=255, null=True)
    url = fields.CharField(max_length=255, default="")

    class Meta:
        table = "drivers"

    def __str__(self) -> str:
        return f'<Driver: "{self.forename} {self.surname}">'


class LapTimes(models.Model):
    raceId = fields.IntField()
    driverId = fields.IntField()
    lap = fields.IntField()
    position = fields.IntField(null=True)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)


#   PRIMARY KEY (raceId,driverId,lap),


class PitStops(models.Model):
    raceId = fields.IntField()
    driverId = fields.IntField()
    stop = fields.IntField()
    lap = fields.IntField()
    time = fields.DateField()
    duration = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)


#   PRIMARY KEY (raceId,driverId,stop),


class Qualifying(models.Model):
    qualifyId = fields.IntField(pk=True)
    raceId = fields.IntField(default=0)
    driverId = fields.IntField(default=0)
    constructorId = fields.IntField(default=0)
    number = fields.IntField(default=0)
    position = fields.IntField(null=True)
    q1 = fields.CharField(max_length=255, null=True)
    q2 = fields.CharField(max_length=255, null=True)
    q3 = fields.CharField(max_length=255, null=True)


class Races(models.Model):
    raceId = fields.IntField(pk=True)
    year = fields.IntField(default=0)
    round = fields.IntField(default=0)
    circuitId = fields.IntField(default=0)
    name = fields.CharField(max_length=255, default="")
    date = fields.DateField(default=date.today())
    time = fields.TimeField(null=True)
    url = fields.CharField(max_length=255, null=True)
    fp1_date = fields.DateField(null=True)
    fp1_time = fields.TimeField(null=True)
    fp2_date = fields.DateField(null=True)
    fp2_time = fields.TimeField(null=True)
    fp3_date = fields.DateField(null=True)
    fp3_time = fields.TimeField(null=True)
    quali_date = fields.DateField(null=True)
    quali_time = fields.TimeField(null=True)
    sprint_date = fields.DateField(null=True)
    sprint_time = fields.TimeField(null=True)


class Results(models.Model):
    resultId = fields.IntField(pk=True)
    raceId = fields.IntField(default=0)
    driverId = fields.IntField(default=0)
    constructorId = fields.IntField(default=0)
    number = fields.IntField(null=True)
    grid = fields.IntField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(max_length=255, default="")
    positionOrder = fields.IntField(default=0)
    points = fields.FloatField(default=0)
    laps = fields.IntField(default=0)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)
    fastestLap = fields.IntField(null=True)
    rank = fields.IntField(default=0)
    fastestLapTime = fields.CharField(max_length=255, null=True)
    fastestLapSpeed = fields.CharField(max_length=255, null=True)
    statusId = fields.IntField(default=0)


class Seasons(models.Model):
    year = fields.IntField(default=0)
    url = fields.CharField(max_length=255, default="")


class SprintResults(models.Model):
    sprintResultId = fields.IntField(pk=True)
    raceId = fields.IntField(default=0)
    driverId = fields.IntField(default=0)
    constructorId = fields.IntField(default=0)
    number = fields.IntField(default=0)
    grid = fields.IntField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(max_length=255, default="")
    positionOrder = fields.IntField(default=0)
    points = fields.FloatField(default=0)
    laps = fields.IntField(default=0)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)
    fastestLap = fields.IntField(null=True)
    fastestLapTime = fields.CharField(max_length=255, null=True)
    statusId = fields.IntField(default=0)


class Status(models.Model):
    statusId = fields.IntField(pk=True)
    status = fields.CharField(max_length=255, default="")
