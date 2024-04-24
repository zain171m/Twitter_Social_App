# Twitter_Social_App

This project is a social network implemented using Python, JavaScript, HTML, and CSS. It allows users to make posts, follow other users, and interact with posts by liking them.

## Features Implemented

### New Post
- Users who are signed in can write new text-based posts by filling in text into a text area and then clicking a button to submit the post.

### All Posts
- The "All Posts" link in the navigation bar takes the user to a page where they can see all posts from all users, with the most recent posts first.
- Each post includes the username of the poster, the post content itself, the date and time at which the post was made, and the number of likes the post has.

### Profile Page
- Clicking on a username loads that user’s profile page.
- The profile page displays the number of followers the user has, as well as the number of people that the user follows.
- It displays all of the posts for that user, in reverse chronological order.
- For any other user who is signed in, this page displays a "Follow" or "Unfollow" button that lets the current user toggle whether or not they are following this user’s posts.

### Following
- The "Following" link in the navigation bar takes the user to a page where they see all posts made by users that the current user follows.
- This page behaves just like the "All Posts" page, but with a more limited set of posts.
- This page is only available to users who are signed in.

### Pagination
- Posts are displayed 10 on a page.
- If there are more than ten posts, a "Next" button appears to take the user to the next page of posts (which should be older than the current page of posts).
- If not on the first page, a "Previous" button appears to take the user to the previous page of posts.

### Edit Post
- Users can click an "Edit" button or link on any of their own posts to edit that post.
- When a user clicks "Edit" for one of their own posts, the content of their post is replaced with a textarea where the user can edit the content of their post.
- The user can then "Save" the edited post without requiring a reload of the entire page.
- Security measures are in place to prevent users from editing another user’s posts.

### "Like" and "Unlike"
- Users can click a button or link on any post to toggle whether or not they "like" that post.
- Asynchronously, the server updates the like count and the post’s like count displayed on the page without requiring a reload of the entire page.

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install Python and necessary dependencies.
3. Set up a virtual environment.
4. Run the application using Flask's built-in development server.
5. Access the application in your web browser.

## Technologies Used

- Python
- Flask
- JavaScript
- HTML
- CSS

## Credits

This project was completed as part of the CS50W course by Harvard University.

