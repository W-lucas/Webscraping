# import module
import requests


# create a funciton to test the page
# pass the url
def url_ok():
	url = 'https://www.buyrentkenya.com/land-for-sale'
	# exception block
	try:
		
		# pass the url into
		# request.hear
		response = requests.head(url)
		
		# check the status code
		if response.status_code == 200:
			return url
		else:
			return False
	except requests.ConnectionError as e:
		return e