from flask import Flask, render_template, request
from colormap import name2rgb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    color_name = None
    rgb_result = None
    
    if request.method == 'POST':
        color_name = request.form['color_name'].lower()
        try:
            rgb_result = name2rgb(color_name)
        except:
            rgb_result = "Invalid color name"
    
    return render_template('index.html', color_name=color_name, rgb_result=rgb_result)

if __name__ == '__main__':
    app.run(debug=True)
