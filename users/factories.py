import factory
from factory.django import DjangoModelFactory
import datetime
from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)
