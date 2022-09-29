import os
from pathlib import Path
from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
  
app = Flask(__name__)
  
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/c3-bar-chart')
def c3_bar():
    return render_template('c3_bar_chart.html')

@app.route('/d3-bar-chart')
def d3_bar():
    return render_template('d3_BarChart.html')

@app.route('/d3-circle-packing')
def d3_cpack():
    return render_template('d3_circlePacking.html')

@app.route('/d3-network-diagram')
def d3_network():
    return render_template('d3_NetworkDiagram.html')

@app.route('/d3-funnel')
def d3_funnel():
    return render_template('d3_funnel_chart.html')

@app.route('/d3-radial')
def d3_radial():
    return render_template('d3_radialStackedBar.html')

@app.route('/d3-spiral-heatmap')
def d3_spiral_heatmap():
    return render_template('d3_spiralHeatmap.html')

@app.route('/d3-spiral-plot')
def d3_spiral_plot():
    return render_template('d3_spiralPlot.html')

@app.route('/data-update')
def data_update():
    return render_template('dataUpdate.html')

@app.route('/export-to-csv')
def export_to_csv():
    return render_template('export2CSV.html')

@app.route('/google-bar-chart')
def google_bar_chart():
    return render_template('google_BarChart.html')

@app.route('/google-calendar')
def google_calendar():
    return render_template('google_Calendar.html')

@app.route('/google-org-chart')
def google_org_chart():
    return render_template('google_OrgChart.html')

@app.route('/json-data-viewer')
def json_data_viewer():
    return render_template('jsonDataViewer.html')

@app.route('/multi-selector')
def multi_selector():
    return render_template('multiSelector.html')

@app.route('/hold-horses')
def hold_horses():
    return render_template('coming-soon.html')

@app.route('/full-list')
def full_list():
    return render_template('full-list.html')

@app.route('/newrule', methods=['POST'])
def newrulecreator():
    print("entered post")
    f = request.files['upload']
    sf=Path(secure_filename(f.filename)).stem
    print(sf)
    f.save(os.path.join(os.getcwd(),"templates",sf))
    return render_template("upload-confirmation.html",sf=sf)

@app.route('/userddc/<sf>')
def user_ddc(sf):
    if os.path.exists(os.path.join(os.getcwd(),"templates",sf)):
        return render_template(sf)
    else:
        return render_template("upload-confirmation.html","No such file")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,ssl_context='adhoc',debug=False)


