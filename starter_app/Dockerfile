FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src

RUN python -m pip install --upgrade pip && python -m pip install .

ENV OPPORTUNITY_DB_PATH=/data/opportunities.db
RUN mkdir -p /data

EXPOSE 8000

CMD ["uvicorn", "opportunity_tracker.app:app", "--host", "0.0.0.0", "--port", "8000"]
