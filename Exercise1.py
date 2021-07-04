
user = {'document': 'rx','email':'red@gmail.com','address': 'ST JOHN 21 AR'}
		

def harmonizer(user):
	"""Returns a list of emails of a user"""

	#This block of code is to validate if there any emails in the source, so we can include them in a list and then return the list of emails of a user
	#This could include a logic where if emails not exist then finish the program saying the list of emails is empty so that we don´t execute the whole code
	emails = user['email']
	#print (emails)
	if not emails: 
		emails = ''
		print('emails not exist')
	
	#This block of code is to create a list	that includes all the user values (document, address and email)
	emails = []
	#print(user)
	for document in user.values():
		emails.append(document)
		print(document)

	print(emails)

	emails = list(set(filter(None, emails)))
	print(emails)
	print('email done')
	return {'email': emails}

if __name__ == '__main__':
	a = harmonizer(user)
	print (a)

