# User Management

## Introduction

This app is destinated to manage user in a business

## Installation

## How to run the app in VSCode

Create files launch.json and tasks.json
and run in the command palete using Run tasks
![alt text](image.png)
tasks.json

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "run",
      "type": "shell",
      "command": "uvicorn main:app --reload",
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": [],
      "options": {
        "cwd": "${workspaceFolder}/src"
      }
    }
  ]
}
```

launch.json

```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: FastAPI",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "main:app",
        "--reload"
      ],
      "cwd": "${workspaceFolder}/src",
      "jinja": true
    }
  ]
}
```

## Migrations

`alembic -c src/shared/infrastructure/persistence/migrations/alembic.ini revision --autogenerate`

`alembic -c src/shared/infrastructure/persistence/migrations/alembic.ini upgrade head`
