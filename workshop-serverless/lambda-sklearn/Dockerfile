FROM public.ecr.aws/lambda/python:3.13

# Copy the 'uv' executables from the latest uv image into /bin/ in this image
# 'uv' is a fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
#RUN pip install uv

# Copy the project configuration files into the container
# pyproject.toml     → project metadata and dependencies
# uv.lock            → locked dependency versions (for reproducibility)
# ignore '.python-version'
COPY pyproject.toml uv.lock ./

# Install dependencies
# AWS needs only cannot recognize virtual environment
# uv export        ->   Export the project's lockfile
#                        (defaults to requirements.txt)
# uv pip install   ->   Install packages
#  --system        ->   Install into the system Python environment
#   -r             ->   Install the packages listed in 
#                       requirements.txt
RUN uv pip install --system -r <(uv export --format requirements.txt)

# Copy application code and model data into the container
COPY lambda_function.py model.bin ./

CMD ["lambda_function.lambda_handler"]
