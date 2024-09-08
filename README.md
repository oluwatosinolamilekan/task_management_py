## Flask Task Processing API

This project is a simple Flask-based API for task processing, simulating external processing by responding with a message when a task is created.

## Minimum system requirements
Prerequisites
- Python: Ensure you have Python installed (version 3.x).
- pip: Ensure pip is installed to manage Python packages.

## Installation
```
    git clone 
    cd task_management_py
```

## Set Up a Virtual Environment (Optional but Recommended)

- On Windows:
```
    python -m venv venv
    .\venv\Scripts\activate
```

- On macOS/Linux:

```
    python3 -m venv venv
    source venv/bin/activate
```

##  Install the Dependencies

Use the `requirements.txt` file to install the necessary Python packages:

This will install Flask and all required dependencies.

```
    pip install -r requirements.txt
```

## Running the Flask Server
 To start the Flask development server, run the following command:
 ```
  python app.py
 ```

Or, if using python3:

```
 python3 app.py
```

The API will now be running at http://localhost:5000 or   http://127.0.0.1:5000


## Endpoints
    Process Task
 - Url: `/process_task`
 - Method: POST
 - Request Body:
    ```json
        {
            "name": "Task Name",
        }
    ```
- Response

```json
    {
        "message": "Task 'Task Name' has been successfully processed by Python."
    }
```