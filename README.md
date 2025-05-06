# Column-Averaged CO₂ Concentration Interactive Visualization

## 🌍 Overview

The **CO₂ Concentration** project provides an interactive web application that visualizes global atmospheric CO₂ concentrations over time. Built using Python and Flask, the app processes atmospheric CO₂ data from raster files, generates PNG visualizations, and serves them through a user-friendly interface.

![CO₂ Concentration Visualization](https://github.com/wirrywoo/co2-concentration/blob/main/static/combined.gif?raw=true)

## 🚀 Features

- **Interactive Map**: View global CO₂ concentrations with intuitive navigation.
- **Time Series Animation**: Explore how CO₂ levels have changed over time.
- **Data Processing**: Efficiently handles large datasets using multiprocessing.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/wirrywoo/co2-concentration.git
cd co2-concentration
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```
**Note:** Ensure your AWS credentials have the necessary permissions to access the required S3 buckets.

### 5. Run the Application
```
python app.py
```
The application will be accessible at `http://127.0.0.1:5000/`.

## 🧪 Data Processing

The application processes TIFF files containing atmospheric CO₂ concentration data:

- **Data Download**: Retrieves raw data from an S3 bucket.
- **Data Processing**: Converts TIFF data to masked arrays.
- **Visualization**: Generates PNG images representing CO₂ concentrations.
- **Optimization**: Utilizes multiprocessing to accelerate image generation.

## 📁 Project Structure

```
co2-concentration/
├── app.py # Flask application entry point
├── requirements.txt # Python dependencies
├── .env # Environment variables
├── scripts/ # Data processing scripts
├── static/ # Static files (images, CSS, JS)
├── templates/ # HTML templates
└── README.md # Project documentation
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or contributions, please open an issue or submit a pull request.


