from django import forms
from django import views
from django import Items
class forms(forms.ModelForm):
    class Meta:
        model=Items,
        fields=[
            'customer_name',
            'item_type',
            'image',
            'status',
            'cost',

        ]
    widget={
        'description':forms.Textarea({'row:4'})
    }
