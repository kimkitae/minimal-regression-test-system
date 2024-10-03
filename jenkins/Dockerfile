# Jenkins LTS 이미지를 기반으로 함
FROM jenkins/jenkins:lts

# root 권한으로 전환
USER root

# 필요한 패키지 설치 (예: git, docker 클라이언트 등)
RUN apt-get update && \
    apt-get install -y git docker.io

# Docker를 실행하기 위한 설정
RUN usermod -aG docker jenkins

# Jenkins 플러그인 설치 (예: Allure 플러그인)
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:latest docker-workflow

USER jenkins
