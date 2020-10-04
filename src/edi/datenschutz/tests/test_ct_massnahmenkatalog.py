# -*- coding: utf-8 -*-
from edi.datenschutz.content.massnahmenkatalog import IMassnahmenkatalog  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MassnahmenkatalogIntegrationTest(unittest.TestCase):

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

    def test_ct_massnahmenkatalog_schema(self):
        fti = queryUtility(IDexterityFTI, name='Massnahmenkatalog')
        schema = fti.lookupSchema()
        self.assertEqual(IMassnahmenkatalog, schema)

    def test_ct_massnahmenkatalog_fti(self):
        fti = queryUtility(IDexterityFTI, name='Massnahmenkatalog')
        self.assertTrue(fti)

    def test_ct_massnahmenkatalog_factory(self):
        fti = queryUtility(IDexterityFTI, name='Massnahmenkatalog')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMassnahmenkatalog.providedBy(obj),
            u'IMassnahmenkatalog not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_massnahmenkatalog_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Massnahmenkatalog',
            id='massnahmenkatalog',
        )

        self.assertTrue(
            IMassnahmenkatalog.providedBy(obj),
            u'IMassnahmenkatalog not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('massnahmenkatalog', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('massnahmenkatalog', parent.objectIds())

    def test_ct_massnahmenkatalog_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Massnahmenkatalog')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_massnahmenkatalog_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Massnahmenkatalog')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'massnahmenkatalog_id',
            title='Massnahmenkatalog container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
