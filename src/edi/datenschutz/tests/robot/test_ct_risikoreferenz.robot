# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_risikoreferenz.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_risikoreferenz.robot
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

Scenario: As a site administrator I can add a Risikoreferenz
  Given a logged-in site administrator
    and an add Risikomanagement form
   When I type 'My Risikoreferenz' into the title field
    and I submit the form
   Then a Risikoreferenz with the title 'My Risikoreferenz' has been created

Scenario: As a site administrator I can view a Risikoreferenz
  Given a logged-in site administrator
    and a Risikoreferenz 'My Risikoreferenz'
   When I go to the Risikoreferenz view
   Then I can see the Risikoreferenz title 'My Risikoreferenz'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Risikomanagement form
  Go To  ${PLONE_URL}/++add++Risikomanagement

a Risikoreferenz 'My Risikoreferenz'
  Create content  type=Risikomanagement  id=my-risikoreferenz  title=My Risikoreferenz

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Risikoreferenz view
  Go To  ${PLONE_URL}/my-risikoreferenz
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Risikoreferenz with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Risikoreferenz title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
