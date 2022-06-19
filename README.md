<br>

# 🛰 도로정찰대 : 위성사진 기반 도시 정비 인공지능 서비스
> 2022.05.23 ~ 2022.05.13<br>
>  *'도로정찰대'는 AI로 위성사진 상 도로 차선의 부실한 도색을 인식해 도로 정비를 돕는 디지털 서비스입니다*
<img src="https://user-images.githubusercontent.com/37900424/174465736-cfb7e461-316c-4b9b-8066-9a7ca7c2dbde.png" width="1000" height="352">

## 팀원 소개
- `[K-Digital Training] KT AIVLE SCHOOL 수료생`
> 김나래(팀장), 권윤경, 김보연, 손현우, 안세영, 이원호


## 목차
[1. 개발 배경 및 목적](#1-개발-배경-및-목적)

[2. 기능](#2-기능-및-UI/UX)

[3. 서비스 FLOW](#3-서비스-FLOW)

[4. 3 Tier Architecture](#4-3-Tier-Architecture)

[5. DB 설계](#5-DB-설계)

[6. 개발 환경](#6-개발-환경)

[7. 유저 가이드](#7-유저-)

***

## 1. 개발 배경 및 목적
> 💡 **'위성사진과 AI기술을 통해 안전하고 편리한 도로 환경 조성을 위해 개발하게 되었다.'** 현재 차선 노후화에 대한 지속적인 미원이 발생하고 있고, 이로 인한 사고 위험 증가와 도시 미관 저해 문제 등의 여러 이슈가 있다. 하지만, 노후 차선을 정비하기 위한 처리 과정 전부가 수작업으로 진행되고 있어서 인력 자원이 많이 투입되고 있다. 즉, 차선 보수에 필요한 금액에 비해서 정해진 예산이 턱업이 부족한 상황이다. 우리는 도로정찰대를 통해 훼손 차선 탐색 프로세스 자동화를 도입해 효율적 예산 집행으로 현 무제점을 개선할 것이다.
<br>

#### 차선 노후화에 대한 지속적인 민원 발생
- `기존 보수 현황`
    - 도로교통안전점검 계획부터 점거반 구성, 차선 육안 조사, 결과 분석 및 보고 까지 전 과정을 수작업으로 처리 
    - 차선 보수 예산 부족
    
- `As-Is`
    - [1단계] 차선점검계획 수립
    - [2단계] 자료준비 및 점검인력 구성
    - [3단계] 차선 점검 실시
    - [4단계] 결과 분석·보고
    - [5단계] 정비·보수 
<br>

#### 위와 같은 사항을 **보완**하기 위해 **도로정찰대**를 기획
- `To-Be`
    - [1단계] 위성사진과 AI를 활용한 도시 정비 웹서비스
    - [2단계] 결과 분석·보고
    - [3단계] 정비·보수
<br>

<br>

## 2. 기능 및 UI/UX
- `서비스 주요 기능`

<details>
  <summary>메인 화면</summary>
   <div markdown="1">       
     <br>
     <img src="https://user-images.githubusercontent.com/37900424/174467018-f37d26fe-3b21-409e-9b5d-dea2621ecb01.gif">
     <br>
     <text>⇒ 도로정찰대의 홈화면으로 회원가입과 로그인을 할 수 있는 버튼이 있다</text>
   </div>
 </details>

 <details>
    <summary><strong>1) 고객과 상담사를 위한 회원가입/로그인</strong></summary>
        <div markdown="1">  
            <h3>📝 회원가입</h3>
            <img src="https://user-images.githubusercontent.com/37900424/174467780-f2f42839-d1f2-458c-9527-582b938300df.png" width="700" height="412">
            <h3>🔒 로그인</h3>
            <img src="https://user-images.githubusercontent.com/37900424/174467802-bd815309-051e-4889-a2be-8fb69dca75f9.png" width="700" height="412">
        </div>
</details>
 
 <details>
  <summary><strong>2) 훼손 차선 위치 시각화</strong></summary>
   <div markdown="1"> 
    <br>      
     <img src="https://user-images.githubusercontent.com/37900424/174468478-f99a7bce-5950-4271-b960-314a7c6f7091.png" width="700" height="412">
     <br>
     <text>⇒ 제공 데이터: 훼손 도로 위치의 위도, 경도, 훼손 이미지, 인근 도로명 주소</text>
   </div>
 </details>
 
 <details>
  <summary><strong>3) 오정보 신고 하기</strong></summary>
   <div markdown="1">
     <br>      
     <img src="https://user-images.githubusercontent.com/37900424/174468695-62661211-70d1-4c40-8f33-9f63290297fe.png" width="700" height="412">
     <br>
      <text>⇒ 작성 내용: 수정 요청 내용, 오정보 증거 사진 업로드</text>
   </div>
 </details>
 
 <details>
  <summary><strong>4) 지도 위치 스크랩하기</strong></summary>
   <div markdown="1">  
   <br>     
     <img src="https://user-images.githubusercontent.com/37900424/174468770-863e0584-43f1-4f68-ad68-2367a0ca3144.png" width="700" height="412">
     <br>
     <text>⇒ 훼손 차선에 대해서 스크랩 기능을 통해 특정 훼손 마커를 다시보기가 가능</text>
   </div>
 </details>
 
 <br>

 - `AI 주요 기능`
 <details>
    <summary><strong>1) 훼손 도로 탐지 </strong></summary>
      <img src="https://user-images.githubusercontent.com/37900424/174469009-fd42ae28-2634-47d8-9d22-493780a8faa0.png" width="700" height="412"><br>
      <text>⇒ 2-stage Faster R-CNN 학습을 이용한 객체(훼손 도로) 탐지</text>
 </details>
 
  - `특별한 추가 기능`
 <details>
    <summary><strong>1) 스크랩 내용 엑셀 형식으로 변환 </strong></summary><br>
    <text>⇒ 훼손 차선에 대한 정보를 엑셀 형식으로 받아 실무에 사용해 서비스 완성도 UP!</text>
 </details>


<br>

<br>

## 3. 서비스 FLOW
  - `주요 기능 Flow`
![서비스흐름](https://user-images.githubusercontent.com/37900424/174466315-f1d32588-84f8-4c67-b7bb-1bf44e0305de.png)

  - `서비스 Flow`
![서비스 FLOW](https://user-images.githubusercontent.com/37900424/174466324-057d2f08-3539-4bc3-aea2-330e66810e9a.png)

<br>

## 4. 2 Tier Architecture
   - `2-Tier Architecture`
![서비스아키텍쳐](https://user-images.githubusercontent.com/37900424/174466455-ee55f7f7-18fb-4e4d-a7d8-940ca0720763.png)

<br>

## 5. DB 설계
  - `ERD`
![ERD](https://user-images.githubusercontent.com/37900424/174466403-579571a1-58db-4de7-bb6e-67d41857e1e5.png)



<br>

## 6. 개발 환경

- `Front-End`

  |HTML|CSS|JS|
  |:---:|:---:|:---:|
  |![html](https://user-images.githubusercontent.com/68097036/151471705-99458ff8-186c-435b-ac5c-f348fd836e40.png)|![css](https://user-images.githubusercontent.com/68097036/151471805-14e89a94-59e8-468f-8192-c10746b93896.png)|![js](https://user-images.githubusercontent.com/68097036/151471854-e0134a79-b7ef-4a0f-99fd-53e8ee5baf50.png)


- `Back-End`

  |Python|Django|PostgreSQL|
  |:---:|:---:|:---:|
  |![pngwing com](https://user-images.githubusercontent.com/68097036/151479684-a85d26d4-e79e-47c9-9023-bf6d92f57536.png)|![pngwing com (1)](https://user-images.githubusercontent.com/68097036/151466729-9cad0405-85ad-454e-815a-1a4fd065f8b7.png)|![pngwing com (2)](https://user-images.githubusercontent.com/68097036/151466853-2b56fd0f-3aa9-424e-b17b-1c7cd991ffbf.png)|


- `Etc`

  |VS Code|Microsoft Teams|GitHub|Notion|
  |:---:|:---:|:---:|:---:|
  |<img src="https://user-images.githubusercontent.com/68097036/151479933-01785e34-1283-4fca-a407-9fe284b50fa8.png" width="220" height="100">|![pngwing com (4)](https://user-images.githubusercontent.com/68097036/151467837-2cd89acd-2a92-45dd-b06b-e08e316b7695.png)|<img src="https://user-images.githubusercontent.com/68097036/151467910-0fda00cd-c08b-4869-a21e-a66d1d133ff5.png" width="220" height="100">|<img src="https://user-images.githubusercontent.com/68097036/151468186-82e630d3-8c3c-4c75-8243-e1efcba34926.png" width="220" height="130">|

<br>

<br>

## 7. 유저 가이드

#### 1. 가상환경 설정

python -m venv (가상환경이름)

#### 2. 필요 라이브러리 설치

pip install -r requirments.txt

#### 3. 실행

python manage.py runserver
