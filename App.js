import React, { useState } from 'react';
import axios from 'axios';

function App() {
  // Replace with your actual features
  const [form, setForm] = useState({
    feature1: '',
    feature2: '',
    feature3: ''
  });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:5000/predict', form);
    setResult(res.data.prediction);
  };

  return (
    <div style={{ maxWidth: 400, margin: 'auto', padding: 20 }}>
      <h2>Pulmonary Disease Prediction</h2>
      <form onSubmit={handleSubmit}>
        <input name="feature1" placeholder="Feature 1" value={form.feature1} onChange={handleChange} required /><br />
        <input name="feature2" placeholder="Feature 2" value={form.feature2} onChange={handleChange} required /><br />
        <input name="feature3" placeholder="Feature 3" value={form.feature3} onChange={handleChange} required /><br />
        <button type="submit">Predict</button>
      </form>
      {result !== null && (
        <div>
          <h3>Prediction: {result === 1 ? "Disease Detected" : "No Disease"}</h3>
        </div>
      )}
    </div>
  );
}

export default App; 