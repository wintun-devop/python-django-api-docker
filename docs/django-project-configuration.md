### Django
```
django-admin startproject djangoapp
```
```
cd djangoapp
```
```
python manage.py startapp apis
```
###  Database Setup
- djangoapp/djangoapp/settings.py
- - database
```

```
- - app setting
```

```
- - database routes add
```
DATABASE_ROUTERS = ['djangocrud.routers.ReplicaRouter']
```
### Model
- sample model here
```
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=200,unique=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    #set only once at creation
    created_at = models.DateTimeField(auto_now_add=True)
    #updated each time model is saved  
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (
            f"Product(id={self.id}, name='{self.name}', model='{self.model}', "
            f"price={self.price}, quantity={self.quantity}, "
            f"created_at='{self.created_at}', updated_at='{self.updated_at}')"
        )
```
- create serializer
```
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    quantity = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        fields = ('__all__')
```
- create url pattern on app(not on main project)
```
```
- make database migration (preparing for migration)
```
python manage.py makemigrations

```
- database migration (actual migration)
```
python manage.py migrate
```
### superuser creation
```
python manage.py createsuperuser
```
### running server
```
python manage.py runserver

```