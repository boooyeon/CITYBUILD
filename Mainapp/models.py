from django.db import models

class Lane(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    damage = models.IntegerField()
    images = models.ImageField(blank=True, upload_to="images", null=True)

    class Meta:
        db_table = 'Lane'

class Building(Lane, models.Model):
    lane_id = models.ForeignKey("Lane", related_name="lane", on_delete=models.CASCADE, db_column="lane_id")
    city = models.CharField(max_length=32)  # 시
    county = models.CharField(max_length=32)  # 군
    district = models.CharField(max_length=32)  # 구
    road_address = models.CharField(max_length=64)  # 도로명주소
    
    class Meta:
        db_table = 'Building'

class Scrap(models.Model):
    scrap_id = models.AutoField(primary_key=True)
    lane_id = models.ForeignKey('Lane', on_delete=models.CASCADE, db_column='lane_id')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'Scrap'
        managed = False

