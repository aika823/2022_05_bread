from this import d
from django.db import models
from app_api.functions_db import get_values
from django.contrib.auth.models import AbstractUser

# Override Django Auth User
class User(AbstractUser):
    nickname = models.CharField(max_length=10, db_column="nickname", null=False, default="")
    email_certified = models.BooleanField(db_column="email_certified", null=False, default=False)
    contact = models.CharField(max_length=20, db_column="contact", null=False, default="연락처")
    password_060 = models.CharField(max_length=4, db_column="password_060", null=True, default=None)
    def get_values(self):
        return get_values(self)
    class Meta:
        db_table = "user"


# class Master(models.Model):
    
#     # 유저 정보
#     user = models.OneToOneField(to=User, db_column="user", null=True, on_delete=models.SET_NULL, unique=True)
    
#     # 상담사 기본 정보 (관리자용)
#     name = models.CharField(max_length=20, db_column="name", null=False, default='')
#     address = models.CharField(max_length=200, db_column="address", null=False, default="주소")
#     contact = models.CharField(max_length=20, db_column="contact", null=False, default="연락처")
#     email = models.EmailField(max_length=100, db_column="email", null=False, default="이메일")
    
#     # 상담사 기본 정보 (유저용)
#     code = models.CharField(max_length=6, db_column="code", null=False, default="000")
#     type = models.CharField(max_length=10, db_column="type", null=False, default="타로")
#     nickname = models.CharField(max_length=20, db_column="nickname", null=False, default="상담명", unique=True)
#     image = models.ImageField(upload_to="media/images/master", null=True)
#     detail = models.CharField(max_length=500, db_column="detail", null=True)
#     hashtag = models.CharField(max_length=20, db_column="hashtag", null=False, default="#연애타로")
    
#     # 공지, 약력, 인삿말
#     notice = models.CharField(max_length=500, db_column="notice", null=False, default="")
#     history = models.CharField(max_length=500, db_column="history", null=False, default="")
#     greeting = models.CharField(max_length=500, db_column="greeting", null=False, default="")

#     # 활성화 여부
#     active = models.BooleanField(db_column="active", null=False, default=False)

#     def get_values(self):
#         return get_values(self)
#     class Meta:
#         db_table = "master"


# class Counseling(models.Model):
#     date = models.DateField(db_column="date", auto_now_add=True)
#     time = models.TimeField(db_column="time", null=False, default="00:00")
#     master = models.ForeignKey(to=Master, db_column="master", null=True, on_delete=models.CASCADE)
#     user = models.ForeignKey(to=User, db_column="user", null=True, default=None,  on_delete=models.CASCADE)
#     def get_values(self):
#         return get_values(self)
#     class Meta:
#         db_table = "counseling"


# class Review(models.Model):
#     counseling = models.ForeignKey(to=Counseling, null=True, default=None, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50, db_column="title", null=True)
#     content = models.CharField(max_length=500, db_column="content", null=True)
#     date = models.DateField(db_column="date", auto_now_add=True)
#     reply_to = models.ForeignKey(db_column="reply_to", to="self", null=True, default=None, on_delete=models.CASCADE)
#     grade = models.IntegerField(db_column="grade", null=False, default=10)
#     point_given = models.BooleanField(db_column="point_givne", null=False, default=False)
#     def get_values(self):
#         return get_values(self)
#     class Meta:
#         db_table = "review"

# class ReviewImage(models.Model):
#     review = models.ForeignKey(to=Review, db_column="review", null=False, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="media/images/review", null=True)
#     def get_values(self):
#         return get_values(self)
#     class Meta:
#         db_table = "review_image"

# class Purchase(models.Model):
#     user = models.ForeignKey(to=User, db_column="user", null=False, on_delete=models.CASCADE)
#     mul_id = models.IntegerField(db_column="mul_id", null=False)
#     price = models.IntegerField(db_column="price", null=False)
#     goodname = models.CharField(db_column="goodname", null=False, max_length=500)
#     reqdate = models.DateTimeField(db_column="reqdate", null=False)
#     def get_values(self):
#         return get_values(self)
#     class Meta:
#         db_table = "purchase"

# class Event(models.Model):
#     title = models.CharField(max_length=50, db_column="title", null=True)
#     category = models.CharField(max_length=50, db_column="category", null=True)
#     content = models.CharField(max_length=50000, db_column="content", null=True)
#     created_at = models.DateTimeField(db_column='created_at', null=False, auto_now_add=True)
#     def get_values(self):
#         return get_values(self)
#     class Meta:
#         db_table = "event"
