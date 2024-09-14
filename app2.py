from flask import Flask, request, jsonify
from torchvision.transforms import transforms
from PIL import Image
import torch
import numpy as np
import glob
import os

app = Flask(__name__)

# Load the model checkpoint and classes
checkpoint = torch.load('C:\\Users\\Vaska\\Downloads\\checkpoint6.pt')
model = ConvNet(num_classes=38)
model.load_state_dict(checkpoint)
model.eval()

# Define the transformation for test data
trnsfrm = transforms.Compose([
    transforms.Resize((150, 150)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])


# Prediction function
def predict_bird(image_path, transform, model, classes, device):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        predicted_class = classes[predicted.item()]
        return predicted_class


@app.route('/', methods=['GET'])
def homepage():
    return 'Welcome to the homepage of your Flask application!'


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = file.filename
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        predicted_class = predict_bird(file_path, trnsfrm, model, classes, device)
        return jsonify({'predicted_class': predicted_class})


if __name__ == '__main__':
    app.run(debug=True)
