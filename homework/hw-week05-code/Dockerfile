FROM agrigorev/zoomcamp-model:2025

RUN mkdir data; mv pipeline_v2.bin data/hw5-pipeline.bin; cd ../; mv code app

# Set the working directory inside the container to /app
# All subsequent commands will be run from here
WORKDIR /app


# Copy the 'uv' and 'uvx' executables from the latest uv image into /bin/ in this image
# 'uv' is a fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#RUN pip install uv

# Set the working directory inside the container to /app
# All subsequent commands will be run from here
#WORKDIR /app

# Add the virtual environment's bin directory to the PATH so Python tools work globally
ENV PATH="/app/.venv/bin:$PATH"

# Copy the project configuration files into the container
# pyproject.toml     → project metadata and dependencies
# uv.lock            → locked dependency versions (for reproducibility)
# .python-version    → Python version specification
COPY ".python-version" "pyproject.toml"  "uv.lock" ./

# Install dependencies exactly as locked in uv.lock, without updating them
RUN uv sync --locked

# Copy application code and model data into the container
COPY "predict_application.py" "data/hw5-pipeline.bin" ./

# Expose TCP port 9696 so it can be accessed from outside the container
EXPOSE 9696

# Run the application using uvicorn (ASGI server)
# churn_application:app → refers to 'app' object inside churn_application.py
# --host 0.0.0.0 → listen on all interfaces
# --port 9696    → listen on port 9696
ENTRYPOINT ["uvicorn", "predict_application:app", "--host", "0.0.0.0", "--port", "9696"]