import smtplib, os, json
from email.message import EmailMessage
import logging


logging.basicConfig(level=logging.INFO)


def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("YANDEX_ADDRESS")
        sender_password = os.environ.get("YANDEX_PASSWORD")
        receiver_address = message["username"]

        msg = EmailMessage()
        msg.set_content(f"mp3 file_id: {mp3_fid} is not ready!")
        msg["Subject"] = "MP3 Download"
        msg["From"] = sender_address
        msg["To"] = receiver_address

        with smtplib.SMTP("smtp.yandex.ru") as session:
            session.starttls()
            session.login(sender_address, sender_password)
            session.send_message(msg, sender_address, receiver_address)
            logging.info("Mail Sent")

    except Exception as err:
        logging.error(err)
        return err
