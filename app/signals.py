import json
import os
from config.config.settings import BASE_DIR
from config.config.settings import DEFAULT_FROM_EMAIL
from app.models import Category,Product
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.core.mail import send_mail


#Category uchun
@receiver(pre_save, sender=Category)
def pre_save_category(sender, instance, **kwargs):
    print('before save category')

@receiver(post_save, sender=Category)
def post_save_category(sender, instance, created, **kwargs):
    if created:
        print('Category created')
        subject = 'Category created'
        message = 'Category succesfully created and verificated by admin Omadbek'
        from_email = DEFAULT_FROM_EMAIL
        to = 'qosimoff701@gmail.com'
        send_mail(subject, message, from_email, [to, ], fail_silently=False)
    else:
        print('Category updated')    



@receiver(pre_delete, sender=Category)
def pre_delete_category(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'texnomartuz/delete_categories', f'category_{instance.id}.json')

    category_data = {
        'id': instance.id,
        'category_name': instance.category_name,
        'slug': instance.slug
    }


    with open(file_path, 'w') as json_file:
        json.dump(category_data, json_file, indent=4)

    print('Category saved json file before deleted')



#For Product
@receiver(pre_save, sender=Product)
def pre_save_product(sender, instance, **kwargs):
    print('before save product')

@receiver(post_save, sender=Product)
def post_save_product(sender, instance, created, **kwargs):
    if created:
        print('Product created')
        subject = 'Product created'
        message = 'Product succesfully created and verificated by admin Omadbek'
        from_email = DEFAULT_FROM_EMAIL
        to = 'qosimoff701@gmail.com'
        send_mail(subject, message, from_email, [to, ], fail_silently=False)
    else:
        print('Product updated')    



@receiver(pre_delete, sender=Product)
def pre_delete_product(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'texnomartuz/delete_products', f'category_{instance.id}.json')

    product_data = {
        'id': instance.id,
        'product_name': instance.product_name,
        'slug': instance.slug
    }


    with open(file_path, 'w') as json_file:
        json.dump(product_data, json_file, indent=4)

    print('Product saved json file before deleted')