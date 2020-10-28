# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_gefaehrdung.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_gefaehrdung.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Gefaehrdung
  Given a logged-in site administrator
    and an add Zielerfuellungsmanagement form
   When I type 'My Gefaehrdung' into the title field
    and I submit the form
   Then a Gefaehrdung with the title 'My Gefaehrdung' has been created

Scenario: As a site administrator I can view a Gefaehrdung
  Given a logged-in site administrator
    and a Gefaehrdung 'My Gefaehrdung'
   When I go to the Gefaehrdung view
   Then I can see the Gefaehrdung title 'My Gefaehrdung'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Zielerfuellungsmanagement form
  Go To  ${PLONE_URL}/++add++Zielerfuellungsmanagement

a Gefaehrdung 'My Gefaehrdung'
  Create content  type=Zielerfuellungsmanagement  id=my-gefaehrdung  title=My Gefaehrdung

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Gefaehrdung view
  Go To  ${PLONE_URL}/my-gefaehrdung
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Gefaehrdung with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Gefaehrdung title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
