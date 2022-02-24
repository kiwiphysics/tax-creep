from django.shortcuts import render
from .my_functions import *

# Create your views here.
def home(request):
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

	else:

		return render(request, 'home.html', {})
