from django.test import SimpleTestCase  # here we use simple test model
from django.urls import reverse, resolve
from main.views import *


def main():  # check urls to the linked pages
    TestUrls.test_index()
    TestUrls.test_single_product()
    TestUrls.test_about()
    TestUrls.test_post_contacts()
    TestUrls.test_product_boxes()
    TestUrls.test_product_big_box()
    TestUrls.test_product_bouquets()


class TestUrls(SimpleTestCase):

    def test_index(self):  # catalog
        url = reverse("index")
        print(resolve(url))
        self.assertEquals(resolve(url).func, shop_index)

    def test_single_product(self):  # single product
        url = reverse("single_product")
        print(resolve(url))
        self.assertEquals(resolve(url).func, shop_single)

    def test_about(self):  # about company page
        url = reverse("about")
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_post_contacts(self):  # contacts page
        url = reverse("contact")
        print(resolve(url))
        self.assertEquals(resolve(url).func, post_contacts)

    def test_product_boxes(self):  # only boxes
        url = reverse("boxes")
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_boxes)

    def test_product_big_box(self):  # only big boxes
        url = reverse("big_box")
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_big_box)

    def test_product_bouquets(self):  # only bouquets
        url = reverse("bouquets")
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_bouquets)


if __name__ == "__main__":
    main()
