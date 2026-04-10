import requests
import pandas as pd
import matplotlib.pyplot as plt
import logging

# লগging setup
logging.basicConfig(
    filename="app_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = "5589e759"
BASE_URL = "https://www.omdbapi.com/"

def fetch_movies(search_term, timeout=5, max_retries=1):
    params = {
        "apikey": API_KEY,
        "s": search_term
    }

    attempt = 0

    while attempt <= max_retries:
        try:
            response = requests.get(BASE_URL, params=params, timeout=timeout)

            # Status code check
            if response.status_code == 200:
                data = response.json()

                # OMDb-specific error check
                if data.get("Response") == "False":
                    msg = f"OMDb error for '{search_term}': {data.get('Error')}"
                    print(msg)
                    logging.error(msg)
                    return None

                return data

            else:
                msg = f"HTTP {response.status_code} error for '{search_term}'"
                print(msg)
                logging.error(msg)

            response.raise_for_status()

        except requests.exceptions.Timeout:
            msg = f"Timeout on attempt {attempt + 1} for '{search_term}'"
            print(msg)
            logging.error(msg)

            if attempt < max_retries:
                print("Retrying...")
                attempt += 1
                continue
            else:
                print("Max retries reached.")
                return None

        except requests.exceptions.RequestException as e:
            msg = f"Request failed for '{search_term}': {e}"
            print(msg)
            logging.error(msg)
            return None

        break

    return None
