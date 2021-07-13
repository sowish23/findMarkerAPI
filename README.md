# findMarkerAPI
마커인식용 웹앱 API - Django

## Description
openCV 를 이용해 도형인식과 OCR을 도입한 애플리케이션의 API 배포를 위한 코드입니다.

## Environment
개발환경 : macOS

사용언어 : Python3 (Django)

배포환경 : www.pythonanywhere.com

## Prerequisite

Pillow

```pip install pillow```


## APIs

### Post Image
----
  post image to server

* **URL**

  /api/image

* **Method:**

  `POST`
  
*  **URL Params**

   None

* **Data Params**

   `{ image : ImageFILE }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ message : "SUCCESS" }`


* **Sample Call:**

  ```javascript
    axios.post('/api/image/', { image : ImageFILE })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  ```
### Get Image
----
  get last image on server

* **URL**

  /api/image

* **Method:**

  `GET`
  
*  **URL Params**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ```{ images : {
                        id : 1,
                        document : 'images/image.jpg',
                        uploaded_at: '2021-07-13T02:30:53.34OZ'
                     }```


* **Sample Call:**

  ```javascript
    axios.get('/api/image/')
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  ```
  
### Find Marker
----
  find marker Shape and OCR and return address

* **URL**

  /api/address

* **Method:**

  `POST`
  
*  **URL Params**

   None

* **Data Params**

   `{ path : imagePATH }`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ message : "SUCCESS" }`


* **Sample Call:**

  ```javascript
    axios.post('/api/address/', { path : ImagePATH })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  ```
  
### Get Address
----
  get last address info
  
* **URL**

  /api/address

* **Method:**

  `GET`
  
*  **URL Params**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ```{ address : {
                        id : 1,
                        document : 'images/image.jpg',
                        address: '서울특별시 성북구 성북동 13길 3층 사무실'
                     }```


* **Sample Call:**

  ```javascript
    axios.get('/api/address/')
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  ```
