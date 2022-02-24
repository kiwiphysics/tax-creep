def calculate_take_home_pay(income):
	#Given a salary, calculates your after-tax income. Does NOT account for ACC levy
	tax_brackets = [0, 14001, 48001, 70001, 180001]
	tax_rates = [10.5, 17.5, 30, 33, 39]

	if income < tax_brackets[1]:
		after_tax_income = income * (100-tax_rates[0])/100

	elif income < tax_brackets[2]:
		after_tax_income = (income - tax_brackets[1]) * (100-tax_rates[1])/100 + 12530

	elif income < tax_brackets[3]:
		after_tax_income = (income - tax_brackets[2]) * (100-tax_rates[2])/100 + 40580

	elif income < tax_brackets[4]:
		after_tax_income = (income - tax_brackets[3]) * (100-tax_rates[3])/100 + 55980

	else:
		after_tax_income = (income-tax_brackets[4]) * (100 - tax_rates[4])/100 + 129680

	return after_tax_income

def reverse_tax_calculator(after_tax_income):
	#Given your after tax income, calculates your pretax income
	
	if after_tax_income < 12530:
		income = after_tax_income / 0.895
	elif after_tax_income < 40580:
		income = (after_tax_income - 12530) / 0.825 + 14000
	elif after_tax_income < 55980:
		income = (after_tax_income - 40580) / 0.7 + 48000
	elif after_tax_income < 129680:
		income = (after_tax_income - 55980) / 0.67 + 70000
	else:
		income = (after_tax_income - 129680) / 0.61 + 180000

	return income

def tax_creep_fun(salary, inflation):
	#Works out what percentage you actually need to ask for, to match real inflation
	current_after_tax = calculate_take_home_pay(salary)
	should_be_future_after_tax = current_after_tax * inflation
	should_be_future_salary = round(reverse_tax_calculator(should_be_future_after_tax), 2)

	percentage_change = round((should_be_future_salary-salary)/salary *100, 2)

	return should_be_future_salary, percentage_change