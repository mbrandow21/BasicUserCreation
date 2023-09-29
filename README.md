# Flask User Registration & Login

A simple Flask application that allows users to register and log in. The application utilizes a SQL Server backend and integrates with GitHub.

## Setup & Installation

### Prerequisites

- Python
- Flask
- pyodbc
- bcrypt
- A SQL Server instance

### Configuration

1. Ensure you have a `.env` file in your project root with the following variables:

\```
CONNECTION_USERNAME=your_username
SECRET_KEY=your_secret_key
\```

Replace `your_username` and `your_secret_key` with your database connection details.

2. Install the required Python packages:

\```
pip install Flask pyodbc bcrypt python-dotenv
\```

## Usage

To run the application, navigate to the project directory in the terminal and execute:

\```
python app.py
\```

Visit `http://127.0.0.1:5000/` in your browser to access the application.

## Features

- User registration with hashed password storage.
- User login with password verification.
- SQL Server integration for storing user data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
