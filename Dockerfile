FROM python:3.12
RUN mkdir url_shortener
WORKDIR /url_shortener
COPY /pyproject.toml /url_shortener
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]

