# -*- coding: utf-8 -*-
from edi.datenschutz.content.gefaehrdung import IGefaehrdung  # NOQA E501
from edi.datenschutz.testing import EDI_DATENSCHUTZ_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class GefaehrdungIntegrationTest(unittest.TestCase):

    layer = EDI_DATENSCHUTZ_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Zielerfuellungsmanagement',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_gefaehrdung_schema(self):
        fti = queryUtility(IDexterityFTI, name='Gefaehrdung')
        schema = fti.lookupSchema()
        self.assertEqual(IGefaehrdung, schema)

    def test_ct_gefaehrdung_fti(self):
        fti = queryUtility(IDexterityFTI, name='Gefaehrdung')
        self.assertTrue(fti)

    def test_ct_gefaehrdung_factory(self):
        fti = queryUtility(IDexterityFTI, name='Gefaehrdung')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IGefaehrdung.providedBy(obj),
            u'IGefaehrdung not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_gefaehrdung_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Gefaehrdung',
            id='gefaehrdung',
        )

        self.assertTrue(
            IGefaehrdung.providedBy(obj),
            u'IGefaehrdung not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('gefaehrdung', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('gefaehrdung', parent.objectIds())

    def test_ct_gefaehrdung_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Gefaehrdung')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
