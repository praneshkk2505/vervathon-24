from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace this URL with the endpoint of your text-to-3D model API
API_URL = 'https://api.example.com/generate-3d'  # Placeholder for the actual API

# The index route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the text-to-3D image generation request
@app.route('/generate', methods=['POST'])
def generate_3d_image():
    try:
        # Get the input text from the form
        input_text = request.form.get('input_text')
        
        # Send request to the API (or your custom model) for 3D generation
        response = requests.post(API_URL, json={'text': input_text})

        if response.status_code == 200:
            # Assuming the API returns the URL of the generated 3D model/image
            result = response.json()
            image_url = result.get('image_url')

            return jsonify({'status': 'success', 'image_url': image_url})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to generate 3D image'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
