# -*- coding: utf-8 -*-
from edi.datenschutz.content.vorlage_verarbeitung import IVorlageVerarbeitung  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class VorlageVerarbeitungIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_vorlage_verarbeitung_schema(self):
        fti = queryUtility(IDexterityFTI, name='Vorlage Verarbeitung')
        schema = fti.lookupSchema()
        self.assertEqual(IVorlageVerarbeitung, schema)

    def test_ct_vorlage_verarbeitung_fti(self):
        fti = queryUtility(IDexterityFTI, name='Vorlage Verarbeitung')
        self.assertTrue(fti)

    def test_ct_vorlage_verarbeitung_factory(self):
        fti = queryUtility(IDexterityFTI, name='Vorlage Verarbeitung')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IVorlageVerarbeitung.providedBy(obj),
            u'IVorlageVerarbeitung not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_vorlage_verarbeitung_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Vorlage Verarbeitung',
            id='vorlage_verarbeitung',
        )

        self.assertTrue(
            IVorlageVerarbeitung.providedBy(obj),
            u'IVorlageVerarbeitung not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('vorlage_verarbeitung', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('vorlage_verarbeitung', parent.objectIds())

    def test_ct_vorlage_verarbeitung_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Vorlage Verarbeitung')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
