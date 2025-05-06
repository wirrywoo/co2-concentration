from flask import Flask, render_template, request, send_file, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualization')
def visualization():
    # Get parameters from the query string
    year = request.args.get('year', type=int)
    month = request.args.get('month', type=int)
    day = request.args.get('day', type=int)

    if not (year and month and day):
        return abort(400, description="Missing year, month, or day parameter.")
    
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 16]

    # Build the path to the .png image
    # image_path = f'static/images/{year:04d}/{month:02d}/{day:02d}.png'
    image_path = f'static/images/{year:04d}/{sum(days[: month- 1]) + day}.png'

    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/png')
    else:
        return abort(404, description="Image not found.")

if __name__ == "__main__":
    app.run(debug=True)
