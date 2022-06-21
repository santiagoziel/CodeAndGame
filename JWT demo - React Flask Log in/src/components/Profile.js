import { useState } from 'react'
import axios from "axios";

function Profile(props) {

  const [profileData, setProfileData] = useState(null)
  function getData() {
    axios({
      method: "GET",
      url:"/profile",
      headers: {
        Authorization: 'Bearer ' + props.token
      }
    })
    .then((response) => {
      const res =response.data
      if(res.access_token != undefined){
      props.setToken(res.access_token)
    }
      setProfileData(({
        profile_name: res.name,
        about_me: res.about,
        mail: res.email}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

    function logMeOut() {
      // axios({
      //   method: "POST",
      //   url:"/logout",
      // })
      // .then((response) => {
      //    props.rmtoken()
      // }).catch((error) => {
      //   if (error.response) {
      //     console.log(error.response)
      //     console.log(error.response.status)
      //     console.log(error.response.headers)
      //     }
      // })
     props.rmtoken()}

  return (
    <div className="Profile">
        <button onClick={logMeOut}>
            Logout
        </button>
        <p>To get your profile details: </p>
        <button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
              <p>{profileData.mail}</p>
            </div>
        }

    </div>
  );
}

export default Profile;
