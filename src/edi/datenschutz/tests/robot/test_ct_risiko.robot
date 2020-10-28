# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_risiko.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_risiko.robot
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

Scenario: As a site administrator I can add a Risiko
  Given a logged-in site administrator
    and an add Risikomanagement form
   When I type 'My Risiko' into the title field
    and I submit the form
   Then a Risiko with the title 'My Risiko' has been created

Scenario: As a site administrator I can view a Risiko
  Given a logged-in site administrator
    and a Risiko 'My Risiko'
   When I go to the Risiko view
   Then I can see the Risiko title 'My Risiko'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Risikomanagement form
  Go To  ${PLONE_URL}/++add++Risikomanagement

a Risiko 'My Risiko'
  Create content  type=Risikomanagement  id=my-risiko  title=My Risiko

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Risiko view
  Go To  ${PLONE_URL}/my-risiko
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Risiko with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Risiko title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
