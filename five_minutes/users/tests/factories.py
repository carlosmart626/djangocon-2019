import datetime
import factory
import uuid

from users.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('ascii_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_joined = factory.LazyFunction(datetime.datetime.now)
