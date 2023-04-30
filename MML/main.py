from website import create_app
from flask import render_template, request, redirect

app = create_app()

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(f'uploads/{file.filename}')
    return redirect('/')
