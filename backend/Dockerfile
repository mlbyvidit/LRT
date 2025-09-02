FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Copy CSV files for data loading
COPY ../carrier_samples.csv ./
COPY ../shippers_sample.csv ./
COPY ../postal_codes.csv ./
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]