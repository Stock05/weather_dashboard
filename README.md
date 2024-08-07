# 날씨 대시보드

날씨 대시보드는 OpenWeatherMap API를 사용하여 사용자 지정 위치에 대한 실시간 날씨 정보를 제공하는 웹 애플리케이션입니다.
이 프로젝트는 위도와 경도 또는 주소를 기준으로 사용자가 원하는 지역의 날씨 데이터를 표와 그래프로 표시합니다.

## 기능

- **실시간 날씨 데이터**: 주어진 위치에 대한 날씨 정보를 가져옴
- **그래픽 표현**: 바 그래프로 날씨 데이터 시각화
- **사용자 위치 입력**: 사용자가 주소를 입력하여 특정 위치의 날씨 정보를 조회 가능
- **기본 위치**: 기본적으로 서울의 날씨 데이터를 표시

## 페이지

1. **메인 페이지**: 
   - 서울의 날씨 데이터를 DataFrame으로 표시
   - 서울의 날씨 데이터를 그래픽으로 표현
   ![alt text](image.png)

2. **그래프 페이지**: 
   - 서울의 날씨 데이터를 바 그래프로 표시
   - 사용자가 특정 날씨 속성을 선택하여 맞춤형 그래프 생성
   ![alt text](image-1.png)

3. **커스텀 페이지**: 
   - 사용자가 주소를 입력하여 날씨 데이터를 조회하고 표시
   - 지정된 위치의 DataFrame 및 그래픽 표현
   ![alt text](image-2.png)
   ![alt text](image-3.png)
