# Testing

* User story based end to end testing was performed on both desktop and mobile devices.
* Tests are based on user stories and their acceptance criteria
* Expanded tests were included to cover the entire user experince
* Full scenario and test steps descriptions were omitted for brevity and readability
* Future projects will include testing items in the project board itself

### Manual Tests

|Test| Result | Note
|--|--|--|
| Does the main page display correctly? | Pass | N\A |
| Is the page responsive to different devices? | Pass | N\A |
| CSS animations display correctly across devices? | Pass | N\A |
| Does the navbar only show links available to anon users? | Pass | N\A |
| Does the shop page display just 6 items per pages | Pass | N\A |
| Does the search page display itemas that match the text searched? | Pass | N\A |
| Does clicking an art card take you to that items details? | Pass | N\A |
| Does clicking Account > Register, open create account page? | Pass | N\A |
| Does the create account page validate that the username field is not blank? | Pass | N\A |
| Does the create account page validate that the username entered is not in use? | Pass | N\A |
| Does the password validator ensure a strong password? | Pass | N\A |
| Does the account get created when the user clicks create account | Pass | N\A |
| Does the user get automatically signed in? | Pass | N\A |
| Does the user get a notification at the top of the screen to confirm sign in? | Pass | N\A |
| Does the navbar show extra options for authenticated user | Pass | N\A |
| Does the navbar show extra options (staff pages) for authenticated user who are staff | Pass | N\A |
| Does the view sales page display all art items and their otal sales? | Pass | N\A |
| Does clicking the Account > Sign Out (USER) link show the confirmation? | Pass | N\A |
| Does confirming logout then logout the user and take them to the home page?| Pass | N\A |
| Does the user get a message at the top of the screen to confirm they signed out? | Pass | N\A |
| Does clicking staff pages > Add art open the add art page?  | Pass | N\A |
| Do all fields validate input? | Pass | N\A |
| Do required fields provide feedback if empty? | Pass | N\A |
| Does trying to upload an non image file get blocked| Pass | N\A |
| Does the user get a message at the top of the screen to confirm they created the art item?  | Pass | N\A |
| Does the staff admin link take the user to the admin panel? | Pass | N\A |
| Does clicking on at art item in the shop take you to the details screen | Pass | N\A |
| Do all the correct details for the art piece display correctly? | Pass | N\A |
| Do the images display correctly? | Pass | N\A |
| Do all fields correctly render with formatting? | Pass | N\A |
| Do edit/delete buttons display if user is staff? | Pass | N\A |
| Does the register button display if the user is not authenticated? | Pass | N\A |
| Does the purchase button display if the user is authenticated? | Pass | N\A |
| Does the edit button open the edit art view? | Pass | N\A |
| Does clicking the delete button show the delete page confirmation? | Pass | N\A |
| Does the confirmation have the correct details? | Pass | N\A |
| Does clicking cancel take them back to the detail page they were viewing? | Pass | N\A |
| Does clicking confirm delete the record and take user back to the shop | Pass | N\A |
| Does clicking purchase add that item to the users cart | Pass | N\A |
| Does a new order get created if there isn't an existing one | Pass | N\A |
| Does the user get shown the cart and all current items and total price | Pass | N\A |
| Does the order persist till the next time the user logs in? | Pass | N\A |
| Does the remove item button display? | Pass | N\A |
| Does clicking the remove item present a confirmation? | Pass | N\A |
| If the user cancels or confirms are they taken back to the cart? | Pass | N\A |
| Does the complete order button display? | Pass | N\A |
| Does the complete order button trigger and stripe checkout display? | Pass | N\A |
| Does the checkout have the correct total and connected users email populated? | Pass | N\A |
| Does stripe allow (test) payment to proceed? | Pass | N\A |
| Does the user get redirected back to the success page that confirms their order completed? | Pass | N\A |
| Does the order get marked complete? | Pass | N\A |
| Do items in the order have their sales total incremented? | Pass | N\A |
| Does the user get their order confirmation email along with links to download the full res images? | Pass | N\A |

### Bugs & Known Issues

There are no bugs or known issues at this time

#### Feedback from project submission called out the following

Admin email being hardcoded to checkout - unclear what this was in relation to - confirmed again in testing that emails are being sent to the user that is authenticated - I confirmed this in tests and in the sent items in the related gmail account for the site.

Mention of an incorrect postcode during checkout leading to an error - unable to reproduce - checkout stripe is not collecting any address information since delivery is digital only

Product with a negative value - this was partially intentional as I was planning to add coupon that reduced the orders price - I tested and was able to add items with negative values and they reduced the order price when added to the cart - Its not possible to checkout with just a coupon image - This was a partially implmenmted feature I should have removed - since it was not called out directly as part of the fail, I have left it as is.

The specific fail reason was the lack of a newsletter management feature - I researched mailchimp and implmented that - tested that the popup shows at the desired intervals and also added a direct link for users to sign up at any time.


