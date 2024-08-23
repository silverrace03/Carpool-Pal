import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from dotenv import main
# main.load_dotenv()

SENDER_EMAIL = os.getenv('CARPOOL_EMAIL')
MAIL_PASS = os.getenv('CARPOOL_PASSWORD')

def send_email(receiver_email, driver_name, departure_date, pickup_time, car_id, pickup_point, dropoff_point, no_of_passengers):
    subject = "Your Carpool Ride is Confirmed!"
    body = """  
Dear Customer,
    
This email confirms your carpool ride with {driver_name} on {date} at {pickup_time}. 
Here are the details:

• Car ID: {car_id}
• Driver: {driver_name}
• Pick-up Location: {pickup_point}
• Drop-off Location: {dropoff_point}
• Number of Passengers: {no_of_passengers}

Please be sure to:
• Be at the pick-up location at least 5 minutes before the scheduled time.
• Inform {driver_name} if you are running late.
• You can share the ride cost with {driver_name} using GPay, UPI or  Cash. The fare will be pre-determined by the carpooling platform.
• To ensure a smooth ride, please be respectful of other passengers and the driver.

We hope you have a safe and enjoyable carpool ride!

Thanks,
The Carpool Team
    """.format(
            driver_name=driver_name,
            date=departure_date,
            pickup_time=pickup_time, 
            car_id=car_id,
            pickup_point=pickup_point,
            dropoff_point=dropoff_point,
            no_of_passengers=no_of_passengers,
    )

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, MAIL_PASS)
    text = msg.as_string()
    server.sendmail(SENDER_EMAIL, receiver_email, text)
    server.quit()