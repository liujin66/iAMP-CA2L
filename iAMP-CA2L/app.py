from flask import Flask
from flask import render_template, request, send_from_directory
import predict
import os
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(1)
app = Flask(__name__)

@app.route("/download_all")
def download_all():
    return send_from_directory("static/download", filename="data.zip",
                               as_attachment=True)

@app.route('/upload_seq', methods=['POST'])
def upload_seq():
    file_path = 'static/upload/new_test.fasta'
    Seq_cadd = ">1\n"
    Seq_cadd = Seq_cadd + request.form.get('Seq_cadd')
    with open(file_path, 'w+') as f:
        f.writelines(Seq_cadd)
    try:
        result = predict.predict()
        data = {
            'data': result
        }
        return render_template('back.html', **data)
    except Exception as e:
        print(e)
        return render_template("exception.html")



@app.route('/', methods=['POST', 'GET'])
def Pse_home():
    return render_template('iAMP_home.html')


@app.route('/Pse_example', methods=['POST', 'GET'])
def Pse_example():
    return render_template('iAMP_example.html')


@app.route('/Pse_help', methods=['POST', 'GET'])
def Pse_help():
    return render_template('iAMP_help.html')


@app.route('/Pse_backhome', methods=['POST', 'GET'])
def Pse_backhome():
    return render_template('iAMP_backhome.html')

@app.errorhandler(404)
def Pse_page_not_found(e):
    return render_template('iAMP_404.html')

@app.route("/download")
def Pse_download():
    return render_template('iAMP_download.html')

if __name__ == "__main__":
    app.run(debug=True)
