# Metaline

**Metaline** is a lightweight Python package designed to provide simple, efficient access to database table metadata. It supports **MySQL**, **PostgreSQL**, and **MSSQL** databases, allowing users to retrieve table schema information using just a database connection string.

## Features

- **Retrieve Metadata**: Get essential details about each table column, such as names, data types, nullability, and default values.
- **Multi-Database Support**: Compatible with MySQL, PostgreSQL, and MSSQL.
- **User-Friendly API**: A straightforward function for quick and easy integration into any Python project.

## Installation

You can install *Metaline* directly from PyPI (coming soon) or clone it locally.

### Local Installation

Clone the repository and navigate to the `metaline` directory, then install it in editable mode:

`pip install -e`

## Requirements

- Python 3.6+
- [SQLAlchemy](https://www.sqlalchemy.org/) - For managing database connections.
- Database connectors:
  - **MySQL**: `pymysql`
  - **PostgreSQL**: `psycopg2`
  - **MSSQL**: `pyodbc`

Install dependencies via pip:

`pip install sqlalchemy pymysql psycopg2 pyodbc`

## Usage
To retrieve metadata for a table, use the get_metadata function from Metaline. You need to provide:

*A database connection string.
*The name of the table you want metadata for.

### Try It Out
You can use the code in `Tests` folder to try out the library.

## Supported Databases

Metaline currently supports the following databases:
- **MySQL** (via `pymysql`)
- **PostgreSQL** (via `psycopg2`)
- **MSSQL** (via `pyodbc`)

Make sure to install the appropriate database connector for your target database(s).

---

## Contributing

Contributions are welcome! If you’d like to contribute to *Metaline*, feel free to open an issue or submit a pull request on the GitHub repository.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/NewFeature`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to your branch (`git push origin feature/NewFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

