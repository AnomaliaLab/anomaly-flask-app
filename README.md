# Anomaly Detection Flask App

This project is a simple web application for detecting anomalies in tabular data using the Isolation Forest algorithm. Users can upload a CSV file and specify a contamination rate to identify anomalous data points.

## Features

- Upload CSV files via a web interface
- Set contamination rate for anomaly detection
- Download results with anomaly labels
- Powered by Flask, pandas, and scikit-learn

## Getting Started

### Prerequisites

- Python 3.8+
- See [`requirements.txt`](requirements.txt) for required packages

### Installation

1. Clone this repository
2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the App

```sh
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Usage

1. Upload a CSV file containing your data.
2. Set the contamination rate (e.g., 0.05).
3. Click "Run Anomaly Detection".
4. Download the resulting CSV with anomaly labels.

## File Structure

- [`app.py`](app.py): Main Flask application
- [`model.py`](model.py): Isolation Forest model logic
- [`templates/index.html`](templates/index.html): Web UI
- [`static/style.css`](static/style.css): Stylesheet
- [`requirements.txt`](requirements.txt): Python dependencies

## License

MIT License

---

*Made with Flask & scikit-learn*