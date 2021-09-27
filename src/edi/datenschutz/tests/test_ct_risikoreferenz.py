# -*- coding: utf-8 -*-
from edi.datenschutz.content.risikoreferenz import IRisikoreferenz  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class RisikoreferenzIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Risikomanagement',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_risikoreferenz_schema(self):
        fti = queryUtility(IDexterityFTI, name='Risikoreferenz')
        schema = fti.lookupSchema()
        self.assertEqual(IRisikoreferenz, schema)

    def test_ct_risikoreferenz_fti(self):
        fti = queryUtility(IDexterityFTI, name='Risikoreferenz')
        self.assertTrue(fti)

    def test_ct_risikoreferenz_factory(self):
        fti = queryUtility(IDexterityFTI, name='Risikoreferenz')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IRisikoreferenz.providedBy(obj),
            u'IRisikoreferenz not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_risikoreferenz_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Risikoreferenz',
            id='risikoreferenz',
        )

        self.assertTrue(
            IRisikoreferenz.providedBy(obj),
            u'IRisikoreferenz not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('risikoreferenz', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('risikoreferenz', parent.objectIds())

    def test_ct_risikoreferenz_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Risikoreferenz')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
