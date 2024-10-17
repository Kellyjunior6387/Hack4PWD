# Job API Documentation

This is the documentation for the Job API, providing a set of endpoints for creating, retrieving, and searching job listings.

## Overview

The API supports the following functionalities:
- Listing all jobs
- Retrieving detailed information about a specific job
- Creating a new job listing (for employers only)
- Searching for jobs by title and accessibility tags

---

## Table of Contents

1. [Job List](#1-job-list)
2. [Job Detail](#2-job-detail)
3. [Job Creation](#3-job-creation)
4. [Job Search](#4-job-search)

---

### 1. Job List

**Endpoint**: `/api/jobs/`  
**Method**: `GET`  
**Description**: Retrieve a list of all job listings.

#### Response

- **Status Code**: `200 OK`
- **Body**: A JSON array of job objects.

```json
[
    {
        "id": 1,
        "title": "Software Developer",
        "description": "Develop and maintain web applications.",
        "employer": "Company ABC",
        "location": "Remote",
        "posted_at": "2024-10-15"
    },
]
```

### 2. Job Detail

**Endpoint**: `/api/jobs/<job_id>/`  
**Method**: `GET`  
**Description**: Retrieve detailed information about a specific job by its ID.

**Parameters**
**job_id (required)**: Retrieve detailed information about a specific job by its ID.

#### Response

- **Status Code**: `200 OK` if job exist;
- **Status Code**: `404 Not Found` if job does not exist;

- **Body**: A JSON array of job objects.



```json
[
 {
    "id": 1,
    "title": "Software Developer",
    "description": "Develop and maintain web applications.",
    "employer": "Company ABC",
    "location": "Remote",
    "accessibility_tags": ["remote", "flexible hours"],
    "posted_at": "2024-10-15"
},
]
```

### 3. Job Creation

**Endpoint**: `/api/jobs/create/`  
**Method**: `POST`  
**Authentication**: Required (Only employers can create jobs)  
**Description**: Allows authenticated users with the role of "employer" to create new job listings.

**Request Body**

- `title` (string, required): The title of the job.
- `description` (string, required): Detailed description of the job.
- `location` (string, required): Location of the job.
- `requirements` (array, optional): List of job requirements.
- `accessibility_tags` (array, optional): Accessibility tags related to the job.

```json
{
        "title": "Software Developer",
        "description": "Develop and maintain web applications.",
        "location": "Remote",
        "requirements": ["Python", "Django", "JavaScript"],
        "accessibility_tags": ["remote", "flexible hours"]
}
```

**Response**

- **Status Code**: `201 Created` if job is successfully created; `403 Forbidden` if user is not an employer.
- **Body**: JSON object of the newly created job.

```json
    {
        "id": 2,
        "title": "Software Developer",
        "description": "Develop and maintain web applications.",
        "employer": "Company XYZ",
        "location": "Remote",
        "posted_at": "2024-10-15"
    }
```

### 4. Job Search

**Endpoint**: `/api/jobs/search`  
**Method**: `GET`  
**Description**: Search for a job title or specific tags.

**Parameters**
- **title (string, optional)**: Job title to search for (partial matches allowed).
- **tags (array, optional)**: List of accessibility tags to filter jobs by.

#### Response

- **Status Code**: `200 OK`
- **Body**: A JSON array of job objects.

```json
[
    {
        "id": 1,
        "title": "Software Developer",
        "description": "Develop and maintain web applications.",
        "location": "Remote",
        "accessibility_tags": ["remote", "flexible hours"],
        "posted_at": "2024-10-15"
    },
]
```
