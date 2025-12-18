password=input("Enter your password:")
confirm_password = input("Confirm Password:")

if password == confirm_password:
	print("Password changed")
else:
	if password.casefold() == confirm_password.casefold():
		print("Please check the cases and Try Again")
	else:
		print("Wrong password")