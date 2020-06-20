from app import app
from flask import render_template, redirect, url_for, session
from app.forms import MacroForm, ReSubmit
from app.calcs import calculate 


  

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = MacroForm()
  if form.validate_on_submit():
    results = calculate(form)
    session['results'] = results
    return redirect(url_for('calculations'))
  return render_template('calcs.html', form=form)

@app.route('/results', methods=['GET', 'POST'])
def calculations():
  startForm = MacroForm()
  results = session.get('results', None)
    
  return render_template("results.html", results=results)
  

@app.route('/gmf_website')
def gmf_website():
  return redirect("https:///www.garrettmillerfitness.com")

@app.route('/forge_website')
def forge_website():
  return redirect("https://forgesupps.com/?utm_source=Gbaby&utm_campaign=affiliate")


