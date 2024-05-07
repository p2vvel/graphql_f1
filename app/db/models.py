from datetime import date

from tortoise import fields, models


class Circuits(models.Model):
    id = fields.IntField(pk=True, source_field="circuitId")
    ref = fields.CharField(max_length=255, default="", source_field="circuitRef")
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

    def __repr__(self) -> str:
        return str(self)


class ConstructorResults(models.Model):
    id = fields.IntField(pk=True, source_field="constructorResultsId")
    race_id = fields.IntField(default=0, source_field="raceId")
    constructor_id = fields.IntField(default=0, source_field="constructorId")
    points = fields.FloatField(null=True)
    status = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "constructorResults"


class ConstructorStandings(models.Model):
    id = fields.IntField(pk=True, source_field="constructorStandingsId")
    race_id = fields.IntField(default=0, source_field="raceId")
    constructor_id = fields.IntField(default=0, source_field="constructorId")
    points = fields.FloatField(default=0)
    position = fields.IntField(null=True)
    positionText = fields.CharField(
        max_length=255, null=True, source_field="positionText"
    )
    wins = fields.IntField(default=0)

    class Meta:
        table = "constructorStandings"


class Constructors(models.Model):
    id = fields.IntField(pk=True, source_field="constructorId")
    ref = fields.CharField(max_length=255, default="", source_field="constructorRef")
    name = fields.CharField(max_length=255, default="")
    nationality = fields.CharField(max_length=255, null=True)
    url = fields.CharField(max_length=255, default="")

    class Meta:
        table = "constructors"

    def __str__(self) -> str:
        return f'<Constructor: "{self.name}">'

    def __repr__(self) -> str:
        return str(self)


class DriverStandings(models.Model):
    id = fields.IntField(pk=True, source_field="driverStandingsId")
    race_id = fields.IntField(default=0, source_field="raceId")
    driver_id = fields.IntField(default=0, source_field="driverId")
    points = fields.FloatField(default=0)
    position = fields.IntField(null=True)
    position_text = fields.CharField(
        max_length=255, null=True, source_field="positionText"
    )
    wins = fields.IntField(default=0)

    class Meta:
        table = "driverStandings"


class Drivers(models.Model):
    id = fields.IntField(pk=True, source_field="driverId")
    ref = fields.CharField(max_length=255, default="", source_field="driverRef")
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

    def __repr__(self) -> str:
        return str(self)


class LapTimes(models.Model):
    race_id = fields.IntField(source_field="raceId")
    driver_id = fields.IntField(source_field="driverId")
    lap = fields.IntField()
    position = fields.IntField(null=True)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)

    class Meta:
        table = "lapTimes"


#   PRIMARY KEY (raceId,driverId,lap),


class PitStops(models.Model):
    race_id = fields.IntField(source_field="raceId")
    driver_id = fields.IntField(source_field="driverId")
    stop = fields.IntField()
    lap = fields.IntField()
    time = fields.DateField()
    duration = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)

    class Meta:
        table = "pitStops"


#   PRIMARY KEY (raceId,driverId,stop),


class Qualifying(models.Model):
    id = fields.IntField(pk=True, source_field="qualifyId")
    race_id = fields.IntField(default=0, source_field="raceId")
    driver_id = fields.IntField(default=0, source_field="driverId")
    constructor_id = fields.IntField(default=0, source_field="constructorId")
    number = fields.IntField(default=0)
    position = fields.IntField(null=True)
    q1 = fields.CharField(max_length=255, null=True)
    q2 = fields.CharField(max_length=255, null=True)
    q3 = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "qualifying"


class Races(models.Model):
    id = fields.IntField(pk=True, source_field="raceId")
    year = fields.IntField(default=0)
    round = fields.IntField(default=0)
    circuit_id = fields.IntField(default=0, source_field="circuitId")
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

    def __repr__(self) -> str:
        return str(self)


class Results(models.Model):
    id = fields.IntField(pk=True, source_field="resultId")
    race_id = fields.IntField(default=0, source_field="raceId")
    driver_id = fields.IntField(default=0, source_field="driverId")
    constructor_id = fields.IntField(default=0, source_field="constructorId")
    number = fields.IntField(null=True)
    grid = fields.IntField(default=0)
    position = fields.IntField(null=True)
    position_text = fields.CharField(
        max_length=255, default="", source_field="positionText"
    )
    position_order = fields.IntField(default=0, source_field="positionOrder")
    points = fields.FloatField(default=0)
    laps = fields.IntField(default=0)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)
    fastest_lap = fields.IntField(null=True, source_field="fastestLap")
    rank = fields.IntField(default=0)
    fastest_lap_time = fields.CharField(
        max_length=255, null=True, source_field="fastestLapTime"
    )
    fastest_lap_speed = fields.CharField(
        max_length=255, null=True, source_field="fastestLapSpeed"
    )
    status_id = fields.IntField(default=0, source_field="statusId")

    class Meta:
        table = "results"


class Seasons(models.Model):
    year = fields.IntField(default=0)
    url = fields.CharField(max_length=255, default="")

    class Meta:
        table = "seasons"

    def __str__(self) -> str:
        return f'<Season: "{self.year}">'

    def __repr__(self) -> str:
        return str(self)


class SprintResults(models.Model):
    id = fields.IntField(pk=True, source_field="sprintResultId")
    race_id = fields.IntField(default=0, source_field="raceId")
    driver_id = fields.IntField(default=0, source_field="driverId")
    constructor_id = fields.IntField(default=0, source_field="constructorId")
    number = fields.IntField(default=0)
    grid = fields.IntField(default=0)
    position = fields.IntField(null=True)
    position_text = fields.CharField(
        max_length=255, default="", source_field="positionText"
    )
    position_order = fields.IntField(default=0, source_field="positionOrder")
    points = fields.FloatField(default=0)
    laps = fields.IntField(default=0)
    time = fields.CharField(max_length=255, null=True)
    milliseconds = fields.IntField(null=True)
    fastest_lap = fields.IntField(null=True, source_field="fastestLap")
    fastest_lap_time = fields.CharField(
        max_length=255, null=True, source_field="fastestLapTime"
    )
    status_id = fields.IntField(default=0, source_field="statusId")

    class Meta:
        table = "sprintResults"


class Status(models.Model):
    id = fields.IntField(pk=True, source_field="statusId")
    status = fields.CharField(max_length=255, default="")

    class Meta:
        table = "status"

    def __str__(self) -> str:
        return f'<Status: "{self.status}">'

    def __repr__(self) -> str:
        return str(self)
