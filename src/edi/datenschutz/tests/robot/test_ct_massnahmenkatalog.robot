# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_massnahmenkatalog.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_massnahmenkatalog.robot
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

Scenario: As a site administrator I can add a Massnahmenkatalog
  Given a logged-in site administrator
    and an add Verarbeitungstaetigkeit form
   When I type 'My Massnahmenkatalog' into the title field
    and I submit the form
   Then a Massnahmenkatalog with the title 'My Massnahmenkatalog' has been created

Scenario: As a site administrator I can view a Massnahmenkatalog
  Given a logged-in site administrator
    and a Massnahmenkatalog 'My Massnahmenkatalog'
   When I go to the Massnahmenkatalog view
   Then I can see the Massnahmenkatalog title 'My Massnahmenkatalog'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Verarbeitungstaetigkeit form
  Go To  ${PLONE_URL}/++add++Verarbeitungstaetigkeit

a Massnahmenkatalog 'My Massnahmenkatalog'
  Create content  type=Verarbeitungstaetigkeit  id=my-massnahmenkatalog  title=My Massnahmenkatalog

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Massnahmenkatalog view
  Go To  ${PLONE_URL}/my-massnahmenkatalog
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Massnahmenkatalog with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Massnahmenkatalog title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
