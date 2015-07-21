FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mnemonic.settings
RUN mkdir /MaaS
WORKDIR /MaaS
ADD . /MaaS/
RUN pip install -r requirements.txt
RUN python setup.py install
RUN django-admin.py syncdb
EXPOSE 8000
CMD ./docker_entry.sh

