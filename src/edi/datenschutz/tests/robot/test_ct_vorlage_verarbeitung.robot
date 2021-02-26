# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_vorlage_verarbeitung.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_vorlage_verarbeitung.robot
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

Scenario: As a site administrator I can add a Vorlage Verarbeitung
  Given a logged-in site administrator
    and an add Vorlage Verarbeitung form
   When I type 'My Vorlage Verarbeitung' into the title field
    and I submit the form
   Then a Vorlage Verarbeitung with the title 'My Vorlage Verarbeitung' has been created

Scenario: As a site administrator I can view a Vorlage Verarbeitung
  Given a logged-in site administrator
    and a Vorlage Verarbeitung 'My Vorlage Verarbeitung'
   When I go to the Vorlage Verarbeitung view
   Then I can see the Vorlage Verarbeitung title 'My Vorlage Verarbeitung'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Vorlage Verarbeitung form
  Go To  ${PLONE_URL}/++add++Vorlage Verarbeitung

a Vorlage Verarbeitung 'My Vorlage Verarbeitung'
  Create content  type=Vorlage Verarbeitung  id=my-vorlage_verarbeitung  title=My Vorlage Verarbeitung

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Vorlage Verarbeitung view
  Go To  ${PLONE_URL}/my-vorlage_verarbeitung
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Vorlage Verarbeitung with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Vorlage Verarbeitung title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
