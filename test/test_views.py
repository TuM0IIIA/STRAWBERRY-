from django.test import TestCase  # here we use Test case
from main.views import *


def main():  # check urls to the linked pages
    TestDataBase.test_index()
    TestDataBase.test_render_funcs()


class TestDataBase(TestCase):

    def test_index(self):
        response = self.client.get('/')  # if the user move to the main page
        self.assertEqual(response.status_code, 200)


    def test_render_funcs(self):  # checking all the render funcs

        with self.assertTemplateUsed(template_name='index.html'):
            shop_index('index.html')
        with self.assertTemplateUsed('about.html'):
            about('about.html')
        with self.assertTemplateUsed('products.html'):
            shop_products('products.html')
        with self.assertTemplateUsed('big_box.html'):
            product_big_box('big_box.html')
        with self.assertTemplateUsed('bouquets.html'):
            product_bouquets('bouquets.html')
        with self.assertTemplateUsed('single_product.html'):
            shop_single('single_product.html')
        with self.assertTemplateUsed('boxes.html'):
            product_boxes('boxes.html')

if __name__ == "__main__":
    main()
