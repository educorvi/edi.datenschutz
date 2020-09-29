# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_verarbeitungstaetigkeit.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_verarbeitungstaetigkeit.robot
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

Scenario: As a site administrator I can add a Verarbeitungstaetigkeit
  Given a logged-in site administrator
    and an add Verarbeitungstaetigkeit form
   When I type 'My Verarbeitungstaetigkeit' into the title field
    and I submit the form
   Then a Verarbeitungstaetigkeit with the title 'My Verarbeitungstaetigkeit' has been created

Scenario: As a site administrator I can view a Verarbeitungstaetigkeit
  Given a logged-in site administrator
    and a Verarbeitungstaetigkeit 'My Verarbeitungstaetigkeit'
   When I go to the Verarbeitungstaetigkeit view
   Then I can see the Verarbeitungstaetigkeit title 'My Verarbeitungstaetigkeit'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Verarbeitungstaetigkeit form
  Go To  ${PLONE_URL}/++add++Verarbeitungstaetigkeit

a Verarbeitungstaetigkeit 'My Verarbeitungstaetigkeit'
  Create content  type=Verarbeitungstaetigkeit  id=my-verarbeitungstaetigkeit  title=My Verarbeitungstaetigkeit

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Verarbeitungstaetigkeit view
  Go To  ${PLONE_URL}/my-verarbeitungstaetigkeit
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Verarbeitungstaetigkeit with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Verarbeitungstaetigkeit title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
