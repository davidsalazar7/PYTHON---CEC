def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    if year < 1500 or month < 1 or month < 12:
        return None
    
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    res=days[month-1]
    if month == 2 and isYearLeap(year):
        res=29
    return res
'''    
    list30=[4,6,9,11]
    list31=[1,3,5,7,8,10,12]
    if isYearLeap(year) == True and month == 2:
        return 29
    elif isYearLeap(year) == False and month == 2:
        return 28
    elif month in list30:
        return 30
    elif month in list31:
        return 31
'''
  
'''
30 abril, junio, septie, nov

31 enero, marzo, mayo, julio, agosto, octubre, diciembre

28,29 febrero

list30=[4,6,9,11]

list31=[1,3,5,7,8,10,12]

'''

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print(" OK")
	else:
		print(" Failed")
