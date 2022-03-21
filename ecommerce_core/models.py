

import json

from django.db import models
from django.utils import timezone


class ProductsTable(models.Model):
    name = models.CharField(max_length=100, db_column='name')
    description = models.TextField(db_column='description', default='', blank = True, null=True) 
    code = models.CharField(max_length=100, db_column='code')
    price = models.FloatField(db_column='price', null=True)
    rating = models.IntegerField(db_column='rating')
    review_count = models.IntegerField(db_column='review_count')
    img = models.TextField(db_column='img', default='', blank = True, null=True) 
    cat = models.CharField(max_length=100, db_column='cat')
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now)
    

    def __str__(self):
        product_data = {}
        product_data['id'] = self.id
        product_data['name'] = self.name 
        product_data['description'] = self.description
        product_data['code'] = self.code
        product_data['price'] = self.price
        product_data['rating'] = self.rating
        product_data['review_count'] = self.review_count
        product_data['img'] = self.img
        product_data['cat'] = self.cat
        product_data['create_at'] = str(self.create_at)

        return json.dumps(product_data)
 
    
    class Meta:
        db_table = "MASTER_PRODUCTS"
