# Todo-tool
Local TODO tool with Python, Flask, SQLite, and Docker

## Stack
    1. Python
    2. SQLite
    3. Flusk
    4. Docker

## Features    
    1. The user can add todos and those can be saved in a local SQLite database
    2. Add TODO
        1. Date
        2. Title
        3. Notes
        4. Tags
    3. Update TODO
    4. Delete TODO
    5. Mark TODO as Completed
    6. Add Hour Spending Tracker on TODO
        1. Start
        2. Pause
        3. End
    7. Change the TODO status
    8. Create a Report section to display the TODO list with the following columns
        1. Id
        2. Title
        3. Notes
        4. Due By
        5. Tags
        6. Status
            1. Complete
            2. Due
            3. Hold
            4. Ongoing
        7. Created On
    9. Create Filters for the report
        1. Date
        2. Status
        3. Search
            1. Title
            2. Notes
            3. Tags
    10. The report should be the Homescreen
    11. Insert/Update/Delete should be done using popup modal
    12. Export the report
        1. CSV
        2. Clipboard
    13. EOD Mail Feature

## Identified API

| Method | URL                  | Description                  |
| ------ | -------------------- | ---------------------------- |
| GET    | {base_url}/todo      | List all todo                |
| POST   | {base_url}/todo      | Create new todo              |
| GET    | {base_url}/todo/{id} | Get todo by ID               |
| PUT    | {base_url}/todo/{id} | Update todo by ID            |
| DELETE | {base_url}/todo/{id} | Delete todo by ID            |
| PATCH  | {base_url}/todo/{id} | Update todo by ID            |
| GET    | {base_url}/log       | Get all logs with total time |
| POST   | {base_url}/log       | Add start/stop time          |
| GET    | {base_url}/note/?    | Get notes by parametres      |
| POST   | {base_url}/note      | Create new note entry        |


## Identified database schema

| Table Name | Columns      | Data Types   |
| ---------- | ------------ | ------------ |
| todo       | id           | INT, AI, PK  |
|            | title        | VARCHAR(250) |
|            | description  | TEXT         |
|            | status       | INT          |
|            | completed_at | DATETIME     |
|            | created_at   | DATETIME     |
|            |              |              |
| logs       | id           | INT, AI, PK  |
|            | todo_id      | INT          |
|            | start_time   | DATETIME     |
|            | end_time     | DATETIME     |
|            |              |              |
| notes      | id           | INT, AI, PK  |
|            | todo_id      | INT          |
|            | notes        | TEXT         |
|            | created_at   | DATETIME     |

## NB: We will add more points in future if needed.