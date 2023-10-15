FROM python:3-alpine
LABEL authors="emiliano"

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-emilianomassolin
WORKDIR /scrabble-2023-emilianomassolin
RUN git checkout dev
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m main" ]