# Profiles Management API

This repository contains a profiles (users) management API that enables the users to:
* Do CRUD operations on profiles.
* Authenticate users.
* Do CRUD operations on posts as feed items.

This API is created using Django and Django REST Framework based on classes:
* APIView
* ViewSet

Permissions are also applied to the API, i.e:
* A user can update their status only.
* A user can update their profile only.
* Only logged users can retrieve the status feed.

__*Since this project is meant to be a practice for me, the logic of some functions is not applied.*__

The *requirements.txt* file is included.
