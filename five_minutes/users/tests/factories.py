import datetime
import factory

from users.models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda n: 'john%s@example.org' % n)
    date_joined = factory.LazyFunction(datetime.datetime.now)
