#! usr/bin/python3

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        sample_name = request.form['sample_name']
        start_temp = request.form['start_temp']
        end_temp = request.form['end_temp']
        water_mass = request.form['water_mass']
        start_wt = request.form['start_wt']
        end_wt = request.form['end_wt']

        delta_temp = float(end_temp) - float(start_temp)

        c = float(1)

        m = float(water_mass)

        Q = m * c * delta_temp

        cal = Q

        C = cal/1000

        return render_template('results.html', sample_name=sample_name, start_temp=start_temp, end_temp=end_temp,
                                water_mass=water_mass, start_wt=start_wt, end_wt=end_wt, delta_temp=delta_temp, Q=Q, C=C)

    return render_template('input.html')

@app.route('/results', methods=['GET','POST'])
def results():

    return render_template('results.html', start_temp='"no data available"', end_temp='"no data available"',
        water_mass='"no data available"', start_wt='"no data available"', end_wt='"no data available"',
        delta_temp='"no data available"', Q='"no data available"', C='"no data available"')

@app.route('/about')
def about():

    return render_template('about.html')

# @app.route('/results')
# def results():

    # return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)