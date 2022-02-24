from django.shortcuts import render
from .my_functions import *

# Create your views here.
def home(request):
	#IF posted a salary, then do calculation
	if request.method=="POST":
		salary = float(request.POST['salary'])
		inflation = float(request.POST['inflation'])

		display_inflation = inflation
		inflation = inflation/100 + 1
		should_be_future_salary, percentage_change = tax_creep_fun(salary, inflation)


		content = {
			'salary': salary,
			'display_inflation': display_inflation,
			'should_be_future_salary': should_be_future_salary,
			'percentage_change': percentage_change,
		}
		return render(request, 'home.html', content)

	else:#IF visiting site, have empty form boxes

		return render(request, 'home.html', {})
