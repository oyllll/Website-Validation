# Website Validation 

I have started learning the program by myself. I started with C language, Java, Javascript, HTML, CSS, React JS, Git, and Python. After that, I am interested in Web testing. So I went to learn the Selenium framework and I have built this project for practice.

## Front-end (Web Sever)

- HTML
- CSS
- React JS

<img width="600" alt="web sever" src="https://user-images.githubusercontent.com/96046766/156499895-2b0ecb75-41a4-4f83-bf2d-1654a1dfbe0f.png">

## Web Testing

- Python
- Selenium Framework

<img width="229" alt="result" src="https://user-images.githubusercontent.com/96046766/156500341-7779a7e9-a564-4fad-bf86-74cd8884c374.png">

## Scenario

| TC No.   | Test Description| Step to Reproduce| Test Data| Expected Result| Status | Remark |
|----------|-----------------|------------------|----------|----------------|--------|--------|
| Testcase_01 | Verify content in the webpage should display correctly | - Open browser<br/> - Verify title webpage<br/> - Verify content| Url : http://localhost:3000| 1. “Register”<br/> 2. "Register"<br/> 3. “Full name :”<br/> 4. “Gender”<br/> 5. “Age :”<br/> 6. “Date of Birth”<br/> 7. “Phone No.”<br/> 8. “Email”<br/> 9. “Submit” | PASSED | Done   |
| Testcase_02 | Verify content in the webpage should display correctly | - Open browser<br/> - Verify dropdown button|| 1. "Choose Gender"<br/> 2. “Female”<br/> 3. “Male”<br/> 4. “Other”| PASSED | Done   |
| Testcase_03 | User input valid name should work fine| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be result with correctly that = null| PASSED | Done   |
| Testcase_04 | User input name with number should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John 345<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be text error “*Wrong Name”| PASSED | Done   |
| Testcase_05 | User input name with symbol should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John *=/<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be text error “*Wrong Name”| PASSED | Done   |
| Testcase_06 | User input invalid age should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 9<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be text error “*Underage”                                                                                                                                     | PASSED | Done   |
| Testcase_07 | User input invalid age should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 51<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be text error “*Overage”                                                                                                                                      | PASSED | Done   |
| Testcase_08 | User input age with text should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : ab<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be text error “*Enter age”| PASSED | Done   |
| Testcase_09 | User input invalid date of birth should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 23<br/> Text : 1999-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com| Should be text error “*Date of Birth not related to age”| PASSED | Done   |
| Testcase_10 | User input invalid phone should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : 0123456789<br/> Text : john@gmail.com| Should be text error “*Wrong Phone no.”| PASSED | Done   |
| Testcase_11 | User input phone with text should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : abcdefg<br/> Text : john@gmail.com| Should be text error “*Wrong Phone no.”| PASSED | Done   |
| Testcase_12 | User input mail with symbol should error| - Open browser<br/> - Input text with valid<br/> - Click button| Text : John John<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john==@gmail.com| Should be text error “*Enter your email address in format email@xxx.xxx”| PASSED | Done   |
| Testcase_13 | User input valid all data should work fine| - Open browser<br/> - Input text with valid<br/> - Click Submit  button| Text : John John<br/> Text : 23<br/> Text : 1998-04-20<br/> Text : 012-3456789<br/> Text : john@gmail.com | Should be result with correctly that  “Registered Successfully”| PASSED | Done   |

## Example

![example](https://user-images.githubusercontent.com/96046766/156501394-6cdfc4a1-6f6f-4688-ba63-937f15dd17a6.gif)
