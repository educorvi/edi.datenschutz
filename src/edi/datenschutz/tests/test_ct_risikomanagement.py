# -*- coding: utf-8 -*-
from edi.datenschutz.content.risikomanagement import IRisikomanagement  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class RisikomanagementIntegrationTest(unittest.TestCase):

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

    def test_ct_risikomanagement_schema(self):
        fti = queryUtility(IDexterityFTI, name='Risikomanagement')
        schema = fti.lookupSchema()
        self.assertEqual(IRisikomanagement, schema)

    def test_ct_risikomanagement_fti(self):
        fti = queryUtility(IDexterityFTI, name='Risikomanagement')
        self.assertTrue(fti)

    def test_ct_risikomanagement_factory(self):
        fti = queryUtility(IDexterityFTI, name='Risikomanagement')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IRisikomanagement.providedBy(obj),
            u'IRisikomanagement not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_risikomanagement_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Risikomanagement',
            id='risikomanagement',
        )

        self.assertTrue(
            IRisikomanagement.providedBy(obj),
            u'IRisikomanagement not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('risikomanagement', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('risikomanagement', parent.objectIds())

    def test_ct_risikomanagement_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Risikomanagement')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
