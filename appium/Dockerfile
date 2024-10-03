FROM appium/appium:latest

# 필요한 Appium 드라이버 설치
RUN appium driver install uiautomator2 || true
# 필요에 따라 다른 드라이버나 플러그인 설치
# 예: RUN appium driver install xcuitest

# 기본 명령어 유지
CMD ["appium"]
