# -*- coding: utf-8 -*-
from edi.datenschutz.content.massnahme import IMassnahme  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MassnahmeIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_massnahme_schema(self):
        fti = queryUtility(IDexterityFTI, name='Massnahme')
        schema = fti.lookupSchema()
        self.assertEqual(IMassnahme, schema)

    def test_ct_massnahme_fti(self):
        fti = queryUtility(IDexterityFTI, name='Massnahme')
        self.assertTrue(fti)

    def test_ct_massnahme_factory(self):
        fti = queryUtility(IDexterityFTI, name='Massnahme')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMassnahme.providedBy(obj),
            u'IMassnahme not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_massnahme_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Massnahme',
            id='massnahme',
        )

        self.assertTrue(
            IMassnahme.providedBy(obj),
            u'IMassnahme not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('massnahme', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('massnahme', parent.objectIds())

    def test_ct_massnahme_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Massnahme')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_massnahme_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Massnahme')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'massnahme_id',
            title='Massnahme container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
