from pathlib import Path
from app.config import settings
from app.tasks.celery_app import celery
import smtplib
from app.tasks.email_templates import create_booking_confirmation_template
from pydantic import EmailStr


@celery.task
def send_booking_confirmation_email(
    booking: dict,
    email_to: EmailStr
):
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
