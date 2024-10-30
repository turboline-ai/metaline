from setuptools import setup, find_packages

setup(
    name="metaline",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "pymysql",      # MySQL support
        "psycopg2",     # PostgreSQL support
        "pyodbc"        # MSSQL support
    ],
    description="A lightweight package for fetching database table metadata",
    author="Turboline",
    author_email="dev@turboline.ai",
    url="https://github.com/turboline-ai/metaline",
)
