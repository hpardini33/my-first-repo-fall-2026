# Deploying to Render

Follow this guide to host the application on a free server provided by the Render platform.

References:
  + https://render.com/docs/deploy-flask

## Render Setup

Login to [Render](https://dashboard.render.com) and visit the dashboard.

Create a New "Web Service".

Update the name, as desired.

Choose your own repository from GitHub (or specify its public URL).

Specify the build command:

```
pip install -r requirements.txt
```

Specify the start command:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Set the `ALPHAVANTAGE_API_KEY` environment variable (your own API key value, without quotes). If you implemented flash messaging, also set a `SECRET_KEY`.

Finally, click to "Deploy" the web service.

## Render Deploys

Whenever you push new code to the `main` branch, Render will automatically redeploy the site.

You can also trigger deploys manually.

Live site: https://hollie-web-app.onrender.com