# a473a907-03bd-4ac9-a9b7-00619ab81a32
# Python Calculator API

This is a simple calculator API built with Python and FastAPI.

## Endpoints

*   `/`: Welcome message
*   `/plus?a=<num>&b=<num>`: Adds two numbers
*   `/minus?a=<num>&b=<num>`: Subtracts two numbers
*   `/times?a=<num>&b=<num>`: Multiplies two numbers
*   `/division?a=<num>&b=<num>`: Divides two numbers

## How to run locally

1.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

2.  Run the application:
    ```
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

## Deployment on Render

For Render, you can use the following settings:

*   **Build Command:** `pip install -r requirements.txt`
*   **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 8000`
