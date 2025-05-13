# Pixela Habit Tracker Script

This Python script interacts with the **Pixela API** and was developed as part of **The 100 Days of Code: The Complete Python Pro Bootcamp** course by **Angela Yu**.

It provides functionality to programmatically manage your Pixela habit tracking graphs and data points.

## Features

This script includes code for the following Pixela API operations:

* **User Creation:** (Currently commented out) Creates a new Pixela user account.
* **Graph Creation:** (Currently commented out) Defines a new graph within your Pixela user account.
* **Pixel Posting:** (Currently commented out) Adds a data point (pixel) to a specific graph for a given date and quantity.
* **Pixel Deletion:** (Currently **active**) Deletes a data point (pixel) from a specific graph for the current date.

## Prerequisites

Before running this script, you need:

* **Python 3.x**
* **Required Python Libraries:**
    * `requests`
    * `python-dotenv`
    You can install them using pip:
    ```bash
    pip install requests python-dotenv
    ```
* **A Pixela Account:** You need a Pixela user account. If you don't have one, you can create one using the commented-out code in the script or via the Pixela website/documentation.
* **Your Pixela User Token:** The secret token generated when you create your Pixela user.
* **Your Pixela Username:** The username you chose for your Pixela account.
* **A Pixela Graph ID:** An ID for a graph you have created (or will create using the script).

## Setup

1.  **Save the script:** Save the provided Python code as a `.py` file (e.g., `pixela_script.py`).
2.  **Create a `.env` file:** In the same directory as your script, create a file named exactly `.env`. Add your Pixela credentials here:
    ```dotenv
    # .env file

    # Pixela API Credentials
    TOKEN=YOUR_PIXELA_USER_TOKEN
    MYNAME=YOUR_PIXELA_USERNAME
    ```
    Replace `YOUR_PIXELA_USER_TOKEN` and `YOUR_PIXELA_USERNAME` with your actual Pixela credentials.

3.  **Set the Graph ID:** In the Python script, ensure the `GRAPH_ID` variable is set to the ID of the graph you want to interact with (e.g., `GRAPH_ID = "graph1"`).

## How to Run

1.  Ensure the script file and `.env` file are in the same directory.
2.  Open your terminal or command prompt and navigate to that directory.
3.  Run the script:
    ```bash
    python pixela_script.py
    ```

By default, the script will attempt to **delete** a pixel for the current date on the specified graph using your credentials.

## How to Use Different Operations

The script contains code for creating users, graphs, and posting pixels, but they are commented out. To use them:

1.  **Uncomment the relevant section of code.** For example, to create a user, remove the `#` symbols before the `params = {...}` dictionary and the `response = requests.post(...)` call for user creation.
2.  **Comment out the sections you *don't* want to run.** To avoid unintended actions, make sure only the API call you intend to make is active (uncommented) when you run the script.
3.  **Adjust parameters/data:** Modify the dictionaries (`params`, `data`, `graph_entry`, `graph_update_entry`) with the specific details you need for that operation (e.g., new graph name, different quantity, specific date for posting/updating/deleting).

## Troubleshooting

* **API Errors:** Pixela API responses often include helpful messages in the text output. Read these carefully if a request fails. Common issues include:
    * **Incorrect Token:** Ensure your `TOKEN` in `.env` is correct and the `X-USER-TOKEN` header is exactly right.
    * **Incorrect Username/Graph ID:** Verify `MYNAME` and `GRAPH_ID` in your script.
    * **Incorrect URL or Method:** Double-check the URL structure and that you're using the correct `requests` method (`.post()`, `.put()`, `.delete()`).
    * **Incorrect Payload:** Ensure the JSON data sent (`json=...`) matches the Pixela API documentation for the specific endpoint and method you are using. (Remember, DELETE doesn't use `json=`).
    * **Missing or Invalid Required Parameters:** Check that all necessary parameters are included in the URL, headers, or payload as required by the API.

## Acknowledgements

This script was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp** on Udemy, instructed by **Angela Yu**.
It also interacts with the [Pixela API](https://pixe.la/).

## Future Improvements

* Implement a command-line interface to choose which operation to perform.
* Add functionality for updating pixels (`PUT` request).
* Improve error handling.

---

