# Improve-Youself-Eery-Time-When-You-Visit

**Writing a code, to solve a problem**
a problem can be small or big

" जर आपल्याकडे एक big problem असेल तर...
........तर त्याला छोट्या छोट्या parts मध्ये divide करा...
..............आता त्या छोट्या छोट्या parts ला solve करा...
....................आणि मग step by step त्याला जोडा...
..........................ओ, शेठ...
................................सापडलं कि उत्तर तुम्हांला...
.......................................चला मग, लागा कमला."

##### You get your answer, just search properly I am updating it time to time

###### Q#. You got a big Project. what to do now ?

- [1]

###### Q1. Which image matches the flex layout defined in this style rule?

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

###### Q2. Variables declared with the let keyword have what type of scope?

- [ ] function scope
- [x] block scope
- [ ] inline scope
- [ ] global scope

###### Q3. How to create Pop up React?

```css
.container {
  display: flex;
}
.container div:last-child {
  margin-left: auto;
}
```

###### Q4. How to create Simple Promise?

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

###### this is an example nested Promise.

```css
functionOfPromise().then((response) => {
          console.log("promise Function response ", response);
        });
```

###### and from this line we can resolve get the value of this promise.

1. at which point we want to return a value, at that point called the first function resolved() at that point.

2. this functions means the parameters of callback function of Promise Constructor.

3. also you can use reject() function at a point where it gives an error

4. you can passed any value as parameter in this resloved() or reject() functions.

###### Q5. How to create Promise with mapFunction or loop ?

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

###### Q5. How to write any Pop-Up / Drawer / Snakbar / Alert or a component or a pice of code with map function ?

1.  If want to create a such type of code or component, write this code out of map function.

    for ex.

```css
//table component start here
<Box component="main" sx={{ flexGrow: 1 }}>
        <Toolbar />
        <ExpenseFormV2 />
        <TableContainer component={Paper}>
          <Table aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Name
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Title
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Location
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Date of Added
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  From
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Till
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Amount
                </TableCell>
                <TableCell align="right" sx={{ textAlign: "center" }}>
                  Status
                </TableCell>
                <TableCell align="right">Edit</TableCell>
                <TableCell align="right">View</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {dataForNormalView && dataForNormalView.length > 0                      // map function starts here
                ? dataForNormalView.map((arrayItem) => {
                    return (
                      <TableRow
                        key={arrayItem.id}
                        sx={{
                          "&:last-child td, &:last-child th": { border: 0 },
                        }}
                      >
                        <TableCell
                          component="th"
                          scope="row"
                          sx={{ textAlign: "center" }}
                        >
                          {arrayItem.name}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.expanceCategory}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.location}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.currentDate}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.selectDate}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.selectDateTill}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.amount}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          {arrayItem.status}
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          <IconButton
                            disabled={
                              arrayItem.status == "Approved" ||
                              arrayItem.status == "reimbursed"
                                ? true
                                : false
                            }
                            // onClick={() => onDroverOpenHandler(arrayItem.id)}
                            onClick={droverOpenFunction}
                          >
                            <SwipeableDrawer                                          // Swipeable drawer code start from here
                              anchor={"right"}
                              // open={openDrover}
                              open={drover && drover}
                              // disableSwipeToOpen={"true"}
                            >
                              <Box
                                sx={{
                                  width:                                                            [
                                    "right" === "top" || "right" === "bottom"                       don`t write this code here becaus on
                                      ? "auto"                                                      click the function or this drawer code runs
                                      : 350,                                                        no. of times equal to the no of iterations
                                }}                                                                  ]
                                role="presentation"
                                // onClick={() => setOpenDrover(!openDrover)}
                              >
                                {/* {console.log("idOfInstanse1", id)} */}
                                <FormFildsForEditForm
                                  idOfInstanse={arrayItem.id}
                                  droverFunction={closedrover}
                                  droverState={drover}
                                />
                              </Box>
                            </SwipeableDrawer>                                            // Swipeable drawer code ends
                            <EditIcon />
                          </IconButton>
                        </TableCell>
                        <TableCell align="center" sx={{ textAlign: "center" }}>
                          <Button
                            variant="outlined"
                            onClick={() => onViewFormHandler(arrayItem.id)}
                          >
                            View
                          </Button>
                        </TableCell>
                      </TableRow>
                    );
                  })
                : ""}
            </TableBody>
          </Table>
        </TableContainer>

        {
           <SwipeableDrawer
                              anchor={"right"}
                              // open={openDrover}
                              open={drover && drover}
                              // disableSwipeToOpen={"true"}
                            >
                              <Box
                                sx={{
                                  width:
                                    "right" === "top" || "right" === "bottom"
                                      ? "auto"
                                      : 350,                                                       }
                                role="presentation"
                                // onClick={() => setOpenDrover(!openDrover)}
                              >
                                {/* {console.log("idOfInstanse1", id)} */}
                                <FormFildsForEditForm
                                  idOfInstanse={arrayItem.id}
                                  droverFunction={closedrover}
                                  droverState={drover}
                                />
                              </Box>
                            </SwipeableDrawer>
        }

        {showViewOnlyForm && (
          <ExpenseFormV2
            viewOnly={true}
            formCloseFunction={setShowViewOnlyForm}
          />
        )}
      </Box>
// Table componentends here
```

##### after writting code after the table component give conditional rendering and pass props according to you.

git add

#### Q6 .How to axcess the child component`s state value in parent component ?

#### or .How to axcess the updated value of child in parent component ?

1.  We can done this by passing a function in child component written in parent component.
2.  We can pass a arrow function also or useState`s function.
3.  and call this function inside child component, if require pass some props in it .

#### Q7. How to make one expression or function like block type as alert in javascript ?

Using Async and await Function.

#### Q8. how to disable the toggle behavior of the mui-check box? we aren't able to click directly on UI its value should be set by Javascript only.

1. we can do this by using only a prop called checked={true or false}
2. we can check or uncheck by setting the prop value we can't do by UI part.
3. our events are triggered but the checkmark is restricted, we can do it by only setting the prop value.

```css
 <div>
      <Checkbox {...label} defaultChecked size="small" />     // this check box worked directly.
      <Checkbox  check={true} />                              // this checked box can`t check directly
    </div>
```

#### Q9. How to googling like senior software enginner? for 10X code writting.

- [x] 1. "exact required keywords" or "exact error message" ................................at last
- [x] 2. site:fireship.io our required query ...............................................at first
- [x] 3. -jquery means -EXCLUDE WORD .......................................................at last
- [x] 4. before:2020 or after:2020 .........................................................at last
- [x] 5. 2013..2015 want content between this date .........................................at last
- [x] 6. *tailwind means *wildcardword .....................................................at last
- [x] 7. site:\*fireship.io -www combine selectors .........................................at last
- [x] 8. :PDF or :image or :filetype .......................................................at last

###### 1. "exact required keywords" or "exact error message"

- if we write exact error message we can get exact google search results which include this exact error or words wrapped inside double quots.
- [] eg.**"**has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource **"**
- and get result exact.

###### 2. site:fireship.io our required query

- we want search results only from specific website then enter the website name after site:nameofwebsite.com and your query
- [] eg. **site:**stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" \*react
- now i get search result only from stackoverflow.com

###### 3. -jquery means -EXCLUDE WORD

- I don`t want a keyword include in my search result use (- operator) -keywordname
- [] eg. site:stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" **-jquery**
- I get result`s exclude jquery

###### 4. before:2020 or after:2020

- want search result`s only after specific date or after the specific date use this operator
- [] eg. site:stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" -jquery **after:2020**

###### 5. 2013..2015 want content between this date

- or want a results between the dates use this operator
- [] eg. site:stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" -jquery **2018..2020**

###### 6. *tailwind means *wildcardword

- we want in result`s this wildcard-word must include
- [] eg. "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" **\*react 18** -jquery

###### 7. site:\*fireship.io -www combine selectors

- we can combine multiple operators
- [] eg. in above examples I use multiple combinations.

###### 8. :PDF or :image or :filetype

- if we want specefic file type use this operator
- [] eg. **:md** react code snippets dsa questions and answers
