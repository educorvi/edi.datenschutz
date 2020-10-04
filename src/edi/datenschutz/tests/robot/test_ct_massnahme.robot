# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_massnahme.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_massnahme.robot
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

Scenario: As a site administrator I can add a Massnahme
  Given a logged-in site administrator
    and an add Massnahme form
   When I type 'My Massnahme' into the title field
    and I submit the form
   Then a Massnahme with the title 'My Massnahme' has been created

Scenario: As a site administrator I can view a Massnahme
  Given a logged-in site administrator
    and a Massnahme 'My Massnahme'
   When I go to the Massnahme view
   Then I can see the Massnahme title 'My Massnahme'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Massnahme form
  Go To  ${PLONE_URL}/++add++Massnahme

a Massnahme 'My Massnahme'
  Create content  type=Massnahme  id=my-massnahme  title=My Massnahme

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Massnahme view
  Go To  ${PLONE_URL}/my-massnahme
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Massnahme with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Massnahme title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
