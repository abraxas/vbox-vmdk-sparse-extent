FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LABEL=vbox-vmdk-sparse-extent \
    WITNESS=VBOX-VMDK-SPARSE-EXTENT-WITNESS

WORKDIR /lab

RUN mkdir -p /work/import/disk /work/oracle /lab

COPY poc.py /lab/poc.py

RUN chmod 0755 /lab/poc.py

CMD ["python3", "-c", "import time; time.sleep(10**9)"]
