FROM python:3

WORKDIR /assignmenttwo

ADD main.py .

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
EXPOSE 5000

CMD ["python", "main.py"]