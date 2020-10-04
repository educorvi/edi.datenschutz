# -*- coding: utf-8 -*-
from edi.datenschutz.content.kontrolle import IKontrolle  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class KontrolleIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Massnahme',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_kontrolle_schema(self):
        fti = queryUtility(IDexterityFTI, name='Kontrolle')
        schema = fti.lookupSchema()
        self.assertEqual(IKontrolle, schema)

    def test_ct_kontrolle_fti(self):
        fti = queryUtility(IDexterityFTI, name='Kontrolle')
        self.assertTrue(fti)

    def test_ct_kontrolle_factory(self):
        fti = queryUtility(IDexterityFTI, name='Kontrolle')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IKontrolle.providedBy(obj),
            u'IKontrolle not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_kontrolle_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Kontrolle',
            id='kontrolle',
        )

        self.assertTrue(
            IKontrolle.providedBy(obj),
            u'IKontrolle not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('kontrolle', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('kontrolle', parent.objectIds())

    def test_ct_kontrolle_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Kontrolle')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
