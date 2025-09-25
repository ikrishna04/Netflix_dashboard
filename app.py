from flask import Flask, render_template
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load your cleaned Netflix data
data_df = pd.read_csv('netflix_merged.csv')

@app.route('/')
def home():
    """Renders the main dashboard page with top directors and countries."""

    # Top 10 directors
    top_directors = data_df['director'].value_counts().head(10).to_dict()

    # Top 10 countries
    top_countries = data_df['country'].value_counts().head(10).to_dict()

    return render_template('index.html',
                           directors=top_directors,
                           countries=top_countries)

if __name__ == "__main__":
    app.run(debug=True)
