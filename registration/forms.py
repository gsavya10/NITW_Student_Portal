from django import forms
from django.forms.widgets import DateInput


Payment_Mode = (
	('-','--SELECT ONE--'),
	('-','NEFT'),
	('-','I Collect'),
	('-','Swift'),
	)

Payment_Category = (
	('-','--SELECT ONE--'),
	('-','Chief Warden'),
	)

class AddTransactionDetails(forms.Form):

	transaction_id = forms.CharField(
		required = True,
		label = 'Transaction ID',
		max_length = 32,
		widget = forms.TextInput(
			attrs={
			"class":"form-control",
			}
		)
	)

	mess_dues = forms.IntegerField(
		required = True,
		label = 'Mess Dues',
		widget = forms.NumberInput(
			attrs={
			"class":"form-control",
			}
		)
	)

	mess_advance = forms.IntegerField(
		required = True,
		label = 'Mess Advance',
		widget = forms.NumberInput(
			attrs={
			"class":"form-control",
			}
		)
	)

	total_amount = forms.IntegerField(
		required = True,
		label = 'Total Amount',
		widget = forms.NumberInput(
			attrs={
			"class":"form-control",
			}
		)
	)

	payment_mode = forms.CharField(
		required = True,
		label = 'Payment Mode',
		max_length = 32,
		widget = forms.Select(
			choices = Payment_Mode,
			attrs={
			"class": "form-control",
			}
		)
	)

	payment_category = forms.CharField(
		required = True,
		label = 'Payment Category',
		max_length = 32,
		widget = forms.Select(
			choices = Payment_Category,
			attrs={
			"class": "form-control",
			}
		)
	)