FROM python:3.12-slim

RUN useradd --system --uid 10001 --no-create-home appuser

WORKDIR /app
COPY app.py .

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

USER 10001
CMD ["python", "app.py"]