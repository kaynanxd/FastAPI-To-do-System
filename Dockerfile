FROM python:3.13-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY . .

RUN uv pip install --system --no-cache .

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "backend.app:app"]