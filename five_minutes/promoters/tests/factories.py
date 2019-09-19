import factory


from promoters.models import Promoter, PromoterSpace


class PromoterFactory(factory.DjangoModelFactory):

    class Meta:
        model = Promoter

    name = factory.Sequence(lambda n: "Promoter %03d" % n)


class PromoterSpaceFactory(factory.DjangoModelFactory):

    class Meta:
        model = PromoterSpace

    name = factory.Sequence(lambda n: "Promoter Space %03d" % n)
    promoter = factory.SubFactory(PromoterFactory)
