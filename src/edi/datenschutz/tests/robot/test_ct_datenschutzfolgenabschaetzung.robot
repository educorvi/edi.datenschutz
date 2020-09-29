# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_datenschutzfolgenabschaetzung.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_datenschutzfolgenabschaetzung.robot
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

Scenario: As a site administrator I can add a Datenschutzfolgenabschaetzung
  Given a logged-in site administrator
    and an add Datenschutzfolgenabschaetzung form
   When I type 'My Datenschutzfolgenabschaetzung' into the title field
    and I submit the form
   Then a Datenschutzfolgenabschaetzung with the title 'My Datenschutzfolgenabschaetzung' has been created

Scenario: As a site administrator I can view a Datenschutzfolgenabschaetzung
  Given a logged-in site administrator
    and a Datenschutzfolgenabschaetzung 'My Datenschutzfolgenabschaetzung'
   When I go to the Datenschutzfolgenabschaetzung view
   Then I can see the Datenschutzfolgenabschaetzung title 'My Datenschutzfolgenabschaetzung'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Datenschutzfolgenabschaetzung form
  Go To  ${PLONE_URL}/++add++Datenschutzfolgenabschaetzung

a Datenschutzfolgenabschaetzung 'My Datenschutzfolgenabschaetzung'
  Create content  type=Datenschutzfolgenabschaetzung  id=my-datenschutzfolgenabschaetzung  title=My Datenschutzfolgenabschaetzung

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Datenschutzfolgenabschaetzung view
  Go To  ${PLONE_URL}/my-datenschutzfolgenabschaetzung
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Datenschutzfolgenabschaetzung with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Datenschutzfolgenabschaetzung title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
