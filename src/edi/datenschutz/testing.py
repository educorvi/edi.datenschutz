# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.datenschutz


class EdiDatenschutzLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.datenschutz)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.datenschutz:default')


EDI_DATENSCHUTZ_FIXTURE = EdiDatenschutzLayer()


EDI_DATENSCHUTZ_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_DATENSCHUTZ_FIXTURE,),
    name='EdiDatenschutzLayer:IntegrationTesting',
)


EDI_DATENSCHUTZ_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_DATENSCHUTZ_FIXTURE,),
    name='EdiDatenschutzLayer:FunctionalTesting',
)


EDI_DATENSCHUTZ_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_DATENSCHUTZ_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiDatenschutzLayer:AcceptanceTesting',
)
