# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.datenschutz -t test_vorlage_d_s_f_a.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.datenschutz.testing.EDI_DATENSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/datenschutz/tests/robot/test_vorlage_d_s_f_a.robot
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

Scenario: As a site administrator I can add a Vorlage DSFA
  Given a logged-in site administrator
    and an add Vorlage DSFA form
   When I type 'My Vorlage DSFA' into the title field
    and I submit the form
   Then a Vorlage DSFA with the title 'My Vorlage DSFA' has been created

Scenario: As a site administrator I can view a Vorlage DSFA
  Given a logged-in site administrator
    and a Vorlage DSFA 'My Vorlage DSFA'
   When I go to the Vorlage DSFA view
   Then I can see the Vorlage DSFA title 'My Vorlage DSFA'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Vorlage DSFA form
  Go To  ${PLONE_URL}/++add++Vorlage DSFA

a Vorlage DSFA 'My Vorlage DSFA'
  Create content  type=Vorlage DSFA  id=my-vorlage_d_s_f_a  title=My Vorlage DSFA

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Vorlage DSFA view
  Go To  ${PLONE_URL}/my-vorlage_d_s_f_a
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Vorlage DSFA with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Vorlage DSFA title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
