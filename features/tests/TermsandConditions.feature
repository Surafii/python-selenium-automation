# Created by surafiiabetew at 2/24/21
Feature: # Enter feature name here
  # Enter feature description here

 Scenario: User can open and close Amazon Applications
  Given Open Amazon Terms_and_Conditions page
  When Store original windows
  And Click on Amazon applications link
  And Switch to the newly opened window
  And Amazon page is opened
  Then User can close new window and switch back to original window





 Scenario: Amazon 404 page opens blog in another window
  Given Open Amazon Dress B0777K16R9V3 page
  When store original windows
  And click to open blog
  And switch to the newly opened window
  Then user can close new window and switch back to original window
    # Enter steps here