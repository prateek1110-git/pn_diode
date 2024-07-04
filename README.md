
# PN Junction Diode Output Current Prediction

This project aims to predict the output current of a p-n junction diode based on various input parameters. It uses a machine learning model to make the predictions and is implemented using Flask for the web interface.

## Project Structure

- `SVR_model.ipynb`: Jupyter Notebook used for training the Support Vector Regression (SVR) model.
- `requirements.txt`: Contains all the required libraries
- `app.py`: The main Flask application file that handles the web server and prediction logic.
- `web.html`: HTML template for the web interface.

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/prateek1110-git/pn_diode.git
    ```

2. **Create a virtual environment:**
    ```bash
    conda create -p venv python==3.7 -y
    ```

3. **Activate the virtual environment:**
      ```bash
      conda activate venv/
      ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask application:**
    ```bash
    python app.py
    ```

6. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **Enter the input parameters in the form:**
    - n_doping (cm⁻³)
    - p_doping (cm⁻³)
    - Temperature (K)
    - Electron Carrier Lifetime (s⁻¹)
    - Hole Carrier Lifetime (s⁻¹)
    - Bias Voltage (V)

2. **Click on the 'Predict' button to get the predicted output current.**

3. **The previous predictions will be displayed on the web page.**

4. **To clear the prediction history, click on the 'Clear History' button.**

## Explanation of Files

- **`app.py`:**
  - Contains the Flask web application.
  - Routes:
    - `/`: Home route that renders the `web.html` template.
    - `/predict`: Handles form submission and prediction logic.
    - `/clear`: Clears the prediction history.
  - Uses session management to store previous inputs and outputs.

- **`SVR_model.ipynb`:**
  - Notebook for training the Support Vector Regression (SVR) model.
  - Data preprocessing, model training, and evaluation steps.

- **`web.html`:**
  - HTML template for the web interface.
  - Form for input parameters.
  - Displays the predicted output current.
  - Shows the history of previous predictions.
  - Button to clear the prediction history.

## Model Details

The machine learning model used in this project is a Support Vector Regression (SVR) model. It was trained using a dataset of PN Junction Diode characteristics. The input features include doping concentrations, temperature, carrier lifetimes, and bias voltage.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgements

Thanks to all the open-source contributors and the Flask, Pandas, NumPy, and Scikit-Learn communities.

