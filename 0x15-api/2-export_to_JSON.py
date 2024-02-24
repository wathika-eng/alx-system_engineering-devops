#!/usr/bin/python3
"""
API requests using Python
"""
import json
import requests
import sys


def export_to_JSON(employee_id):
    """
    Retrieves information about an employee's TODO list from a REST API and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: The function creates a CSV file with the employee's TODO list data.

    Raises:
        requests.exceptions.RequestException: If there is an error in making the API request.

    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data["username"]

    response = requests.get(todos_url)
    todos_data = response.json()

    json_filename = f"{employee_id}.json"

    data = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name,
            }
            for task in todos_data
        ]
    }

    with open(json_filename, mode="w", newline="") as file:
        json.dump(data, file)

    print(f"JSON file '{json_filename}' has been created.")


if __name__ == "__main__":
    export_to_JSON(sys.argv[1])
