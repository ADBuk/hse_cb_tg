FROM python:3.10
RUN echo 'Build is launched'

WORKDIR /root/docker_cb

COPY poetry.lock pyproject.toml ./ 

RUN python -m pip install --no-cache-dir poetry==1.4.2 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev,test --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}


COPY . /root/docker_cb
CMD ["python", "main.py"] 
