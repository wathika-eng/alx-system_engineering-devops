#!/usr/bin/python3
"""
API requests using Python
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves information about an employee's TODO list progress from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: The function prints the employee's TODO list progress to the standard output.

    Raises:
        requests.exceptions.RequestException: If there is an error in making the API request.

    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data["name"]

    response = requests.get(todos_url)
    todos_data = response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task["completed"]]
    num_done_tasks = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    """Run only when called by name"""
    get_employee_todo_progress(sys.argv[1])
