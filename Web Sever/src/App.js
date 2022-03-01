import React, {useState} from 'react';
import moment from 'moment';

function App() {
  const [nameUser, setName] = useState('');
  const [age, setAge] = useState('');
  const [date, setDate] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [errorMessageName, setErrorMessageName] = useState('');
  const [errorMessageAge, setErrorMessageAge] = useState('');
  const [errorMessageDate, setErrorMessageDate] = useState('');
  const [errorMessagePhone, setErrorMessagePhone] = useState('');
  const [errorMessageEmail, setErrorMessageEmail] = useState('');
  

  function handleSubmit(e) {
    e.preventDefault();

      // NAME
    const regName = /^[a-zA-Z]+[\s]+[a-zA-Z]+$/;
    const checkName = regName.test(nameUser);
    if (!checkName) {
      setErrorMessageName("*Wrong Name");
    } else {
      setErrorMessageName('');
    }
    if (nameUser == 0) {
      setErrorMessageName('*Enter fullname');
    }
    
    
      // AGE
    const regAge = /^[0-9]+$/;
    const checkAge = regAge.test(age);
    if (!checkAge) {
      setErrorMessageAge('*Wrong Age')
    } else {
      setErrorMessageAge('')
    }
    if (age > 50) {
      setErrorMessageAge('*Overage')
    }
    else if (age < 10 && age > 0) {
      setErrorMessageAge('*Underage')
    }
    else if (age == 0) {
      setErrorMessageAge('*Enter age')
    }

      // DATE
    const epochtime = Date.now();
    const OneYear = 31556926;
    const unixTimestamp = moment(date, 'YYYY-MM-DD').unix();
    const getEpochtime = (epochtime/1000) - unixTimestamp;
    const getYear = getEpochtime /  OneYear;
    const years = Math.trunc(getYear);

    if (years != age) {
      setErrorMessageDate('*Date of Birth not related to age');
    }
    else if (getYear == 0) {
      setErrorMessageDate('*Enter Date of Birth')
    }
    else {
      setErrorMessageDate('')
    }
    
    // PHONE
    const regPhone = /^[0-9]{3}-[0-9]{7}/;
    const checkPhone = regPhone.test(phone);
    if (!checkPhone) {
        setErrorMessagePhone('*Wrong Phone no.');
      }else{
        setErrorMessagePhone('');
      }
      if (phone == 0) {
        setErrorMessagePhone('*Enter Phone no.');
      }


      // EMAIL
    const regMail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    const checkMail = regMail.test(email);
    if (!checkMail) {
      setErrorMessageEmail('*Enter your email address in format email@xxx.xxx');
    }else{
        setErrorMessageEmail('');
    }
    if (email == 0) {
      setErrorMessageEmail('*Enter Email');
    }

      //SUBMIT
    if (!checkName || !checkAge || !checkPhone || !checkMail || years != age) { 
      
    }
    else {
      alert('Register Successfully');
    }
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <fieldset>
          <legend >Register</legend>
          <div className="name">
            <label name="fullname">Full name : </label>
            <input name="input_name" type="text" onChange={e => setName(e.target.value)}></input>
            {errorMessageName && <div className="error">{errorMessageName}</div>}
          </div>
          <div className="gender">
            <label name="gender">Gender : </label>
            <select name="input_gender" className="gender_list">
              <option name="choose" value="">Choose Gender</option>
              <option name="female" value="">Female</option>
              <option name="male" value="">Male</option>
              <option name="other" value="">Other</option>
            </select>
          </div>
          <div className="age">
            <label name="age">Age : </label>
            <input name="input_age" type="text" maxLength="2" onChange={e => setAge(e.target.value)}></input>
            {errorMessageAge && <div className="error"> {errorMessageAge}</div>}
          </div>
          <div className="date">
            <label name="date">Date of Birth : </label>
            <input name="input_date" type="date" onChange={e => setDate(e.target.value)}></input>
            {errorMessageDate && <div className="error">{errorMessageDate}</div>}
          </div>
          <div className="phone">
            <label name="phone">Phone No. : </label>
            <input name="input_phone" type="tel" placeholder="0xx-xxxxxxx" maxLength="11"
            onChange={e => setPhone(e.target.value)} ></input>
            {errorMessagePhone && <div className="error">{errorMessagePhone}</div>}
          </div>
          <div className="mail">
            <label name="mail">Email : </label>
            <input name="input_mail" type="text" placeholder="email@xxx.com" 
            onChange={e => setEmail(e.target.value)}></input>
            {errorMessageEmail && <div className="error">{errorMessageEmail}</div>}
          </div>
        </fieldset>
        <button id='submit'>Submit</button>
      </form>
    </div>
  );
}

export default App;