FROM alpine
RUN apk add --no-cache bash
RUN apk add --no-cache python3
COPY problems problems
COPY test_runner.sh test_runner.sh
CMD bash test_runner.sh clockDelay