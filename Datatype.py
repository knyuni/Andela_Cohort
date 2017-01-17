def data_type(a):
	"""Takes one input and returns a value in respect to data type of the input  """
	a_type =type(a)


	if a_type == str:

		return len(a)


	elif a_type ==bool:

		return a


	elif a_type ==int:

		if a == 100:

			return 'equal to 100'
			
		elif a < 100:
			return 'less than 100'

		else:
			return 'more than 100'

	elif a_type ==list:
		try:
			if a[2]:
				return a[2]
		except(IndexError):
			return None
	else:
return 'no value'