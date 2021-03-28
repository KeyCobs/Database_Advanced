#We create a base image.
FROM python:3.8

ADD scraping.py3 .

CMD ["python" ,"scraping.py3"]


