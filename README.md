# HTTP Client

This repository contains a simple HTTP client implemented in Python using sockets. It allows you to make HTTP GET requests to a specified server and port.

## Table of Contents
- [HTTP Client](#http-client)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
- [HTTP Request Example](#http-request-example)
  - [Usage](#usage-1)
  - [Dependencies](#dependencies)
- [HTTP Request without Proxy](#http-request-without-proxy)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage-2)
- [Simple HTTP Client](#simple-http-client)
  - [Installation](#installation)
  - [Usage](#usage-3)
  - [Scripts](#scripts)
- [XPath Demo](#xpath-demo)
  - [Script](#script)
  - [Usage](#usage-4)
  - [Dependencies](#dependencies-1)
  - [Contributing](#contributing)
  - [License](#license)

## Usage
1. Clone the repository:
git clone https://github.com/your-username/simple-http-client

markdown
Copy code

2. Navigate to the repository directory

3. Run the Python script:
python3 http_client.py

markdown
Copy code
Follow the instructions in the script to enter the server hostname or IP address, as well as the port number.

# HTTP Request Example

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

# XPath Demo

This repository contains a Python script demonstrating the power of XPath for extracting links from HTML content fetched via HTTP.

## Script

xpath_demo.py: This script illustrates how to use XPath to extract links from HTML content obtained through an HTTP request.

## Usage

Ensure you have Python installed on your system.
Install the required dependencies using pip install -r requirements.txt.
Run the script using python xpath_demo.py.
The script will make an HTTP request to fetch HTML content from a webpage and then extract and print the links using XPath.

## Dependencies

Python 3.x
lxml library

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) f