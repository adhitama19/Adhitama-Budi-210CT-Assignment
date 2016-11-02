from datetime import date


def countDays (days, month, year):
	input_Date = date(year, month, days)
	final_Date = date(2016, 12, 31)
	count_Days = final_Date - input_Date
	count_days_count = int(count_Days.days)
	days_Passed = int(365 - count_days_count)
	return ("days passed: %d , days remaining: %d" % (count_days_count, days_Passed))
	

d = 26
m = 9
y = 2016

print(countDays(d, m, y))
	
