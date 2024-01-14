# product-catalog-project

---

# product-catalog with basic authentication

Develop a RESTful service for a product catalog with basic user authentication.
- Create API endpoints to register a user, list products, add a new product, and get product details.
- Use a SQL database (any of the candidate’s choice) for user data.
- Use a NoSQL database (any of the candidate’s choice) for product data.
- Containerize the application and databases using Docker.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Python: [Install Python](https://www.python.org/downloads/)

### Running the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/kushpal/product-catalog-project.git
   cd finkartProduct
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker image from the provided `Dockerfile` and start the containers defined in the `docker-compose.yml` file.

3. Access the application

   Once the containers are up and running, you can access the application in your browser at [http://localhost:5001](http://localhost:5001).

## Configuration

The project uses environment variables for configuration. You can customize the environment variables in the `docker-compose.yml` file.

- `MONGO_URI`: MongoDB connection URI.
- `SQLALCHEMY_DATABASE_URI`: SQLAlchemy database URI.

## Project Structure

The project is organized into the following structure:

- **app**: Contains your application code.
- **requirements.txt**: Lists the Python dependencies for your project.
- **Dockerfile**: Defines the Docker image for your application.
- **docker-compose.yml**: Configures Docker services.

## Contributing

If you would like to contribute to the project, please follow the standard GitHub flow:

1. Fork the project.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.
