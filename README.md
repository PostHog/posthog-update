# Posthog Update

A super simple microservice that allows PostHog apps to find out if there are any updates.

## Developing locally

```bash
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

## Deploying

The service gets automatically deployed [on Heroku](https://dashboard.heroku.com/apps/posthog-update) when you push to master.