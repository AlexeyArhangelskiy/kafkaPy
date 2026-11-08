import json
import time
import uuid

from framework.internal.http.account import AccountApi
from framework.internal.http.mail import MailApi
from kafka import KafkaProducer

from framework.internal.kafka.producer import KafkaProducerWrapper


def test_failed_register_user(account_api: "AccountApi", mail_api: "MailApi") -> None:
    expected_email = "string@mail.ru"
    response = account_api.register_user(
        login="string",
        email=expected_email,
        password="string",
    )
    for _ in range(10):
        responsemail = mail_api.mail_search(query=expected_email)
        if responsemail.json()["total"] > 0:
            raise AssertionError(f"Email {expected_email} found in mail search")
        time.sleep(1)
   
def test_register_user(account_api: "AccountApi", mail_api: "MailApi") -> None:
    base = uuid.uuid4().hex
    response = account_api.register_user(
        login=base,
        email=f"{base}@mail.ru",
        password="123123123",
    )
    for _ in range(10):
        responsemail = mail_api.mail_search(query=base)
        if responsemail.json()["total"] > 0:
            break
        time.sleep(1)
    else:
        raise AssertionError(f"Email {base} not found in mail search")


def test_register_user_kafka(mail_api: "MailApi", kafka_producer: "KafkaProducerWrapper") -> None:
    base = uuid.uuid4().hex
    message = {
            "login": base,
            "email": f"{base}@mail.ru",
            "password": "123123123"
        }
    
    kafka_producer.send("register-events", message)

    for _ in range(10):
        responsemail = mail_api.mail_search(query=base)
        if responsemail.json()["total"] > 0:
            break
        time.sleep(1)
    else:
        raise AssertionError(f"Email {base} not found in mail search")