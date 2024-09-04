FROM python:3

## testing rules

## more testing on wednesday, tims my friend 

ADD get_web.py /

RUN pip install pystrich

RUN pip install requests 

RUN pip install time

CMD [ "python", "./my_script.py" ]
