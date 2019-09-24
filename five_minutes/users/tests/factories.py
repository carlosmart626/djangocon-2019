import datetime
import factory

from users.models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: 'john%s' % n)
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda o: '%s.%s@example.org' % (o.first_name, o.last_name))
    date_joined = factory.LazyFunction(datetime.datetime.now)
