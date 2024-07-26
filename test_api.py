import requests

url = 'https://pdf-reader-app.onrender.com/read_pdf'  # URL de tu aplicación en Render
files = {'file': open('example.pdf', 'rb')}  # Asegúrate de proporcionar la ruta correcta al archivo PDF
response = requests.post(url, files=files)

print(response.json())
