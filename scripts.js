const imageForm = document.getElementById('imageForm');
const imageInput = document.getElementById('imageInput');
const submitButton = document.getElementById('submitButton');
const imageContainer = document.getElementById('imageContainer');

const express = require('express');
const app = express();

app.use(express.static('public', { 'extensions': ['html'] }));
app.listen(5500, () => {
  console.log('Server is running on port 5500');
});const express = require('express');

submitButton.addEventListener('click', () => {
  const file = imageInput.files[0];
  const reader = new FileReader();

  reader.onload = (event) => {
    const imageElement = document.createElement('img');
    imageElement.src = event.target.result;
    imageContainer.appendChild(imageElement);
  };

  reader.readAsDataURL(file);
});