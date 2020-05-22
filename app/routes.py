from app import app
from flask import render_template, redirect
from app.forms import MacroForm

@app.route('/')
@app.route('/index')
def index():
  form = MacroForm()
  if form.validate_on_submit():
    flash("Submit successful")
  return render_template('index.html', form=form)

@app.route('/gmf_website')
def gmf_website():
  return redirect("https:///www.garrettmillerfitness.com")

@app.route('/forge_website')
def forge_website():
  return redirect("https://forgesupps.com/?utm_source=Gbaby&utm_campaign=affiliate")


