from django.db import models
from django.utils import timezone


class OrderAddress(models.Model):
    company_name = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=512)
    address_line2 = models.CharField(max_length=512)
    city = models.CharField(max_length=52)
    state = models.CharField(max_length=52)
    country = models.CharField(max_length=52)
    postcode = models.CharField(max_length=22)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id) + " : " + self.company_name


class Orders(models.Model):
    ORDER_TYPE = (
        ('S', 'Sale'),
        ('F', 'Free Trial'),
        ('M', 'Sample'),
        ('R', 'Return'),
    )
    ORDER_STATUS = (
        ('N', 'New'),
        ('P', 'Prepared'),
        ('D', 'Dispatch'),
        ('A', 'Assemble'),
        ('E', 'DEAD'),
    )
    ID = models.CharField(max_length=512, db_column="ID")
    CustomerID = models.CharField(max_length=512, db_column="CustomerID")
    OrderSummary = models.CharField(max_length=512, db_column="OrderSummary")
    OrderMessage = models.CharField(max_length=512, db_column="OrderMessage")
    OrderCurrency = models.CharField(max_length=512, db_column="OrderCurrency")
    OrderStatus = models.CharField(max_length=512, db_column="OrderStatus")
    OrderType = models.CharField(max_length=512, db_column="OrderType")
    OrderContact = models.CharField(max_length=512, db_column="OrderContact")
    CreatedDate = models.CharField(max_length=512, db_column="CreatedDate")
    ModifiedDate = models.CharField(max_length=512, db_column="ModifiedDate")

    class Meta:
        db_table = "Orders"

    def __str__(self):
        return str(self.ID)+" : "+str(self.OrderSummary)


class OrderItem(models.Model):
    ID = models.CharField(max_length=512, db_column="ID")
    OrderID = models.CharField(max_length=512, db_column="OrderID")
    PackageID = models.CharField(max_length=512)
    ProductType = models.CharField(max_length=512)
    HardwareID = models.CharField(max_length=512)
    ItemQuantity = models.CharField(max_length=512)
    ItemPrice = models.CharField(max_length=512)
    ItemDescription = models.CharField(max_length=512,db_column="ItemDescription")
    ItemFullDescription = models.CharField(max_length=512)
    ItemType = models.CharField(max_length=512)
    ItemStatus = models.CharField(max_length=512)
    CreatedDate = models.DateTimeField(default=timezone.now)
    ModifiedDate = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "OrderItems"

    def __str__(self):
        return str(self.OrderID)
