FROM python:3

WORKDIR /fetch-rewards

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]