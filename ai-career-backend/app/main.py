from app.api_client import APIClient

def main():
    client = APIClient()

    try:
        result = client.get_data("example-endpoint")
        print("GET result:", result)
    except Exception as e:
        print("Error:", e)
    

    try:
        payload = {"key": "value"}
        result = client.post_data("example-endpoint", payload)
        print("POST result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()