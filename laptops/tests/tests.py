from django.test import TestCase

from laptops.tests.factories import LaptopFactory, VendorFactory


class VendorTest(TestCase):

    def test_create_vendor_with_factory(self):

        # laptop1 = LaptopFactory()
        # print("*******", laptop1.vendor.name)
        #
        # laptop2 = LaptopFactory()
        # print("*******", laptop2.vendor)
        #
        # print(id(laptop1.vendor), id(laptop2.vendor))
        #
        # assert laptop1.vendor == laptop2.vendor

        vendor_1 = VendorFactory(name="Apple")

        laptop1 = LaptopFactory(vendor=vendor_1)
        print("*******", laptop1.vendor.name)

        laptop2 = LaptopFactory(vendor=vendor_1)

        print(id(laptop1.vendor), id(laptop2.vendor))
