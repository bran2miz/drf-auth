# Authentication & Production Server - Lab 33

## Author: Brandon Mizutani

Version: 1.0.0 (PR URL: [PR URL](https://github.com/bran2miz/drf-auth/pull/1)

## Overview

This lab assignment required us to add Authentication and switching to a production server.

## Getting Started

### Lab 31

We had to create a project that followed the same steps as the previous lab, only this time we had to add:

- JSON Web Token Authentication to the API. (Install needed libraries in project configuration and/or site settings.)

- Keep any pre-existing authentication so DRF Browsable API still usable. (Install needed libraries in project configuration and/or site settings.)

We then had to:

- Create a boilerplate Dockerfile and docker-compose.yml so you don’t need to start from scratch each time.

- Switch to using Gunicorn instead of Django’s built in development server

- Properly handle static files using Whitenoise to avoid running into styling issues.

## Architecture

Python, Django, Models, get_user_model, superuser, CRUD, Docker, REST, permissions, postgresql, JWT, whitenoise, Gunicorn

## Change Log

03-24-22 -- Pages render as expected and assignment is complete.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Connor Boyce

Roger Huba
