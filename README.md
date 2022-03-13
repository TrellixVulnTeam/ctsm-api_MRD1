## Setup and Run the Dev Server

To run the services locally or with docker, first you need to create a `.env` file in your project root directory.
You can use `env-example` as a template and adjust the variables accordingly. See the `Variable` section below for more information.

### Run locally
> We recommend using a virtual environment for your project.
>
> You can either use [Conda](https://docs.conda.io/en/latest/) or [Python venv](https://docs.python.org/3/library/venv.html) to create a virtual environment.

- Make sure [Poetry](https://python-poetry.org/) is installed in your environment.
- Install the dependencies: `poetry install`.
- Set up the database: `./scripts/migrations_forward.sh`.
- Set up CTSM repo: `./scripts/setup_ctsm.sh`.
- Run the dev server: `./scripts/run_dev_server.sh`.

### Run in Docker

> Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) first.
>
> The current configs and commands are tested with docker 20.10.13 and docker-compose 1.29.2.

- To build the image locally, run `docker-compose -f docker-compose.dev.yaml build`.
- To run the docker services in debug mode, run `docker-compose -f docker-compose.dev.yaml up`.
- For production, run `docker-compose up`.

In order to avoid permission issues on folders handled by docker,
you can set `HOST_USER` and `HOST_UID` vars to their respective values for the host user under which you are running the docker commands.

You can do this either in your `.env` file or by exporting them in your environment.
THe following command is an example of how to set the variables:
`HOST_USER=$(whoami) HOST_UID=$(id -u) docker-compose -f docker-compose.dev.yaml up`

### Variables

#### Adjustable Variables in `.env`:

|    Variable    | Required |                                                                                    Description                                                                                     |             Default             | Scope  |
|:--------------:|:--------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------:|--------|
|   CTSM_REPO    |    No    |                                                                             The CTSM repository to use                                                                             | https://github.com/ESCOMP/CTSM/ | API    |
|    CTSM_TAG    |   Yes    |                                                                           The CTSM repository tag to use                                                                           |                -                | API    |
|  CESMDATAROOT  |    No    |                                                                 The relative or absolute path to CESM data folder                                                                  |        ./resources/data         | API    |
|   SQLITE_DB    |    No    |             The path to the SQLite file to use<br/>If the file doesn't exist, it will be created at the given path<br/>The default DB will be created in project root              |          cases.sqlite           | API    |
| SQLITE_DB_TEST |    No    |                                                                         Same as SQLITE_DB, but for testing                                                                         |        cases_test.sqlite        | API    |
|     DEBUG      |    No    |                                             Set `DEBUG` state, which is used for adjusting logging level and other debugging purposes                                              |              False              | API    |
|      PORT      |    No    |                                                                     The port to use for API service in docker                                                                      |              8000               | Docker |
|   HOST_USER    |    No    |  Docker host user. If specified for a docker container, ownership of all folders within `resources` will be changed to the container host user<br/>It must be used with HOST_UID   |                -                | Docker |
|    HOST_UID    |    No    |                                                 UID of docker host user. See `HOST_ID` above and the docker section for more info                                                  |                -                | Docker |
