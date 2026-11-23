# Iris Full-Stack Classifier

- **Description:** Extend the FastAPI Iris classifier with a web UI and PostgreSQL inference logging, all runnable with Docker Compose.
- **Inputs:** Sepal length, sepal width, petal length, and petal width in centimetres.
- **Classes:** Setosa, versicolor, and virginica.

## Assignment

- Create a `ui/` directory with a Streamlit app for entering the four measurements.
- Send the measurements from the UI to the API's `POST /predict` endpoint and display the predicted species.
- Add a `ui/Dockerfile` to build and run the Streamlit app.
- Add a root-level `compose.yaml` with services for the API, UI, and PostgreSQL.
- Use the lightweight official PostgreSQL image `postgres:16-alpine` and configure a persistent data volume.
- Create `api/.env` with a `DATABASE_URL` for the Compose PostgreSQL service, for example:
  `DATABASE_URL=postgresql://postgres:postgres@db:5432/iris`
- Keep the database name, user, and password consistent between `api/.env` and the Compose PostgreSQL settings.
- Configure the UI to call the API at `http://api:8000` from inside Compose; use the Compose service name, not `localhost`.
- Start the full stack from the project root with `docker compose up --build`.
- Verify the UI prediction, API docs at `http://localhost:8000/docs`, and inference records in PostgreSQL.

## Run the full stack

Create `api/.env` with the database URL (it is not committed):

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/iris
```

Then from the project root:

```powershell
docker compose up --build
```

- UI: <http://localhost:8501>
- API docs: <http://localhost:8000/docs>

Check the logged inferences in PostgreSQL:

```powershell
docker compose exec db psql -U postgres -d iris -c "SELECT * FROM inferences;"
```

Predictions are stored in the `pgdata` volume, so they persist across
`docker compose down` and `up`. Use `docker compose down -v` to wipe them.
