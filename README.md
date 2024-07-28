# Patient Management Application

A Patient Management Application has been developed using Django to streamline hospital operations. This application automates the patient registration and verification process, making it easier for reception staff to manage patient information efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Local Development](#local-development)
  - [Run on Local Host with Docker](#run-on-local-host-with-docker)
  - [AWS Deployment](#aws-deployment)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Hospitals often face challenges in managing patient information, especially with manual processes that involve recording and retrieving patient details. This Django-based application addresses these challenges by automating the registration and verification processes, allowing reception staff to quickly check if a patient is already registered and, if not, facilitate their registration.

## Features

- Automates patient registration and verification.
- Enables quick lookup of registered patients.
- Streamlines administrative processes.
- Enhances efficiency of patient management.

## Technologies Used

- **Django**: Backend framework for the application.
- **Docker**: Containerization of the application.
- **Amazon EC2**: Hosting the application.
- **Amazon RDS**: Managing the database in a private subnet.

## Architecture

The application architecture consists of the following components:

1. **Django Application**: Handles patient registration and verification.
2. **Docker**: Containerizes the Django application for easy deployment.
3. **Amazon EC2**: Hosts the Docker container to ensure global accessibility.
4. **Amazon RDS**: Provides a secure and scalable database solution.

## Setup and Installation

### Prerequisites

- Python 3.x
- Docker
- AWS account with EC2 and RDS access

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/amdhazm/Django-Hospital-Deployment.git
   cd Django-Hospital-Deployment
