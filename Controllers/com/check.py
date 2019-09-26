import socket

class CHECK:
	def revisar():
		try:
			socket.gethostbyname('google.com')
			c = socket.create_connection(('google.com', 80), 1)
			c.close()
			return True
		except socket.gaierror:
			return False
		except socket.error:
			return False
