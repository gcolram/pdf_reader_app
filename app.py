from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)

@app.route('/read_pdf', methods=['POST'])
def read_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Leer el archivo PDF
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        
        text = ''
        form_data = {}

        # Extraer texto y datos de formularios de cada página
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()

            # Extraer datos de los formularios
            for field in page.widgets():
                if field.field_name and field.field_value:
                    form_data[field.field_name] = field.field_value

        return jsonify({'text': text, 'form_data': form_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
