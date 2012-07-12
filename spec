Feature: Login
As a ...
I would like to ...
So that ...

	Scenario: Test Scenario
		Given I am on the "Login" page
		Then I should see "Username"
		Then I fill in "Username" with text "Text"
		Then I should see "Password"
		Then I fill in "Password" with text "Text"
		Then I should see "Location"
		Then I fill in "Location" with text "Text"
		And I press "Finish"
		Then I should be on the next page


Feature: Home Page
As a ...
I would like to ...
So that ...

	Scenario: I have an authorised user
		Given I am on the "Home Page" page
		Then I should see "Project Name" with value "Vitals Registration"
		Then I should see a tab "Overview" linking to "overview.html"
		Then I should see a button "Find or register baby" linking to "search.html"
		And I press "Finish"
		Then I should be on the next page

Feature: Patient Dashboard
As a ...
I would like to ...
So that ...

	Scenario: I have an authorised user
		Given I am on the "Patient Dashboard" page
		Then I should see "Project Name" with value "Vitals Registration"
		Then I should see a tab "Summary" linking to "summary.html"
		Then I should see a button "Baby Demographics" linking to "baby_demographics.html"
		Then I should see a button "Mother Demographics" linking to "mother_demographics.html"
		Then I should see a button "Father Demographics" linking to "father_demographics.html"
		Then I should see a button "Birth Report" linking to "birth_report.html"
		And I press "Finish"
		Then I should be on the next page





Feature: Baby Demographics
As a ...
I would like to ...
So that ...

	Scenario: Logged in user
		Given I am on the "Baby Demographics" page
		Then I should see "First Name"
		Then I fill in "First Name" with text "Text"
		Then I should see "Middle Name"
		Then I fill in "Middle Name" with text "Text"
		Then I should see "Last Name"
		Then I fill in "Last Name" with text "Text"
		Then I should see "Date of birth"
		Then I fill in "Date of birth" with a date ""
		Then I should see "Sex"
		And I should see ""
		And I should see "Male"
		And I should see "Female"
		And I select ""
		And I press "Finish"
		Then I should be on the next page




Feature: Mother Demographics
As a ...
I would like to ...
So that ...

	Scenario: Test Scenario
		Given I am on the "Mother Demographics" page
		Then I should see "First Name"
		Then I fill in "First Name" with text "Text"
		Then I should see "Middle Name"
		Then I fill in "Middle Name" with text "Text"
		Then I should see "Last Name"
		Then I fill in "Last Name" with text "Text"
		Then I should see "Maiden Name"
		Then I fill in "Maiden Name" with text "Text"
		Then I should see "Nationality"
		And I should see ""
		And I should see "Malawian"
		And I should see "Other"
		And I select ""
		Then I should see "Specify" If "Nationality" == "Other"
		Then I fill in "Specify" with text "Text"
		Then I should see "ID No."
		Then I fill in "ID No." with text "Text"
		Then I should see "Home District"
		And I should see ""
		And I should see "List of Districts"
		And I select ""
		Then I should see "T/A"
		And I should see ""
		And I should see "List of T/As in District"
		And I select ""
		Then I should see "Village"
		And I should see ""
		And I should see "List of villages under T/A"
		And I select ""
		And I press "Finish"
		Then I should be on the next page




Feature: Father Demographics
As a ...
I would like to ...
So that ...

	Scenario: Test Scenario
		Given I am on the "Father Demographics" page
		Then I should see "Is father known"
		And I should see ""
		And I should see "Yes"
		And I should see "No"
		And I select ""
		Then I should see "First Name" If "Is father known" == "Yes"
		Then I fill in "First Name" with text "Text"
		Then I should see "Middle Name" If "Is father known" == "Yes"
		Then I fill in "Middle Name" with text "Text"
		Then I should see "Last Name" If "Is father known" == "Yes"
		Then I fill in "Last Name" with text "Text"
		Then I should see "Nationality" If "Is father known" == "Yes"
		And I should see ""
		And I should see "Malawian"
		And I should see "Other"
		And I select ""
		Then I should see "Specify" If "Is father known" == "Yes" && "Nationality" == "Other"
		Then I fill in "Specify" with text "Text"
		Then I should see "ID No." If "Is father known" == "Yes"
		Then I fill in "ID No." with text "Text"
		Then I should see "Home District" If "Is father known" == "Yes"
		And I should see ""
		And I should see "List of Districts"
		And I select ""
		Then I should see "T/A" If "Is father known" == "Yes"
		And I should see ""
		And I should see "List of T/As in district"
		And I select ""
		Then I should see "Village" If "Is father known" == "Yes"
		And I should see ""
		And I should see "List of villages"
		And I select ""
		Then I should see "Physical Address" If "Is father known" == "Yes"
		Then I fill in "Physical Address" with text "Text"
		And I press "Finish"
		Then I should be on the next page

Feature: User Details
As a ...
I would like to ...
So that ...

	Scenario: Test Scenario
		Given I am on the "User Details" page
		Then I should see "Were the details collected here"
		And I should see ""
		And I should see "Yes"
		And I should see "No"
		And I select ""
		Then I should see "Provider First Name" If "Were the details collected here" == "No"
		Then I fill in "Provider First Name" with text "Text"
		Then I should see "Provider Middle Name" If "Were the details collected here" == "No"
		Then I fill in "Provider Middle Name" with text "Text"
		Then I should see "Provider Last Name" If "Were the details collected here" == "No"
		Then I fill in "Provider Last Name" with text "Text"
		Then I should see "Provider Title"
		Then I fill in "Provider Title" with text "Text"
		Then I should see "Place of Issue" If "Were the details collected here" == "No"
		And I should see "Here"
		And I should see "List of sites"
		And I select "Here"
		And I press "Finish"
		Then I should be on the next page




