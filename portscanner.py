import nmap 

while True:
	nmScan = nmap.PortScanner()
	host = input("host(ip/url :)")
	port = input("port:")
	output = nmScan.scan(host,port)
	print(output)