from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template('index.html')


@app.route("/services")
def Services():
    return render_template('services.html')


@app.route("/about")
def About():
    return render_template('about.html')


@app.route("/contact")
def Contact():
    return render_template('contact.html')


@app.route("/blog")
def Blog():
    return "Blog..."


@app.route("/service-pm")
def ServicesPm():
    return render_template('service-pm.html')


@app.route("/service-tech")
def ServicesTech():
    return render_template('service-tech.html')


@app.route("/service-network")
def ServicesNetwork():
    return render_template('service-network.html')


@app.route("/service-cyber")
def ServicesCyber():
    return render_template('service-cyber.html')


@app.route("/service-bcdr")
def ServicesBcdr():
    return render_template('service-bcdr.html')
