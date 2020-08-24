# python version 3.6.2

from datetime import datetime, time, date

brthmnth = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')

bnr = 'Bīrth Dãy Téllèr Mâçhïñē'
bnr = f'* {bnr} *'
star = ''
vrsn = 'Version: 2'
for ln in range(len(bnr)):
	star += '*'
hl = star
print(star)
print(bnr)
star = ''
for i in range(len(bnr) - len(vrsn) - 4 ):
	star += '*'
print(f'{star} {vrsn} **')

def errnum(user_input):
	try:
		val = int(user_input)
	except ValueError:
		error()
		
def errstr(user_inpt):
	try:
		val = str(user_inpt)
	except ValueError:
		error()
						
def greetings():
	print ('\n[=] Thank you for using this program')
	print ('\n∆ Creator : https://www.github.com/s4gor ∆')
	exit()

# error function

def error():
	print ('\n[×] Are you alien? Sorry. Invalid')
	exit()
	
# main function
	
def main():
	
	z = input('\n[+] Enter your name: ')
	print('')
	z = f'{z}, Welcome to BTM'
	z = f'* {z} *'
	q = '*'
	spaces = ' '
	for i in range(len(z) - 5):
		spaces += ' '
	for i in range(len(z) - 1):
		q += '*'
	for i in range(6):
		if i == 1 or i ==5:
			print(q)
		elif i == 2 or i == 4:
			print(f'* {spaces} *')
		elif i == 3:
			print(z)
	
	# input of birth day, month, year
	c = date.today()
	
	birthday = input ('\n[+] Enter your birth day: ')
	errnum(birthday)
	birthday = int(birthday)
	if birthday < 1 or birthday > 31:
		error()
	
	
	birthmonth = input('[+] Enter your birth month: ')
	if birthmonth == brthmnth[0]:
		birthmonth = 1
	elif birthmonth == brthmnth[1]:
		birthmonth = 2
	elif birthmonth == brthmnth[2]:
		birthmonth = 3
	elif birthmonth == brthmnth[3]:
		birthmonth = 4
	elif birthmonth == brthmnth[4]:
		birthmonth = 5
	elif birthmonth == brthmnth[5]:
		birthmonth = 6
	elif birthmonth == brthmnth[6]:
		birthmonth = 7
	elif birthmonth == brthmnth[7]:
		birthmonth = 8
	elif birthmonth == brthmnth[8]:
		birthmonth = 9
	elif birthmonth == brthmnth[9]:
		birthmonth = 10
	elif birthmonth == brthmnth[10]:
		birthmonth = 11
	elif birthmonth == brthmnth[11]:
		birthmonth = 12
	else:
		error()
	
	birthyear = input ('[+] Enter your birth year: ')
	errnum(birthyear)
	birthyear = int(birthyear)
	if birthyear < 1 or birthyear >=  c.year and birthmonth > c.month or birthmonth > c.year and birthday > c.day:
		error()
		
	
	if birthday == 29 and birthmonth == 2 and birthyear % 4 != 0:
		error()
	
	# getting today's date and user's birthday'
	
	
	currentyear = c.year
	
	b = date (currentyear, birthmonth, birthday)
	
	# checking if user's birthday has been passed or not
	print(f'\n[=] Birth date[YYYY-MM-DD]: {date(birthyear, birthmonth, birthday)}' )
	
	if birthday == 29 and birthmonth == 2 and birthyear % 4 ==0:
		currentyear += 4
	elif c > b:
		currentyear += 1
	b = date (currentyear, birthmonth, birthday)
	
	# days calculation
	
	j = date.weekday(date.today())
	
	d = (b - c).days
	d = d + j
	
	a = (date(birthyear, birthmonth, birthday) - c).days 
	
	k = c.year - birthyear
	if birthmonth > c.month or birthmonth == c.month and birthday > c.day:
		k -= 1
	
	print('\n\t[Informations]')
	
	print(f'\tYears: {k}')
	
	k = abs(k * 12) + birthmonth
	
	print(f'\tMonths: {k}')
	
	k = abs(a // 7)
	
	print(f'\tWeeks: {k}')
	
	s = abs(a) - 1
	
	print(f'\tDays: {s}')
	
	k = abs(a * 24) + datetime.time(datetime.today()).hour
	
	print(f'\tHours: {k}')
	
	k = abs(k * 60) + datetime.time(datetime.today()).minute
	
	print(f'\tMinutes: {k}')
	
	k = abs(k * 60) + datetime.time(datetime.today()).second
	
	print(f'\tSeconds: {k}')
	
	k  = abs(k * 1000)
	
	print(f'\tMilliseconds: {k}')
	
	k = abs(k * 1000)
	
	print(f'\tMicroseconds: {k}')
	
	k = abs(k * 1000)
	
	print(f'\tNanoseconds: {k}')
	
	# week days
	
	days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )
	
	a += j
			
	a = a % 7
	
	print ('\n[=] You were born on ' + str(days[a]).upper())
	
	# birth day want to see
	global g
	g = input ("\n[+] Do you want to see your next year's birth day ? [Y/n]: ").lower()
	errstr(g)
	if g == 'y':
		t = input ("[+] How many year's birth day do you want to see: ")
		errnum(t)
		t = int(t)
		if t < 1:
			print ('[=] Print number can not be 0 or negative')
			exit()
			
		print ('')
	elif g == 'n':
		greetings()
	else:
		error()
	
	# loop for printing required year's birth day
		
	for i in range(t):
		
			c = d % 7
			if currentyear % 4 == 0:
				print ('\t' + str(currentyear) +' - '+ str(days[c]) + ' - Leap Year')
			else:
				print ('\t' + str(currentyear) +' - '+ str(days[c]))
		
			currentyear += 1
			
			if birthday == 29 and birthmonth == 2 and birthyear % 4 ==0:
				d += 1460
				currentyear += 3
			if currentyear % 4 == 0 and birthmonth >= 3:
				d += 366
				
			elif currentyear % 4 == 1 and birthmonth <= 2:
				d += 366
			else:
				d += 365
	
if __name__ == '__main__':
	main()


def reloader():
	while g == 'y':
		h = input('\n[+] Wanna see birth day again? [y/N]: ').lower()
		errstr(h)
		if h == 'y':
			print('')
			main()
		elif h == 'n':
			greetings()
		else:
			error()

if __name__ == '__main__':
	reloader()