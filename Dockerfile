FROM python:3.7.2

WORKDIR /FlaskBlogServer

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./main.py