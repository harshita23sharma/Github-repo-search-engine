from django import forms

class NameForm(forms.Form):
    your_product = forms.CharField(max_length=1000)
    # selected_choice = forms.CharField(max_length=100)

    # def __unicode__(self):
    #     return self.your_product
class SelectForm(forms.Form):
	vertical_choices = (("1", "ONE"),("2", "TWO"),("3","Three"),("4","Four"),("5","Five") )
	selected_choice = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple,)


# 	from django import forms

# class NameForm(forms.Form):
#     your_product = forms.CharField(max_length=1000)
#     # selected_choice = forms.CharField(max_length=100)

#     # def __unicode__(self):
#     #     return self.your_product
# class SelectForm(forms.Form):
# 	vertical_choices = (("1", "ONE"),("2", "TWO"),("3","Three"),("4","Four"),("5","Five") )
# 	selected_choice= forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)