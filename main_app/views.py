from django.shortcuts import render

from main_app.forms import TextForm
from main_app.forms import DropdownForm

import main_app.tax_calc as tc


def index(request):
	if request.method == "POST":
		form = TextForm(request.POST)
		dropdown = DropdownForm(request.POST)
		price = ""
		province = ""
		tax=""
		tip=""
		total =""
		temp=""

		if form.is_valid():
			province = dropdown.data['province']
			price = form.cleaned_data['price']
			try:
				price = float(price)
			except:
				return render(
					request,
					'main_app/home.html',
					{'form':form, 'dropdown':dropdown,'error':"You have to put the numberic number"}
				)
			tax = "Price with tax "+ '${:,.2f}'.format(tc.getTax(price,province))
			tip = "Price with tip "+ '${:,.2f}'.format(tc.getTip(price,province))
			temp = tc.getTax(price,province) + tc.getTip(price,province) + price 
			total = "Total price is $" + '{:,.2f}'.format(temp)

		return render(
			request, 
			'main_app/home.html',

			{'form':form, 'dropdown':dropdown, 'price':price, 'province':province, 'tax':tax, 'tip':tip, 'total':total}
			)
	else:
		form = TextForm()
		dropdown = DropdownForm()
		return render(
			request, 
			'main_app/home.html', 

			{'form':form, 'dropdown':dropdown}
			)