# -*- coding: utf-8 -*-
from edi.datenschutz.content.vorlage_d_s_f_a import IVorlageDSFA  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class VorlageDSFAIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_vorlage_d_s_f_a_schema(self):
        fti = queryUtility(IDexterityFTI, name='Vorlage DSFA')
        schema = fti.lookupSchema()
        self.assertEqual(IVorlageDSFA, schema)

    def test_ct_vorlage_d_s_f_a_fti(self):
        fti = queryUtility(IDexterityFTI, name='Vorlage DSFA')
        self.assertTrue(fti)

    def test_ct_vorlage_d_s_f_a_factory(self):
        fti = queryUtility(IDexterityFTI, name='Vorlage DSFA')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IVorlageDSFA.providedBy(obj),
            u'IVorlageDSFA not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_vorlage_d_s_f_a_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Vorlage DSFA',
            id='vorlage_d_s_f_a',
        )

        self.assertTrue(
            IVorlageDSFA.providedBy(obj),
            u'IVorlageDSFA not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('vorlage_d_s_f_a', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('vorlage_d_s_f_a', parent.objectIds())

    def test_ct_vorlage_d_s_f_a_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Vorlage DSFA')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
