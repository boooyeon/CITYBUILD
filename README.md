<br>

# π° λλ‘μ μ°°λ : μμ±μ¬μ§ κΈ°λ° λμ μ λΉ μΈκ³΅μ§λ₯ μλΉμ€
> 2022.05.23 ~ 2022.06.10<br>
>  *'λλ‘μ μ°°λ'λ AIλ‘ μμ±μ¬μ§ μ λλ‘ μ°¨μ μ λΆμ€ν λμμ μΈμν΄ λλ‘ μ λΉλ₯Ό λλ λμ§νΈ μλΉμ€μλλ€*
<img src="https://user-images.githubusercontent.com/37900424/174465736-cfb7e461-316c-4b9b-8066-9a7ca7c2dbde.png" width="1000" height="352">

## νμ μκ°
- `[K-Digital Training] KT AIVLE SCHOOL μλ£μ`
> κΉλλ(νμ₯), κΆμ€κ²½, κΉλ³΄μ°, μνμ°, μμΈμ, μ΄μνΈ


## λͺ©μ°¨
[1. κ°λ° λ°°κ²½ λ° λͺ©μ ](#1-κ°λ°-λ°°κ²½-λ°-λͺ©μ )

[2. κΈ°λ₯](#2-κΈ°λ₯-λ°-UI/UX)

[3. μλΉμ€ FLOW](#3-μλΉμ€-FLOW)

[4. 3 Tier Architecture](#4-3-Tier-Architecture)

[5. DB μ€κ³](#5-DB-μ€κ³)

[6. κ°λ° νκ²½](#6-κ°λ°-νκ²½)

[7. μ μ  κ°μ΄λ](#7-μ μ -)

***

## 1. κ°λ° λ°°κ²½ λ° λͺ©μ 
> π‘ **'μμ±μ¬μ§κ³Ό AIκΈ°μ μ ν΅ν΄ μμ νκ³  νΈλ¦¬ν λλ‘ νκ²½ μ‘°μ±μ μν΄ κ°λ°νκ² λμλ€.'** νμ¬ μ°¨μ  λΈννμ λν μ§μμ μΈ λ―Έμμ΄ λ°μνκ³  μκ³ , μ΄λ‘ μΈν μ¬κ³  μν μ¦κ°μ λμ λ―Έκ΄ μ ν΄ λ¬Έμ  λ±μ μ¬λ¬ μ΄μκ° μλ€. νμ§λ§, λΈν μ°¨μ μ μ λΉνκΈ° μν μ²λ¦¬ κ³Όμ  μ λΆκ° μμμμΌλ‘ μ§νλκ³  μμ΄μ μΈλ ₯ μμμ΄ λ§μ΄ ν¬μλκ³  μλ€. μ¦, μ°¨μ  λ³΄μμ νμν κΈμ‘μ λΉν΄μ μ ν΄μ§ μμ°μ΄ ν±μμ΄ λΆμ‘±ν μν©μ΄λ€. μ°λ¦¬λ λλ‘μ μ°°λλ₯Ό ν΅ν΄ νΌμ μ°¨μ  νμ νλ‘μΈμ€ μλνλ₯Ό λμν΄ ν¨μ¨μ  μμ° μ§νμΌλ‘ ν λ¬΄μ μ μ κ°μ ν  κ²μ΄λ€.
<br>

#### μ°¨μ  λΈννμ λν μ§μμ μΈ λ―Όμ λ°μ
- `κΈ°μ‘΄ λ³΄μ νν©`
    - λλ‘κ΅ν΅μμ μ κ² κ³νλΆν° μ κ±°λ° κ΅¬μ±, μ°¨μ  μ‘μ μ‘°μ¬, κ²°κ³Ό λΆμ λ° λ³΄κ³  κΉμ§ μ  κ³Όμ μ μμμμΌλ‘ μ²λ¦¬ 
    - μ°¨μ  λ³΄μ μμ° λΆμ‘±
    
- `As-Is`
    - [1λ¨κ³] μ°¨μ μ κ²κ³ν μλ¦½
    - [2λ¨κ³] μλ£μ€λΉ λ° μ κ²μΈλ ₯ κ΅¬μ±
    - [3λ¨κ³] μ°¨μ  μ κ² μ€μ
    - [4λ¨κ³] κ²°κ³Ό λΆμΒ·λ³΄κ³ 
    - [5λ¨κ³] μ λΉΒ·λ³΄μ 
<br>

#### μμ κ°μ μ¬ν­μ **λ³΄μ**νκΈ° μν΄ **λλ‘μ μ°°λ**λ₯Ό κΈ°ν
- `To-Be`
    - [1λ¨κ³] μμ±μ¬μ§κ³Ό AIλ₯Ό νμ©ν λμ μ λΉ μΉμλΉμ€
    - [2λ¨κ³] κ²°κ³Ό λΆμΒ·λ³΄κ³ 
    - [3λ¨κ³] μ λΉΒ·λ³΄μ
<br>

<br>

## 2. κΈ°λ₯ λ° UI/UX
- `μλΉμ€ μ£Όμ κΈ°λ₯`

<details>
  <summary>λ©μΈ νλ©΄</summary>
   <div markdown="1">       
     <br>
     <img src="https://user-images.githubusercontent.com/37900424/174467018-f37d26fe-3b21-409e-9b5d-dea2621ecb01.gif">
     <br>
     <text>β λλ‘μ μ°°λμ ννλ©΄μΌλ‘ νμκ°μκ³Ό λ‘κ·ΈμΈμ ν  μ μλ λ²νΌμ΄ μλ€</text>
   </div>
 </details>

 <details>
    <summary><strong>1) κ³ κ°κ³Ό μλ΄μ¬λ₯Ό μν νμκ°μ/λ‘κ·ΈμΈ</strong></summary>
        <div markdown="1">  
            <h3>π νμκ°μ</h3>
            <img src="https://user-images.githubusercontent.com/37900424/174467780-f2f42839-d1f2-458c-9527-582b938300df.png" width="700" height="412">
            <h3>π λ‘κ·ΈμΈ</h3>
            <img src="https://user-images.githubusercontent.com/37900424/174467802-bd815309-051e-4889-a2be-8fb69dca75f9.png" width="700" height="412">
        </div>
</details>
 
 <details>
  <summary><strong>2) νΌμ μ°¨μ  μμΉ μκ°ν</strong></summary>
   <div markdown="1"> 
    <br>      
     <img src="https://user-images.githubusercontent.com/37900424/174468478-f99a7bce-5950-4271-b960-314a7c6f7091.png" width="700" height="412">
     <br>
     <text>β μ κ³΅ λ°μ΄ν°: νΌμ λλ‘ μμΉμ μλ, κ²½λ, νΌμ μ΄λ―Έμ§, μΈκ·Ό λλ‘λͺ μ£Όμ</text>
   </div>
 </details>
 
 <details>
  <summary><strong>3) μ€μ λ³΄ μ κ³  νκΈ°</strong></summary>
   <div markdown="1">
     <br>      
     <img src="https://user-images.githubusercontent.com/37900424/174468695-62661211-70d1-4c40-8f33-9f63290297fe.png" width="700" height="412">
     <br>
      <text>β μμ± λ΄μ©: μμ  μμ²­ λ΄μ©, μ€μ λ³΄ μ¦κ±° μ¬μ§ μλ‘λ</text>
   </div>
 </details>
 
 <details>
  <summary><strong>4) μ§λ μμΉ μ€ν¬λ©νκΈ°</strong></summary>
   <div markdown="1">  
   <br>     
     <img src="https://user-images.githubusercontent.com/37900424/174468770-863e0584-43f1-4f68-ad68-2367a0ca3144.png" width="700" height="412">
     <br>
     <text>β νΌμ μ°¨μ μ λν΄μ μ€ν¬λ© κΈ°λ₯μ ν΅ν΄ νΉμ  νΌμ λ§μ»€λ₯Ό λ€μλ³΄κΈ°κ° κ°λ₯</text>
   </div>
 </details>
 
 <br>

 - `AI μ£Όμ κΈ°λ₯`
 <details>
    <summary><strong>1) νΌμ λλ‘ νμ§ </strong></summary>
      <img src="https://user-images.githubusercontent.com/37900424/174469009-fd42ae28-2634-47d8-9d22-493780a8faa0.png" width="700" height="412"><br>
      <text>β 2-stage Faster R-CNN νμ΅μ μ΄μ©ν κ°μ²΄(νΌμ λλ‘) νμ§</text>
 </details>
 
  - `νΉλ³ν μΆκ° κΈ°λ₯`
 <details>
    <summary><strong>1) μ€ν¬λ© λ΄μ© μμ νμμΌλ‘ λ³ν </strong></summary><br>
    <text>β νΌμ μ°¨μ μ λν μ λ³΄λ₯Ό μμ νμμΌλ‘ λ°μ μ€λ¬΄μ μ¬μ©ν΄ μλΉμ€ μμ±λ UP!</text>
 </details>


<br>

<br>

## 3. μλΉμ€ FLOW
  - `μ£Όμ κΈ°λ₯ Flow`
![μλΉμ€νλ¦](https://user-images.githubusercontent.com/37900424/174466315-f1d32588-84f8-4c67-b7bb-1bf44e0305de.png)

  - `μλΉμ€ Flow`
![μλΉμ€ FLOW](https://user-images.githubusercontent.com/37900424/174466324-057d2f08-3539-4bc3-aea2-330e66810e9a.png)

<br>

## 4. 2 Tier Architecture
   - `2-Tier Architecture`
![μλΉμ€μν€νμ³](https://user-images.githubusercontent.com/37900424/174466455-ee55f7f7-18fb-4e4d-a7d8-940ca0720763.png)

<br>

## 5. DB μ€κ³
  - `ERD`
![ERD](https://user-images.githubusercontent.com/37900424/174466403-579571a1-58db-4de7-bb6e-67d41857e1e5.png)



<br>

## 6. κ°λ° νκ²½

- `Front-End`

  |HTML|CSS|JS|
  |:---:|:---:|:---:|
  |![html](https://user-images.githubusercontent.com/68097036/151471705-99458ff8-186c-435b-ac5c-f348fd836e40.png)|![css](https://user-images.githubusercontent.com/68097036/151471805-14e89a94-59e8-468f-8192-c10746b93896.png)|![js](https://user-images.githubusercontent.com/68097036/151471854-e0134a79-b7ef-4a0f-99fd-53e8ee5baf50.png)


- `Back-End`

  |Python|Django|PostgreSQL|
  |:---:|:---:|:---:|
  |![pngwing com](https://user-images.githubusercontent.com/68097036/151479684-a85d26d4-e79e-47c9-9023-bf6d92f57536.png)|![pngwing com (1)](https://user-images.githubusercontent.com/68097036/151466729-9cad0405-85ad-454e-815a-1a4fd065f8b7.png)|<img src="https://user-images.githubusercontent.com/37900424/174469395-df3b2796-093b-4069-a376-aa1e3585931e.png" width="220" height="200">|


- `Etc`

  |VS Code|Microsoft Teams|GitHub|Notion|
  |:---:|:---:|:---:|:---:|
  |<img src="https://user-images.githubusercontent.com/68097036/151479933-01785e34-1283-4fca-a407-9fe284b50fa8.png" width="220" height="100">|![pngwing com (4)](https://user-images.githubusercontent.com/68097036/151467837-2cd89acd-2a92-45dd-b06b-e08e316b7695.png)|<img src="https://user-images.githubusercontent.com/68097036/151467910-0fda00cd-c08b-4869-a21e-a66d1d133ff5.png" width="220" height="100">|<img src="https://user-images.githubusercontent.com/68097036/151468186-82e630d3-8c3c-4c75-8243-e1efcba34926.png" width="220" height="130">|

<br>

<br>

## 7. μ μ  κ°μ΄λ

#### 1. κ°μνκ²½ μ€μ 

python -m venv (κ°μνκ²½μ΄λ¦)

#### 2. κ°μνκ²½ μ€ν

source (κ°μνκ²½μ΄λ¦)/bin/activate

#### 3. νμ λΌμ΄λΈλ¬λ¦¬ μ€μΉ

pip install -r requirments.txt

#### 4. μ€ν

python manage.py runserver
