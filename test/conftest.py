import pytest

from framework.internal.http.account import AccountApi
from framework.internal.http.mail import MailApi
from framework.internal.kafka.producer import KafkaProducerWrapper


@pytest.fixture(scope="session")
def account_api() -> "AccountApi":
    return AccountApi()

@pytest.fixture(scope="session")
def mail_api() -> "MailApi":
    return MailApi()

@pytest.fixture(scope="session")
def kafka_producer() -> "KafkaProducerWrapper": # type: ignore
    with KafkaProducerWrapper() as producer:
        yield producer  