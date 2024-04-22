# http_client

This repository contains a simple HTTP client implemented in Python using sockets. It allows you to make HTTP GET requests to a specified server and port.

## Usage
1. Clone the repository: git clone https://github.com/your-username/simple-http-client


2. Navigate to the repository directory


3. Run the Python script: python3 http_client.py


Follow the instructions in the script to enter the server hostname or IP address, as well as the port number.

# http_request Example

This Python script demonstrates how to make an HTTP request using the `urllib3` library.

## Usage

1. Ensure you have Python installed on your system.
2. Install the `urllib3` library if you haven't already:

    ```
    pip install urllib3
    ```

3. Run the script using the following command:

    ```
    python3 http_request_example.py
    ```

4. The script will make a GET request to `http://www.google.com` and print the response data.

## Dependencies

- Python 3.x
- urllib3

# HTTP Request without Proxy

This Python script demonstrates how to make HTTP requests without using a proxy server. It uses the `urllib3` library to send a GET request to a specified URL.

## Prerequisites

- Python 3.x
- urllib3 library (install using `pip install urllib3`)

## Usage

1. Make sure you have Python installed on your system.
2. Install the urllib3 library by running `pip install urllib3`.
3. Replace `<USER AGENT>` with your desired user agent in the script.
4. Run the script using Python: `python http_request_no_proxy.py`.

# Simple HTTP Client

This project demonstrates how to use Python to perform HTTP requests using the `urllib3` library. It includes examples of making basic HTTP requests, handling proxies, and extracting links from HTML content.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/simple-http-client.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd simple-http-client
    ```

2. Run the desired Python script:

    ```bash
    python basic_http_request.py
    ```

    Replace `basic_http_request.py` with the name of the script you want to execute.

## Scripts

- `basic_http_request.py`: Demonstrates how to make a basic HTTP request.
- `proxy_http_request.py`: Shows how to make an HTTP request through a proxy.
- `extract_links_from_html.py`: Illustrates how to extract links from HTML content fetched via HTTP.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.