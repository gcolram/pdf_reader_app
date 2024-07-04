import requests

url = 'http://127.0.0.1:5000/read_pdf'
files = {'file': open('example.pdf', 'rb')}  # Asegúrate de que 'example.pdf' sea el nombre correcto del archivo PDF que estás usando
response = requests.post(url, files=files)

print(response.json())
