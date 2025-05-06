# Column-Averaged CO₂ Concentration Interactive Visualization

## 🌍 Overview

The **Column-Averaged CO₂ Concentration** project is a time-series web application that animates the progression of global atmospheric CO₂ levels. Built with Python and Flask, it processes geospatial raster data from the NASA/GSFC/GMAO Carbon Group using `GDAL`. The application generates high-resolution PNG frames and presents them through a web interface equipped with an interactive slider for seamless temporal navigation.

![CO₂ Concentration Visualization](https://github.com/wirrywoo/co2-concentration/blob/main/static/combined.gif?raw=true)

## 🚀 Features

- **Animated Global CO₂ Maps**: Visualize changes in column-averaged CO₂ over time.
- **Interactive Slider**: Navigate across dates to observe variations in CO₂ concentration.
- **High-Resolution Visualization**: Generates publication-quality PNG frames using `matplotlib` and `Basemap`.
- **S3 Integration**: Downloads raw satellite data directly from a public AWS S3 bucket.

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

- **Data Download**: Retrieves raw data from an S3 bucket using `awscli`.
- **Data Processing**: Converts TIFF data to masked arrays using `GDAL`.
- **Visualization**: Generates PNG images representing CO₂ concentrations using `Basemap`.

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


