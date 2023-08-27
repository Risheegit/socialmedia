# Social Media App

This application is built using Django for the backend, while the frontend is developed using HTML, CSS, and Bootstrap. It incorporates essential social media features, including CRUD functionality for posts, Google OAuth for secure authentication, comments, image sharing, and much more.

## Key Features

- **User Profiles**: Every user has a dedicated profile where they can share information about themselves, their posts, and follow other users.

- **Post Creation and Interaction**: Users can create, edit, and delete posts. They can also like, comment on, and share posts with their followers.

- **Authentication via Google OAuth**: Secure user authentication is provided through Google OAuth, ensuring a seamless and trustworthy login experience.

- **Image Sharing**: Users can upload and share images in their posts, enhancing the visual appeal of their content.

- **Comments**: Engage in conversations by leaving comments on posts. This feature promotes interaction and discussion within the community.

- **Follow and Be Followed**: Users can follow other users, enabling them to see posts from those they follow in their feed.

## Technology Stack

- **Backend**: Django is the backend framework, while SQLLite is used as the database to store user data, posts, and interactions.

- **Frontend**: The user interface is built using HTML, CSS, and Bootstrap, providing a responsive and visually appealing design.

- **Authentication**: Google OAuth is implemented for secure and convenient user authentication.

## Setup

To set up and run this project locally, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/Risheegit/socialmedia.git
```

2. Navigate to the project directory


3. Create a virtual environment to install dependencies in and activate it:

```
virtualenv env
source env/bin/activate
```


4. Install the required Python packages:

```
pip install -r requirements.txt
```


5. Configure your Google OAuth credentials in the Django settings.

6. Run database migrations:

```
python manage.py migrate
```


7. Start the development server:

```
python manage.py runserver
```


8. Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to access the application.

## Usage

- Create an account or log in using Google OAuth.

- Explore posts from other users in your feed.

- Create your own posts, including text and images.

- Like, comment on, and share posts with your followers.

- Follow other users to see their posts in your feed.

