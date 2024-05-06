from datetime import date

from tortoise import fields, models


class Circuits(models.Model):
    circuitId = fields.IntField(pk=True, source_field="circuitId")
    circuitRef = fields.CharField(max_length=255, default="", source_field="circuitRef")
    name = fields.CharField(max_length=255, default="")
    location = fields.CharField(max_length=255, null=True)
    country = fields.CharField(max_length=255, null=True)
    lat = fields.FloatField(null=True)
    lng = fields.FloatField(null=True)
    alt = fields.IntField(null=True)
    url = fields.CharField(max_length=255, default="")

    class Meta:
        table = "circuits"

    def __str__(self) -> str:
        return f'<Circuit: "{self.name}">'


class ConstructorResults(models.Model):
    constructorResultsId = fields.IntField(pk=True, source_field="constructorResultsId")
    raceId = fields.IntField(default=0, source_field="raceId")
    constructorId = fields.IntField(default=0, source_field="constructorId")
    points = fields.FloatField(null=True)
    status = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "constructorResults"


class ConstructorStandings(models.Model):
    constructorStandingsId = fields.IntField(
        pk=True, source_field="constructorStandingsId"
    )
    raceId = fields.IntField(default=0, source_field="raceId")
    constructorId = fields.IntField(default=0, source_field="constructorId")
    points = fields.FloatField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(
        max_length=255, null=True, source_field="positionText"
    )
    wins = fields.IntField(default=0)

    class Meta:
        table = "constructorStandings"


class Constructors(models.Model):
    constructorId = fields.IntField(pk=True, source_field="constructorId")
    constructorRef = fields.CharField(
        max_length=255, default="", source_field="constructorRef"
    )
    name = fields.CharField(max_length=255, default="")
    nationality = fields.CharField(max_length=255, null=True)
    url = fields.CharField(max_length=255, default="")

    class Meta:
        table = "constructors"

    def __str__(self) -> str:
        return f'<Constructor: "{self.name}">'


class DriverStandings(models.Model):
    driverStandingsId = fields.IntField(pk=True, source_field="driverStandingsId")
    raceId = fields.IntField(default=0, source_field="raceId")
    driverId = fields.IntField(default=0, source_field="driverId")
    points = fields.FloatField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(
        max_length=255, null=True, source_field="positionText"
    )
    wins = fields.IntField(default=0)

    class Meta:
        table = "driverStandings"


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
    raceId = fields.IntField(source_field="raceId")
    driverId = fields.IntField(source_field="driverId")
    lap = fields.IntField()
    position = fields.IntField(null=True)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)

    class Meta:
        table = "lapTimes"


#   PRIMARY KEY (raceId,driverId,lap),


class PitStops(models.Model):
    raceId = fields.IntField(source_field="raceId")
    driverId = fields.IntField(source_field="driverId")
    stop = fields.IntField()
    lap = fields.IntField()
    time = fields.DateField()
    duration = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)

    class Meta:
        table = "pitStops"


#   PRIMARY KEY (raceId,driverId,stop),


class Qualifying(models.Model):
    qualifyId = fields.IntField(pk=True, source_field="qualifyId")
    raceId = fields.IntField(default=0, source_field="raceId")
    driverId = fields.IntField(default=0, source_field="driverId")
    constructorId = fields.IntField(default=0, source_field="constructorId")
    number = fields.IntField(default=0)
    position = fields.IntField(null=True)
    q1 = fields.CharField(max_length=255, null=True)
    q2 = fields.CharField(max_length=255, null=True)
    q3 = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "qualifying"


class Races(models.Model):
    raceId = fields.IntField(pk=True, source_field="raceId")
    year = fields.IntField(default=0)
    round = fields.IntField(default=0)
    circuitId = fields.IntField(default=0, source_field="circuitId")
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

    class Meta:
        table = "races"

    def __str__(self) -> str:
        return f'<Race: "{self.name} - {self.year}">'


class Results(models.Model):
    resultId = fields.IntField(pk=True, source_field="resultId")
    raceId = fields.IntField(default=0, source_field="raceId")
    driverId = fields.IntField(default=0, source_field="driverId")
    constructorId = fields.IntField(default=0, source_field="constructorId")
    number = fields.IntField(null=True)
    grid = fields.IntField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(
        max_length=255, default="", source_field="positionText"
    )
    positionOrder = fields.IntField(default=0, source_field="positionOrder")
    points = fields.FloatField(default=0)
    laps = fields.IntField(default=0)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)
    fastestLap = fields.IntField(null=True, source_field="fastestLap")
    rank = fields.IntField(default=0)
    fastestLapTime = fields.CharField(
        max_length=255, null=True, source_field="fastestLapTime"
    )
    fastestLapSpeed = fields.CharField(
        max_length=255, null=True, source_field="fastestLapSpeed"
    )
    statusId = fields.IntField(default=0, source_field="statusId")

    class Meta:
        table = "results"


class Seasons(models.Model):
    year = fields.IntField(default=0)
    url = fields.CharField(max_length=255, default="")

    class Meta:
        table = "seasons"

    def __str__(self) -> str:
        return f'<Season: "{self.year}">'


class SprintResults(models.Model):
    sprintResultId = fields.IntField(pk=True, source_field="sprintResultId")
    raceId = fields.IntField(default=0, source_field="raceId")
    driverId = fields.IntField(default=0, source_field="driverId")
    constructorId = fields.IntField(default=0, source_field="constructorId")
    number = fields.IntField(default=0)
    grid = fields.IntField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(
        max_length=255, default="", source_field="positionText"
    )
    positionOrder = fields.IntField(default=0, source_field="positionOrder")
    points = fields.FloatField(default=0)
    laps = fields.IntField(default=0)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)
    fastestLap = fields.IntField(null=True, source_field="fastestLap")
    fastestLapTime = fields.CharField(
        max_length=255, null=True, source_field="fastestLapTime"
    )
    statusId = fields.IntField(default=0, source_field="statusId")

    class Meta:
        table = "sprintResults"


class Status(models.Model):
    statusId = fields.IntField(pk=True, source_field="statusId")
    status = fields.CharField(max_length=255, default="")

    class Meta:
        table = "status"

    def __str__(self) -> str:
        return f'<Status: "{self.status}">'
