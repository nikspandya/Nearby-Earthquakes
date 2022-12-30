FROM python:3.8-buster

COPY . /main

WORKDIR /main

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

EXPOSE 8610

CMD ["controller.py"]
