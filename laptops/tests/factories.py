import factory
from factory.django import DjangoModelFactory

from laptops.models import Laptop, Vendor


class VendorFactory(DjangoModelFactory):
    class Meta:
        model = Vendor

    name = "Default"


class LaptopFactory(DjangoModelFactory):
    class Meta:
        model = Laptop

    vendor = factory.SubFactory(VendorFactory)