FROM alpine
RUN  apk add --update --no-cache g++ python python-dev make curl py-pip && rm -rf /var/cache/apk/*
RUN pip install Flask
RUN mkdir /pdfPlotter /pdfPlotter/pdfServer
WORKDIR /pdfPlotter
COPY installLHA.sh  /pdfPlotter/
RUN ./installLHA.sh
COPY pdfServer /pdfPlotter/pdfServer
WORKDIR /pdfPlotter/pdfServer

EXPOSE 5000

CMD ["/bin/sh", "runFlask.sh"]
