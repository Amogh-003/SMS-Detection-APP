FROM python:3.10.13-bullseye

# Fix CVE-prone config directories
ENV MPLCONFIGDIR=/tmp/mpl
ENV TMPDIR=/tmp
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

# Ensure pip, setuptools, and wheel are updated
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]