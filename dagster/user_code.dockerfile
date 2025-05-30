FROM python:3.7-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance

# RUN pip install \
#     dagster \
#     dagster-postgres \
#     dagster-docker \
#     dagster-airbyte \
#     python-dotenv

# Add repository code

WORKDIR /opt/dagster/app

COPY ["./requirements.txt", "/opt/dagster/app"]

RUN pip install -r requirements.txt
RUN pip install "pydantic<2.0.0"

COPY [".", "/opt/dagster/app"]

# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "--package-name", "repository_like_module"]