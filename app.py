from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

"""
@app.route('/projects')
def projects():
    data_projects = [
        {"name": "COVID-19 Dashboard", "tools": "Plotly, Pandas"},
        {"name": "Churn Prediction", "tools": "Scikit-learn"},
        {"name": "Image Classifier", "tools": "TensorFlow, Keras"},
    ]
    return render_template("projects.html", projects=data_projects)
"""
if __name__ == "__main__":
    app.run(debug=True)