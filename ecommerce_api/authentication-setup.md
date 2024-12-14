# Authentication Setup for E-commerce API

## 1. Basic Authentication
The API is set up to use Django's built-in **Basic Authentication** for user authentication. This is done by adding the following configuration to the `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
}
2. Token Authentication
For more secure authentication, the API is also set up to support Token Authentication using Django Rest Framework's TokenAuthentication. The following settings were added to settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
3. Token Generation
To obtain a token, send a POST request to /api-token-auth/ with the user's credentials:


{
    "username": "user1",
    "password": "password123"
}
The response will contain a token:


{
    "token": "your_generated_token_here"
}
