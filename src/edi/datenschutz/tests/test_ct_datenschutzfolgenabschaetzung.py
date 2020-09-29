# -*- coding: utf-8 -*-
from edi.datenschutz.content.datenschutzfolgenabschaetzung import IDatenschutzfolgenabschaetzung  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class DatenschutzfolgenabschaetzungIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_datenschutzfolgenabschaetzung_schema(self):
        fti = queryUtility(IDexterityFTI, name='Datenschutzfolgenabschaetzung')
        schema = fti.lookupSchema()
        self.assertEqual(IDatenschutzfolgenabschaetzung, schema)

    def test_ct_datenschutzfolgenabschaetzung_fti(self):
        fti = queryUtility(IDexterityFTI, name='Datenschutzfolgenabschaetzung')
        self.assertTrue(fti)

    def test_ct_datenschutzfolgenabschaetzung_factory(self):
        fti = queryUtility(IDexterityFTI, name='Datenschutzfolgenabschaetzung')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDatenschutzfolgenabschaetzung.providedBy(obj),
            u'IDatenschutzfolgenabschaetzung not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_datenschutzfolgenabschaetzung_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Datenschutzfolgenabschaetzung',
            id='datenschutzfolgenabschaetzung',
        )

        self.assertTrue(
            IDatenschutzfolgenabschaetzung.providedBy(obj),
            u'IDatenschutzfolgenabschaetzung not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('datenschutzfolgenabschaetzung', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('datenschutzfolgenabschaetzung', parent.objectIds())

    def test_ct_datenschutzfolgenabschaetzung_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Datenschutzfolgenabschaetzung')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_datenschutzfolgenabschaetzung_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Datenschutzfolgenabschaetzung')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'datenschutzfolgenabschaetzung_id',
            title='Datenschutzfolgenabschaetzung container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
