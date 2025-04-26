from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # nécessaire pour les messages flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping_server():
    server_ip = request.form['server_ip']
    try:
        output = subprocess.check_output(["ping", "-c", "1", server_ip], stderr=subprocess.STDOUT)
        flash(f"Success! Server {server_ip} is reachable.", "success")
    except subprocess.CalledProcessError:
        flash(f"Error! Server {server_ip} is unreachable.", "danger")
    return redirect(url_for('index'))

@app.route('/deploy', methods=['POST'])
def deploy():
    try:
        # Suppose que deploy.sh est un script de déploiement
        output = subprocess.check_output(["bash", "scripts/deploy.sh"], stderr=subprocess.STDOUT)
        flash("Deployment script executed successfully!", "success")
    except subprocess.CalledProcessError as e:
        flash(f"Deployment failed: {e.output.decode()}", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
