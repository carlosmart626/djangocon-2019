import factory


from promoters.models import Promoter, PromoterSpace


class PromoterFactory(factory.DjangoModelFactory):

    class Meta:
        model = Promoter

    name = factory.Sequence(lambda n: "Promoter %03d" % n)
    contact_name = factory.Faker('name')
    contact_phone = factory.Faker('phone_number')
    website = factory.Faker('uri')


class PromoterSpaceFactory(factory.DjangoModelFactory):

    class Meta:
        model = PromoterSpace

    name = factory.Sequence(lambda n: "Promoter Space %03d" % n)
    promoter = factory.SubFactory(PromoterFactory)
    capacity = factory.Iterator([100, 200, 500, 1000])
    description = factory.Faker('paragraphs', nb=3, ext_word_list=None)
