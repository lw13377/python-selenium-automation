Feature:

Scenario: User can open and close Terms and Conditions from sign in page
 Given Open Target App page
 When Store original window
 And Click Privacy Policy link
 And Switch to new window
 Then Verify Privacy Policy page opened
 And Close current page
 And Return to original window