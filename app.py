from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'navin.onwords@gmail.com'
app.config['MAIL_PASSWORD'] = 'oizg ntdk nzsi csgo'
mail = Mail(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/cars")
def cars():
    return render_template('all-cars.html')

@app.route('/send', methods=['POST'])
def send_message():
    name = request.form['Name']
    email = request.form['Email']
    message = request.form['message']
    phone = request.form['phone']

    if name and email and message:
        try:
            msg = Message('New Message From Website', sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])
            msg.body = f'Name: {name}\nPhone:{phone}\nEmail: {email}\nMessage: {message}'
            mail.send(msg)

            return jsonify({'success': True})
        except Exception as e:
            print(e)
            return jsonify({'success': False}), 500
    else:
        return jsonify({'success': False}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80 ,debug=True)