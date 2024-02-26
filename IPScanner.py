import ipaddress
import yaml
import requests

def check(ip):
	# Use the ip_address function from the ipaddress module to check if the input is a valid IP address
	try:
		ipaddress.ip_address(ip)
		print("Valid IP address")
	except ValueError:
		# If the input is not a valid IP address, catch the exception and print an error message
		print("Invalid IP address")


if __name__ == '__main__':
	# READING all the IPs from the YAML inpiut files.
	with open('ips.yaml', 'r') as f:
		data = yaml.full_load(f)
	for ip in data.get('ips'):
		# Logic to check if IP VALID.
        check(ip)
		response=requests.get(ips)
		# Logic to check if IP is belonging to NGINX or IIS HOST based on response headers
		print(response.headers)
		if response.headers.Server == "Nginx":
			print("IP is hosted on Nginx server")
		elif response.headers.Server == "IIS":
			print("IP is hosted on Nginx server")
		else:
			print("IP is hosted on other server")
    


		
