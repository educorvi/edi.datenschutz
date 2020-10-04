# -*- coding: utf-8 -*-
from edi.datenschutz.content.zielerfuellungsmanagement import IZielerfuellungsmanagement  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ZielerfuellungsmanagementIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Verarbeitungstaetigkeit',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_zielerfuellungsmanagement_schema(self):
        fti = queryUtility(IDexterityFTI, name='Zielerfuellungsmanagement')
        schema = fti.lookupSchema()
        self.assertEqual(IZielerfuellungsmanagement, schema)

    def test_ct_zielerfuellungsmanagement_fti(self):
        fti = queryUtility(IDexterityFTI, name='Zielerfuellungsmanagement')
        self.assertTrue(fti)

    def test_ct_zielerfuellungsmanagement_factory(self):
        fti = queryUtility(IDexterityFTI, name='Zielerfuellungsmanagement')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IZielerfuellungsmanagement.providedBy(obj),
            u'IZielerfuellungsmanagement not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_zielerfuellungsmanagement_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Zielerfuellungsmanagement',
            id='zielerfuellungsmanagement',
        )

        self.assertTrue(
            IZielerfuellungsmanagement.providedBy(obj),
            u'IZielerfuellungsmanagement not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('zielerfuellungsmanagement', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('zielerfuellungsmanagement', parent.objectIds())

    def test_ct_zielerfuellungsmanagement_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Zielerfuellungsmanagement')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
