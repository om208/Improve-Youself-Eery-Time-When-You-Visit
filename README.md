# Improve-Youself-Eery-Time-When-You-Visit

## You get your answer, just search properly I am updating it time to time

#### Q1. Which image matches the flex layout defined in this style rule?

```css
.container {
  display: flex;
}
.container div:last-child {
  margin-left: auto;
}
```

- [ ] ![A](images/Q1-A.jpg)
- [x]
  ![B](images/Q1-B.jpg)
- [ ] ![C](images/Q1-C.jpg)
- [ ] ![D](images/Q1-D.jpg)

#### Q2. Variables declared with the let keyword have what type of scope?

- [ ] function scope
- [x] block scope
- [ ] inline scope
- [ ] global scope

#### Q3. How to create Pop up React?

```css
.container {
  display: flex;
}
.container div:last-child {
  margin-left: auto;
}
```

#### Q4. How to create Simple Promise?

```css
const functionOfPromise = async () => {
          return await new Promise(async (resolve, reject) => {
            const storageRef = ref(
              storage,
              "filesOfExpenseBill" +
                arrayOfBillFiles[0].lastModified +
                arrayOfBillFiles[0].name
            );

            await uploadBytes(storageRef, arrayOfBillFiles[0]).then(
              (response) => {
                // first level promise
                getDownloadURL(storageRef).then((url) => {
                  // second level promise
                  // resolve();
                  resolve(url);
                });
              }
            );

            console.log("i AM called");
          });
        };

        functionOfPromise().then((response) => {
          console.log("promise Function response ", response);
        });

```

##### this is an example nested Promise.

```css
functionOfPromise().then((response) => {
          console.log("promise Function response ", response);
        });
```

##### and from this line we can resolve get the value of this promise.

##### 1. at which point we want to return a value, at that point called the first function resolved() at that point.

##### 2. this functions means the parameters of callback function of Promise Constructor.

##### 3. also you can use reject() function at a point where it gives an error

##### 4. you can passed any value as parameter in this resloved() or reject() functions.

#### Q5. How to create Promise with mapFunction or loop ?

```css
let arrayOfPromise = [];

// step 1 .
        const functionOfPromise = async (file, i) => {
          return await new Promise((resolve, reject) => {

            const storageRef = ref(
              storage,
              "filesOfExpenseBill" + file.lastModified + file.name
            );

            uploadBytes(storageRef, file).then((response) => {
              // first level promise
              getDownloadURL(storageRef).then((url) => {
                // second level promise
                resolve(url);
              });
            });
          });
        };
// step 2.
        arrayOfBillFiles.map((file, i) => {
          const promiseFunction = functionOfPromise(file, i);
          arrayOfPromise.push(promiseFunction);
        });

// step 3.
        Promise.all(arrayOfPromise).then((response) => {
          console.log("response of Promise.all", arrayOfPromise);
        });

```

- [x] I used the functions of firebase version.9 for saving documents or files in fireStore
