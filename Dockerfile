FROM debian:jessie-slim
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

# install required ubuntu packages
RUN apt-get update --fix-missing && apt-get upgrade &&\
    apt-get install -y --no-install-recommends wget build-essential checkinstall && \
    apt-get install -y --no-install-recommends libreadline-gplv2-dev libncursesw5-dev libssl-dev \
      libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log

# Install python 3.7
RUN cd /usr/src && wget --no-check-certificate https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz

RUN cd /usr/src && tar xzf Python-3.7.9.tgz

RUN cd /usr/src/Python-3.7.9 && ./configure --enable-optimizations && make install

RUN python -v

# use the environment.yml to create the conda env
COPY requirements.txt /tmp/requirements.txt

# create the conda env using saved environment file
RUN pip install -r /tmp/requirements.txt

# activate env (add conda env bin to path)
ENV PATH /opt/conda/envs/chembl-webservices-py3/bin:$PATH

# copy ws2es code
COPY src src
COPY cluster_replicator.py cluster_replicator.py

ENTRYPOINT [ "/bin/bash" ]