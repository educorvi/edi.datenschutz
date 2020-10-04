# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_kontrolle.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_kontrolle.robot
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

Scenario: As a site administrator I can add a Kontrolle
  Given a logged-in site administrator
    and an add Massnahme form
   When I type 'My Kontrolle' into the title field
    and I submit the form
   Then a Kontrolle with the title 'My Kontrolle' has been created

Scenario: As a site administrator I can view a Kontrolle
  Given a logged-in site administrator
    and a Kontrolle 'My Kontrolle'
   When I go to the Kontrolle view
   Then I can see the Kontrolle title 'My Kontrolle'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Massnahme form
  Go To  ${PLONE_URL}/++add++Massnahme

a Kontrolle 'My Kontrolle'
  Create content  type=Massnahme  id=my-kontrolle  title=My Kontrolle

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Kontrolle view
  Go To  ${PLONE_URL}/my-kontrolle
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Kontrolle with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Kontrolle title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
