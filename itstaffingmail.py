from flask import Flask, request, jsonify
import mailtrap as mt
import os

app = Flask(__name__)

@app.route('/send_it_staffing_email', methods=['POST'])
def send_it_staffing_email():
    try:
        # Get form data from the request
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        company_name = request.form['company_name']
        job_title = request.form['job_title']
        hire_type = request.form['type_of_hire']
        openings = request.form['number_of_openings']
        location = request.form['job_location']
        job_description = request.form['job_description']

        # Prepare Mailtrap email with dynamic recipient email and name
        mail = mt.MailFromTemplate(
            sender=mt.Address(email="itstaffing@fourtechnologies.in", name="Four Technologies"),
            to=[mt.Address(email=email)],
            template_uuid="97f56f88-c032-4882-9d66-623ca888b2f0",
            template_variables={
                "company_info_name": company_name,
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "job_title": job_title,
                "hire_type": hire_type,
                "openings": openings,
                "location": location,
                "job_description": job_description,
                "message": "Thank you for reaching out to us regarding our IT staffing services. Sit back, relax, and allow us to handle the details. We will get back to you soon with your IT staffing proposal."
            }
        )

        # Initialize Mailtrap client and send email
        client = mt.MailtrapClient(token="YOUR_MAILTRAP_API_TOKEN")
        response = client.send(mail)

        return jsonify({"status": "success", "message": "Email sent successfully."}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Ensure app listens on the correct host and port for Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
