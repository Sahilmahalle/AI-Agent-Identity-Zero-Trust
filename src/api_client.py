import requests


BASE_URL = "http://127.0.0.1:8000"


def check_health():
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    response.raise_for_status()
    return response.json()


def get_agent_info():
    response = requests.get(f"{BASE_URL}/agent", timeout=5)
    response.raise_for_status()
    return response.json()


def send_echo_message(message: str):
    response = requests.post(
        f"{BASE_URL}/echo",
        json={"message": message},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("Health response:")
    print(check_health())

    print("\nAgent response:")
    print(get_agent_info())

    print("\nEcho response:")
    print(send_echo_message("Milestone 1 API client test"))