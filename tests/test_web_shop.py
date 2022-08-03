# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite

from trytond.modules.company.tests import CompanyTestMixin


class WebShopTestCase(CompanyTestMixin, ModuleTestCase):
    'Test Web Shop module'
    module = 'web_shop'
    extras = ['product_attribute', 'product_image']


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            WebShopTestCase))
    return suite