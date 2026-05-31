from flask import Flask, render_template, jsonify
import os
from main import generate_headline, get_ai_analysis

app = Flask(__name__)

@app.route('/')
def index():
    headline = generate_headline()
    analysis = get_ai_analysis(headline)
    return render_template('index.html', headline=headline, analysis=analysis)

@app.route('/generate')
def generate():
    headline = generate_headline()
    analysis = get_ai_analysis(headline)
    return jsonify({'headline': headline, 'analysis': analysis})

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)