from flask import Flask, request, jsonify
import mailtrap as mt
import os

app = Flask(__name__)

@app.route('/send_it_staffing_email', methods=['POST'])
def send_email():
    try:
        # Get form data from the request
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        service = request.form['services']

        # Prepare Mailtrap email
        mail = mt.MailFromTemplate(
            sender=mt.Address(email="itstaffing@fourtechnologies.in", name="Four Technologies"),
            to=[mt.Address(email=email)],  # Send to the user's email
            template_uuid="97f56f88-c032-4882-9d66-623ca888b2f0",  # Your template UUID for IT Staffing
            template_variables={
                "company_info_name": "Four Technologies",  # Dynamic data
                "name": name,
                "phone": phone,
                "services": service,
                "message": "Thank you for reaching out to us regarding our IT staffing services. Sit back, relax, and allow us to handle the details. We will get back to you soon with your IT staffing proposal.",
            }
        )

        # Initialize Mailtrap client and send email
        client = mt.MailtrapClient(token="********0d9e")  # Replace with your actual Mailtrap API token
        response = client.send(mail)

        return jsonify({"status": "success", "message": "Email sent successfully."}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Ensure app listens on the correct host and port for Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's provided port or fallback to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
