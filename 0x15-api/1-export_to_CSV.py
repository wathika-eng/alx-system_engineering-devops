#!/usr/bin/python3
"""
API requests using Python
"""
import csv
import requests
import sys


def export_employee_todo_csv(employee_id):
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

    csv_filename = f"{employee_id}.csv"

    csv_data = []
    for task in todos_data:
        task_id = task["id"]
        task_title = task["title"]
        task_completed = task["completed"]
        csv_data.append([task_id, employee_name, task_completed, task_title])

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)

    print(f"CSV file '{csv_filename}' has been created.")


export_employee_todo_csv(sys.argv[1])
