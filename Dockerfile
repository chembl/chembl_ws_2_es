FROM python:3.7.10-slim-buster
ARG USERNAME=${USERNAME:-chembl_user}
ARG UID=${UID:-123}
ARG GID=${GID:-321}
ARG WORKDIR=${WORKDIR:-/chembl-ws-2-es}

# setup user and app root directory
RUN useradd -m ${USERNAME} -u ${UID}
RUN mkdir -p ${WORKDIR}
RUN chown -R ${UID}:${GID} ${WORKDIR}
WORKDIR ${WORKDIR}

# setup gunicorn log and pid folder
RUN mkdir ${WORKDIR}/gunicorn
RUN chown -R ${UID}:${GID} ${WORKDIR}/gunicorn

# setup data folder
RUN mkdir ${WORKDIR}/data
RUN chown -R ${UID}:${GID} ${WORKDIR}/data

# revents Python from writing pyc files to disc and from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# use the environment.yml to create the conda env
COPY requirements.txt /tmp/requirements.txt

# create the conda env using saved environment file
RUN pip install -r /tmp/requirements.txt

# activate env (add conda env bin to path)
ENV PATH /opt/conda/envs/chembl-webservices-py3/bin:$PATH

# copy ws2es code
COPY src src
COPY *.py ./

ENTRYPOINT [ "/bin/bash" ]