document.addEventListener('DOMContentLoaded', function() {
  
  // Dark / Light Mode Toggle
  const modeToggle = document.getElementById('modeToggle');
  modeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
  });

  // Form & Prediction
  const form = document.getElementById('form');
  const resultCard = document.getElementById('result');
  const priceText = document.getElementById('price');
  const confidenceText = document.getElementById('confidenceText');
  const confidenceBar = document.getElementById('confidenceBar');
  const historyList = document.getElementById('historyList');

  form.addEventListener('submit', function(e){
    e.preventDefault(); // prevent page reload

    // Get values
    const year = parseInt(document.getElementById('year').value);
    const mileage = parseFloat(document.getElementById('mileage').value);
    const engine = parseFloat(document.getElementById('engine').value);

    const fuel = document.getElementById('fuel').value;
    const transmission = document.getElementById('transmission').value;
    const seller = document.getElementById('seller').value;

    if (!year || !mileage || !engine || !fuel || !transmission || !seller){
      alert("Please fill all fields.");
      return;
    }

    // Fake prediction formula for demo
    const basePrice = 20000;
    const ageFactor = (2026 - year) * 1000;
    const mileageFactor = mileage * 0.05;
    const engineFactor = engine * 5;

    let predictedPrice = basePrice - ageFactor - mileageFactor + engineFactor;

    // Adjust for fuel type
    if(fuel === "Diesel") predictedPrice *= 1.05;
    if(fuel === "CNG") predictedPrice *= 0.95;

    // Transmission adjustment
    if(transmission === "Automatic") predictedPrice *= 1.1;

    predictedPrice = Math.max(1000, predictedPrice); // minimum value

    // Simulated confidence
    const confidence = Math.floor(Math.random() * 15) + 85; // 85-99%

    // Display results
    resultCard.style.display = 'block';
    priceText.innerText = `Predicted Value: $${predictedPrice.toFixed(2)}`;
    confidenceText.innerText = `Confidence: ${confidence}%`;
    confidenceBar.style.width = `${confidence}%`;

    // Add to history
    const li = document.createElement('li');
    li.innerText = `Year:${year} Mileage:${mileage} Engine:${engine} => $${predictedPrice.toFixed(2)}`;
    historyList.prepend(li); // latest on top
  });

});

// Reset form function
function resetForm() {
  document.getElementById('form').reset();
  document.getElementById('result').style.display = 'none';
}