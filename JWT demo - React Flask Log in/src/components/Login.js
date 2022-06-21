import { useState } from 'react';
import axios from "axios";
import "../LogIn.css"
function Login(props) {

    const [loginForm, setloginForm] = useState({
      email: "",
      password: ""
    })

    function logMeIn(event) {
      axios({
        method: "POST",
        url:"/token",
        data:{
          email: loginForm.email,
          password: loginForm.password
         }
      })
      .then((response) => {
        props.setToken(response.data.access_token)
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      })

      setloginForm(({
        email: "",
        password: ""}))

      event.preventDefault()
    }

    function handleChange(event) {
      const {value, name} = event.target
      setloginForm(
        prevNote => {
          return   {...prevNote, [name]: value}
        }
      )
    }

    return (
      <div class="login-page">
        <div class="form">
          <form class="login-form">
            <input onChange={handleChange}
                  type="email"
                  text={loginForm.email}
                  name="email"
                  placeholder="Email"
                  value={loginForm.email} />
            <input onChange={handleChange}
                  type="password"
                  text={loginForm.password}
                  name="password"
                  placeholder="Password"
                  value={loginForm.password} />
            <button onClick={logMeIn}>login</button>
            <p class="message">Not registered? <a href="#">Create an account</a></p>
          </form>
        </div>
      </div>
    );
}

export default Login;
