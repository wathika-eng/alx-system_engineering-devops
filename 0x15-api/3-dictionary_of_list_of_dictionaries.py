#!/usr/bin/python3
"""
API requests using Python
"""
import json
import requests


def export_to_JSON():
    """
    Retrieves information about employees' TODO lists from a REST API and exports it to a JSON file.

    Returns:
        None: The function creates a JSON file with the TODO list data for all employees.

    Raises:
        requests.exceptions.RequestException: If there is an error in making the API request.

    """
    base_url = "https://jsonplaceholder.typicode.com"
    employees_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    response = requests.get(employees_url)
    employees_data = response.json()

    response = requests.get(todos_url)
    todos_data = response.json()

    json_filename = "todo_all_employees.json"

    data = {}
    for employee in employees_data:
        employee_id = employee["id"]
        employee_name = employee["username"]
        employee_tasks = [
            {
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos_data
            if task["userId"] == employee_id
        ]
        data[employee_id] = employee_tasks

    with open(json_filename, mode="w") as file:
        json.dump(data, file)

    print(f"JSON file '{json_filename}' has been created.")


export_to_JSON()
