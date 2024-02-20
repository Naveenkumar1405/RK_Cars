from flask import render_template, Flask, request
import pywhatkit, datetime

app = Flask(__name__)

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
def send_whatsapp_message():
    name = request.form['Name']
    email = request.form['Email']
    phone = request.form['phone']
    message = request.form['message']

    send_whatsapp_message(name, email, message, phone)
    return 'successfull!'

def send_whatsapp_message(name, phone, email, message):
    try:
        now = datetime.datetime.now()
        pywhatkit.sendwhatmsg("+919080517421", f"Name: {name}, Phone:{phone}, Email: {email}, Message: {message}", now.hour, now.minute + 1)
    except Exception as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80 ,debug=True)