FROM jenkins/jenkins:lts

USER root

# 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y git docker.io

# 호스트의 docker 그룹의 GID를 가져옵니다.
ARG DOCKER_GID=999
RUN groupadd -g ${DOCKER_GID} docker && \
    usermod -aG docker jenkins

# Jenkins 플러그인 설치
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin docker-workflow

USER jenkins
