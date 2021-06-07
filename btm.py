#!/usr/bin/python3

from datetime import datetime, time, date

class BTM(object):
	"""docstring for BTM"""

	def banner(self):

		programName = 'Bīrth Dãy Téllèr Mâçhïñē'
		programName = f'* {programName} *'
		version = 'Version 2.1'

		star = ''
		for i in range(len(programName)):
			star += '*'

		print('\n' + star)
		print(programName)

		star = ''
		for i in range(len(programName) - len(version) - 4 ):
			star += '*'

		print(f'{star} {version} **')


	def errorMessage(self):
		print ('\n[×] Are you alien? Sorry. Invalid')
		exit()

	def errorNumber(self, userInput):
		try:
			val = int(userInput)
		except ValueError:
			self.errorMessage()

	def errorString(self, userInput):
		try:
			val = str(userInput)
		except ValueError:
			self.errorMessage()

	def greetings(self, name):
		print('')
		welcome = f'* {name}, welcome to BTM *'
		star = '*'
		space = ' '
		for i in range(len(welcome) - 5):
			space += ' '
		for i in range(len(welcome) - 1):
			star += '*'
		for i in range(6):
			if i == 1 or i ==5:
				print(star)
			elif i == 2 or i == 4:
				print(f'* {space} *')
			elif i == 3:
				print(welcome)


	def information(self, birthDay, birthMonth, birthYear):
		self.birthDay = birthDay
		self.birthMonth = birthMonth
		self.birthYear = birthYear

		months = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
		self.days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )

		today = date.today()
		self.errorNumber(self.birthDay)
		self.birthDay = int(self.birthDay)

		if self.birthDay < 1 or self.birthDay > 31:
			self.errorMessage()

		for i in months:
			if i == self.birthMonth:
				self.birthMonth = months.index(self.birthMonth) + 1

		self.errorNumber(self.birthYear)
		self.birthYear = int(self.birthYear)

		if self.birthYear < 1 or self.birthYear >=  today.year and self.birthMonth > today.month or self.birthMonth > today.month and self.birthDay > today.day:
			self.errorMessage()

		if self.birthDay == 29 and self.birthMonth == 2 and self.birthYear % 4 != 0:
			self.errorMessage()

		self.currentYear = today.year
		currentBirthday = date(self.currentYear, self.birthMonth, self.birthDay)

		if self.birthDay == 29 and self.birthMonth == 2 and self.birthYear % 4 == 0:
			self.currentYear += 4
		elif today > currentBirthday:
			self.currentYear += 1
		
		currentBirthday = date (self.currentYear, self.birthMonth, self.birthDay)

		weekNumber = date.weekday(date.today())

		self.currentDays = (currentBirthday - today).days
		self.currentDays += weekNumber

		totalDays = (date(self.birthYear, self.birthMonth, self.birthDay) - today).days

		year = today.year - self.birthYear

		if self.birthMonth > today.month or self.birthMonth == today.month and self.birthDay > today.day:
			year -= 1

		if today.month > self.birthMonth:
			month = abs(year * 12) + today.month - self.birthMonth
		else: month = abs(year * 12) + today.month + self.birthMonth - 1
		week = abs(totalDays // 7)
		day = abs(totalDays) - 1
		hour = abs(totalDays * 24) + datetime.time(datetime.today()).hour
		minute = abs(hour * 60) + datetime.time(datetime.today()).minute
		second = abs(minute * 60) + datetime.time(datetime.today()).second

		weekDay = str(self.days[(totalDays + weekNumber) % 7])

		return {
		'years': year,
		'months': month,
		'weeks': week,
		'days': day,
		'hours': hour,
		'minutes': minute,
		'seconds': second,
		'weekDay': weekDay
		}


	def futureInformation(self, number):
		self.errorNumber(number)
		number = int(number)

		if number < 1:
			print ('[=] Year\'s number can not be 0 or negative\n')
			exit()

		print('')

		for i in range(number):
			weekNumber = self.currentDays % 7
			if self.currentYear % 4 == 0:
				print ('\t' + str(self.currentYear) +' - '+ str(self.days[weekNumber]) + ' - Leap Year')
			else:
				print ('\t' + str(self.currentYear) +' - '+ str(self.days[weekNumber]))

			self.currentYear += 1

			if self.birthDay == 29 and self.birthMonth == 2 and self.birthYear % 4 ==0:
				self.currentDays += 1460
				self.currentYear += 3
			if self.currentYear % 4 == 0 and self.birthMonth >= 3:
				self.currentDays += 366

			elif self.currentYear % 4 == 1 and self.birthMonth <= 2:
				self.currentDays += 366
			else:
				self.currentDays += 365

	def reload(self):
		reloader = input('\n[+] Wanna see birth day again? [y/N]: ').lower()
		self.errorString(reloader)

		if reloader == 'y':
			main()
		elif reloader == 'n':
			self.author()
		else: self.errorMessage()

	def author(self):
		print ('\n[=] Thank you for using this program')
		print ('\n∆ Creator : https://www.github.com/s4gor ∆')
		exit()



def main():

	user = BTM()

	user.banner()

	name = input('\n[+] Enter your name: ').strip()

	user.greetings(name.title())

	birthDay = input ('\n[+] Enter your birth day: ')
	birthMonth = input('[+] Enter your birth month: ').lower()
	birthYear = input ('[+] Enter your birth year: ')


	information = user.information(birthDay, birthMonth, 
		birthYear)

	print(f'\n[=] Birth date: {birthDay.title()} {birthMonth.title()}, {birthYear.title()}')

	weekDay = information['weekDay']

	print (f'\n[=] You were born on {weekDay.upper()}')

	print('\n\t[Information]')
	for info in information:
		if info == 'weekDay': continue
		print(f'\t{info.title()}: {information[info]}')

	active = input ("\n[+] Do you want to see your next year's birth day ? [Y/n]: ").lower()
	user.errorString(active)

	if active == 'y':
		number = input ("\n[+] How many year's birth day do you want to see: ")
		user.futureInformation(number)
		user.reload()
	elif active == 'n':
		user.reload()
	else: user.errorMessage()

if __name__ == '__main__':
	main()
