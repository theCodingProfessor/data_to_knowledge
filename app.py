"""
Info to Knowledge; Demonstration Web App
Python, Flask, MatPlotLib, Numpy, more
Clinton Garwood
License: MIT
September 2024
"""

from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def app_index():  # put application's code here
    return render_template("index.html")


@app.route('/success', methods=['GET'])
def get_success():
    return render_template('success.html')


@app.route('/form')
def web_form():
    return render_template('web_form.html')


@app.route('/results', methods=['GET'])
def results():
    return render_template('results.html')


@app.route('/results', methods=['POST'])
def post_success():
    # data = dict()
    starting = request.form['start_at']
    ending = request.form['end_at']

    # Generate a simple plot with the input range
    x = list(range(int(starting), int(ending) + 1))
    y = [i**2 for i in x]  # Example plot: y = x^2

    do_scatter(x, y)

    # Line Plot and save image
    plt.figure()
    plt.plot(x, y)
    plt.title(f'Plot for range x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img', 'plot.png')
    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    # Bar Plot
    plt.bar(x, y)
    plt.title('Bar Plot: y = x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img/', 'bar_plot.png')
    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    # Step Plot
    plt.step(x, y, where='mid')
    plt.title('Step Plot: y = x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img/', 'step_plot.png')
    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    return render_template('web_form.html')


def do_scatter(x, y):
    # Scatter Plot
    plt.scatter(x, y)
    plt.title('Scatter Plot: y = x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img/', 'scatter_plot.png')
    # Save image to the static/images directory
    print(f'{image_path}')
    plt.savefig(image_path)
    plt.close()
    return


if __name__ == '__main__':
    app.run()
