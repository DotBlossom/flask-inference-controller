FROM python:3.9

# 빌드 시에 MongoDB 연결 정보를 전달받을 ARG 변수 정의
ARG MONGO_URL

# 환경 변수 설정
ENV MONGO_URL=$MONGO_URL

