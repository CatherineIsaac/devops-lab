FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --system appgroup \
    && useradd --system --gid appgroup appuser

COPY --chown=appuser:appgroup app.py .

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
