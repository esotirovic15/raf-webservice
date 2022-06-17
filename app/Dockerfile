FROM python:alpine
WORKDIR ./
COPY app.py ./
RUN pip install flask
EXPOSE 8081
CMD [ "python", "app.py" ]