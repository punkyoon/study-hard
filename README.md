# study-hard

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/punkyoon/study-hard/blob/master/LICENSE) [![Build Status](https://travis-ci.org/punkyoon/study-hard.svg?branch=master)](https://travis-ci.org/punkyoon/study-hard)

Study-hard is a Web-Based Application for managing study group.

Before `study-hard`, study group manager had to be in charge of whole operation and financial management such as panalty, gurantee etc. Which was unclearly supervised by manager.

The `study-hard` can solve above problems. `study-hard` support recruitment, management and participation of study gorups to deal with problems.

## Overview

![manager-overview](https://github.com/punkyoon/study-hard/blob/master/images/study-hard-manager-ver.gif)

## Features

**1. As a manager**

* Rejecting or approving participation in study group
* Possible to access applicant’s information (institution, email, gender, etc.)
* Managing study group members attendance (Late / absent / attendance)
* Managing study group members penalty (Reasons for penalty / Fill in fine amount)
* Managing deposit payment
* Posting Announcements

**2. As a general user**

* Searching study group
* Asking for permission to join specific study group
* Checking announcement (a study group that joined)
* Each member can check other members attendance, payment of penalties and deposit money
* Can check the total amount of fine in study group
* Can chat with study member

## Installation and Setting

#### Build Requirements

* Python 3.5+
* Django 1.11+
* PostgreSQL
* Ubuntu or Using Docker Image

> We recommand you to use docker image

#### Installation

```sh
$ docker-compose up -d
$ make
```

For further instructions on installation, please [visit our wiki page](https://github.com/punkyoon/study-hard/wiki/Installation-and-Settings).

## Third Party Libraries
Please check [NOTICE](https://github.com/punkyoon/study-hard/blob/master/NOTICE)

* [`django`](https://github.com/django/django)
* [`django-phonenumber-field`](https://github.com/stefanfoulis/django-phonenumber-field)
* [`pokinator`](https://github.com/punkyoon/pokinator)
* [`psycopg2`](http://initd.org/psycopg)
* [`raven`](https://github.com/getsentry/raven-python)
* [`asgi_redis`](https://github.com/django/asgi_redis)
* [`django-redis`](https://github.com/niwinz/django-redis)
* [`channels`](https://github.com/django/channels)
* [`twisted`](https://github.com/twisted/twisted)
* [`jquery`](https://jquery.org)
* [`bootstrap`](https://github.com/twbs/bootstrap)
* [`font-awesome`](http://fontawesome.io)


## Documentation

We have a [wiki page](https://github.com/punkyoon/study-hard/wiki) for project introduction, installation guide, and some documentation.

We welcome any documentation contribution.

## Bug Report & Contribution

We welcome any and all suggestions. Please follow our guideline when contributing to our project.

If you find a bug, please report it to us using the [Issues](https://github.com/punkyoon/study-hard/issues) page on GitHub, with appropriate labels(bug, ..)!

And we're also using error logging system with [Sentry](https://sentry.io/study-hard/). So you don't need a capture page for every error log.

## License

[GNU General Public License v3.0 (GPL-3)](https://github.com/ddok-ddok/study-hard/blob/master/LICENSE)

study-hard, Study group management service Copyright (C) 2017 3ssarah, punkyoon, simzipark

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
