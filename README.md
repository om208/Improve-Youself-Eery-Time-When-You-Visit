# Improve-Youself-Eery-Time-When-You-Visit

**Writing a code, to solve a problem**
a problem can be small or big

<!-- " जर आपल्याकडे एक big problem असेल तर...
........तर त्याला छोट्या छोट्या parts मध्ये divide करा...
..............आता त्या छोट्या छोट्या parts ला solve करा...
....................आणि मग step by step त्याला जोडा...
..........................ओ, शेठ...
................................सापडलं कि उत्तर तुम्हांला...
.......................................चला मग, लागा कमला." -->

- " जर आपल्याकडे एक big problem असेल तर...
  - तर त्याला छोट्या छोट्या parts मध्ये divide करा...
    - आता त्या छोट्या छोट्या parts ला solve करा...
      - आणि मग step by step त्याला जोडा...
        - ओ, शेठ...
          - सापडलं कि उत्तर तुम्हांला...
            - चला मग, लागा कमला."

##### You get your answer, just search properly I am updating it time to time

### Q#. You got a big Project. what to do now ?

- 1. first understand the code properly, and make a rough outline of it on paper.
- 2. make a list of all inputs given to the application.
- 3. also make a list of all outputs, the application must give this and that many types of output.
- 4. now understand which types of output and give technical names to them and make a list.
     1. now break this list into small parts means small components.
     2. now again make a list of it.
     3. now think about which part or which view or which functionality is common in multiple components.
     4. now again convent this same code in components.
     5. add this component to the last components list.
- 6. Giving numbering to these components according to complexity means required time to build them.
- 7. Now start constructing one by one component.
     1. pick the first component still is it complex make id divide it into small parts again.
     2. make an outline of this component on paper.
     3. write some algorithums loosely on how you code this component.
- 8. if you do this at last your app is ready to deploy and scale and easy to maintain.

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

- 1.  "exact required keywords" or "exact error message" ................................at last
- 2.  site:fireship.io our required query ...............................................at first
- 3.  -jquery means -EXCLUDE WORD .......................................................at last
- 4.  before:2020 or after:2020 .........................................................at last
- 5.  2013..2015 want content between this date .........................................at last
- 6.  *tailwind means *wildcardword .....................................................at last
- 7.  site: \*fireship.io -www combine selectors ........................................at last
      1. or inurl:fireship.io ...........................................................at any point of query
- 8.  :PDF or :image or filetype:py or filetype:js ......................................at last

###### 1. "exact required keywords" or "exact error message"

- if we write exact error message we can get exact google search results which include this exact error or words wrapped inside double quots.
- eg.
  1. **"**has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource **"**
  2. why I learn python "streaming" -pyAudio
- and get result exact.

###### 2. site:fireship.io our required query

- we want search results only from specific website then enter the website name after site:nameofwebsite.com and your query
- eg. **site:**stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" \*react
- now i get search result only from stackoverflow.com

###### 3. -jquery means -EXCLUDE WORD

- I don`t want a keyword include in my search result use (- operator) -keywordname
- eg. site:stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" **-jquery**
- I get result`s exclude jquery

###### 4. before:2020 or after:2020

- want search result`s only after specific date or after the specific date use this operator
- eg. site:stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" -jquery **after:2020**

###### 5. 2013..2015 want content between this date

- or want a results between the dates use this operator
- eg. site:stackoverflow.com "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" -jquery **2018..2020**

###### 6. *tailwind means *wildcardword

- we want in result`s this wildcard-word must include
- eg. "has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource" **\*react 18** -jquery

#### 7. site:\*fireship.io -www combine selectors

- we can combine multiple operators
- eg. in above examples I use multiple combinations.

#### 8. :PDF or :image or :filetype

- if we want specefic file type use this operator
- eg.

  1. **:md** react code snippets dsa questions and answers
  2. binary search tree filetype:py

- if you click on search results directly .py file is open which is adout binary search tree.

#### Q.10 How to what are the syntaxes of readme.md file? how to make a beautiful ?

Markdown Cheatsheet

---

# Heading 1

    Markup :  # Heading 1 #

    -OR-

    Markup :  ============= (below H1 text)

## Heading 2

    Markup :  ## Heading 2 ##

    -OR-

    Markup: --------------- (below H2 text)

### Heading 3

    Markup :  ### Heading 3 ###

#### Heading 4

    Markup :  #### Heading 4 ####

Common text

    Markup :  Common text

_Emphasized text_

    Markup :  _Emphasized text_ or *Emphasized text*

~~Strikethrough text~~

    Markup :  ~~Strikethrough text~~

**Strong text**

    Markup :  __Strong text__ or **Strong text**

**_Strong emphasized text_**

    Markup :  ___Strong emphasized text___ or ***Strong emphasized text***

[Named Link](http://www.google.fr/ "Named link title") and http://www.google.fr/ or <http://example.com/>

    Markup :  [Named Link](http://www.google.fr/ "Named link title") and http://www.google.fr/ or <http://example.com/>

[heading-1](#heading-1 "Goto heading-1")

    Markup: [heading-1](#heading-1 "Goto heading-1")

Table, like this one :

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |

```
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```

Adding a pipe `|` in a cell :

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | \|            |

```
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  |  \|
```

Left, right and center aligned table

| Left aligned Header | Right aligned Header | Center aligned Header |
| :------------------ | -------------------: | :-------------------: |
| Content Cell        |         Content Cell |     Content Cell      |
| Content Cell        |         Content Cell |     Content Cell      |

```
Left aligned Header | Right aligned Header | Center aligned Header
| :--- | ---: | :---:
Content Cell  | Content Cell | Content Cell
Content Cell  | Content Cell | Content Cell
```

`code()`

    Markup :  `code()`

```javascript
var specificLanguage_code = {
  data: {
    lookedUpPlatform: 1,
    query: "Kasabian+Test+Transmission",
    lookedUpItem: {
      name: "Test Transmission",
      artist: "Kasabian",
      album: "Kasabian",
      picture: null,
      link: "http://open.spotify.com/track/5jhJur5n4fasblLSCOcrTp",
    },
  },
};
```

    Markup : ```javascript
             ```

- Bullet list
  - Nested bullet
    - Sub-nested bullet etc
- Bullet list item 2

```
 Markup : * Bullet list
              * Nested bullet
                  * Sub-nested bullet etc
          * Bullet list item 2

-OR-

 Markup : - Bullet list
              - Nested bullet
                  - Sub-nested bullet etc
          - Bullet list item 2
```

1. A numbered list
   1. A nested numbered list
   2. Which is numbered
2. Which is numbered

```
 Markup : 1. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered
```

- [ ] An uncompleted task
- [x] A completed task

```
 Markup : - [ ] An uncompleted task
          - [x] A completed task
```

- [ ] An uncompleted task
  - [ ] A subtask

```
 Markup : - [ ] An uncompleted task
              - [ ] A subtask
```

> Blockquote
>
> > Nested blockquote

    Markup :  > Blockquote
              >> Nested Blockquote

_Horizontal line :_

---

    Markup :  - - - -

_Image with alt :_

![picture alt](http://via.placeholder.com/200x150 "Title is optional")

    Markup : ![picture alt](http://via.placeholder.com/200x150 "Title is optional")

Foldable text:

<details>
  <summary>Title 1</summary>
  <p>Content 1 Content 1 Content 1 Content 1 Content 1</p>
</details>
<details>
  <summary>Title 2</summary>
  <p>Content 2 Content 2 Content 2 Content 2 Content 2</p>
</details>

    Markup : <details>
               <summary>Title 1</summary>
               <p>Content 1 Content 1 Content 1 Content 1 Content 1</p>
             </details>

```html
<h3>HTML</h3>
<p>Some HTML code here</p>
```

Link to a specific part of the page:

[Go To TOP](#TOP)

    Markup : [text goes here](#section_name)
              section_title<a name="section_name"></a>

Hotkey:

<kbd>⌘F</kbd>

<kbd>⇧⌘F</kbd>

    Markup : <kbd>⌘F</kbd>

Hotkey list:

| Key       | Symbol |
| --------- | ------ |
| Option    | ⌥      |
| Control   | ⌃      |
| Command   | ⌘      |
| Shift     | ⇧      |
| Caps Lock | ⇪      |
| Tab       | ⇥      |
| Esc       | ⎋      |
| Power     | ⌽      |
| Return    | ↩      |
| Delete    | ⌫      |
| Up        | ↑      |
| Down      | ↓      |
| Left      | ←      |
| Right     | →      |

Emoji:

:exclamation: Use emoji icons to enhance text. :+1: Look up emoji codes at [emoji-cheat-sheet.com](http://emoji-cheat-sheet.com/)

    Markup : Code appears between colons :EMOJICODE:

#### Q11. How to update the array of objects in a sequential way?

1. first update the array in normal way.
2. then sort the array and then rerender the component using useEffect`s dependency method.

```css

const [obj,setObj]= useState([]);

const data = [
  { id: 1, car: "Toyota 2020", owner: "BM" },
  { id: 2, car: "Nissan", owner: "DK" },
  { id: 3, car: "Mazda", owner: "JA" },
  { id: 4, car: "Ford", owner: "DS" }
];

const newData = ["Audi", "Bentley", "BMW", "Buick"];

const newCars = data.map((obj, i) => {
  setObj(...obj, car: newData[i])
  });

// For sequential way use useEffects dependency parameterto rerender the component and that sort the data according to need
// this is the best way to do it. in sequential way,
// example in expense report`s pending view manager and HR approving checkbox.

console.log(newCars);
```

#### Q12. How to solve emotion react not found an error ?

- Propery convert the Mui versions from v5 to V4 or V5 to V4.

#### Q13. how to autocomplect the vs code sugession properly in code using ctr + space or ctr + i ?
