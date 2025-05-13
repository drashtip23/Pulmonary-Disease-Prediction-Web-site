# Pulmonary Disease Prediction Web App

This project provides a web interface for predicting pulmonary disease using a machine learning model.

## Project Structure

- `backend/`: Flask API for serving the ML model
- `frontend/`: React UI for user interaction

## Getting Started

### 1. Backend Setup

1. Place your dataset (`Pulmonary Disease- Lung Cancer Dataset.csv`) in the `backend/` folder.
2. Edit `train_model.py` to use your actual feature and target column names.
3. Run the training script:
   ```bash
   cd backend
   pip install -r requirements.txt
   python train_model.py
   ```
4. Start the Flask API:
   ```bash
   python app.py
   ```

### 2. Frontend Setup

1. Open a new terminal and go to the `frontend/` folder:
   ```bash
   cd frontend
   npm install
   npm start
   ```
2. The React app will open in your browser (usually at http://localhost:3000).

## Usage
- Enter the required features in the form and click Predict.
- The result will show if pulmonary disease is detected or not.

## Notes
- Update feature names in both backend and frontend to match your dataset.
- Deploy backend and frontend for public access if needed. 