from django.db import models


class Lane(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    damage = models.IntegerField()
    images = models.ImageField(blank=True, upload_to="images", null=True)
    road_address = models.CharField(max_length=64)  # 도로명주소

    class Meta:
        db_table = "Lane"


class Report(models.Model):
    lane_id = models.ForeignKey(
        "Lane", related_name="lane", on_delete=models.CASCADE, db_column="lane_id"
    )
    content = models.TextField()
    report_images = models.ImageField(blank=True, upload_to="images", null=True)


class Scrap(models.Model):
    lane_id = models.ForeignKey("Lane", on_delete=models.CASCADE, db_column="lane_id")
    user_id = models.ForeignKey(
        "Accountsapp.User", on_delete=models.CASCADE, db_column="user_id"
    )

    class Meta:
        db_table = "Scrap"
