# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_zielerfuellungsmanagement.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_zielerfuellungsmanagement.robot
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

Scenario: As a site administrator I can add a Zielerfuellungsmanagement
  Given a logged-in site administrator
    and an add Verarbeitungstaetigkeit form
   When I type 'My Zielerfuellungsmanagement' into the title field
    and I submit the form
   Then a Zielerfuellungsmanagement with the title 'My Zielerfuellungsmanagement' has been created

Scenario: As a site administrator I can view a Zielerfuellungsmanagement
  Given a logged-in site administrator
    and a Zielerfuellungsmanagement 'My Zielerfuellungsmanagement'
   When I go to the Zielerfuellungsmanagement view
   Then I can see the Zielerfuellungsmanagement title 'My Zielerfuellungsmanagement'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Verarbeitungstaetigkeit form
  Go To  ${PLONE_URL}/++add++Verarbeitungstaetigkeit

a Zielerfuellungsmanagement 'My Zielerfuellungsmanagement'
  Create content  type=Verarbeitungstaetigkeit  id=my-zielerfuellungsmanagement  title=My Zielerfuellungsmanagement

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Zielerfuellungsmanagement view
  Go To  ${PLONE_URL}/my-zielerfuellungsmanagement
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Zielerfuellungsmanagement with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Zielerfuellungsmanagement title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
