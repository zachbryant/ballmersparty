FROM alpine
RUN apk add --no-cache bash
RUN apk add --no-cache python3
COPY problems problems
COPY test_runner.sh test_runner.sh
COPY submissions/submission.py submission.py
CMD bash test_runner.sh $problem submission.py