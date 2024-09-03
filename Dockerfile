FROM python:3

## testing rules

ADD get_web.py /

RUN pip install pystrich

RUN pip install requests 

RUN pip install time

CMD [ "python", "./my_script.py" ]
