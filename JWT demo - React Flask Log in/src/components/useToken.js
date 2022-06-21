import { useState } from 'react';
// the reason we are using these funcitons is becouse
//whenever we save the token or we remove it
//that probable means we are changing the status of the page
//we are displaying different info

function useToken() {

  const [token, setToken] = useState(localStorage.getItem('token'));
  console.log(`token variable is set to ${token}`);

  function saveToken(userToken) {
    localStorage.setItem('token', userToken);
    setToken(userToken);
  };

  function removeToken() {
    localStorage.removeItem("token");
    setToken(null);
  }

  return {
    setBanana: saveToken,
    token: localStorage.getItem('token'),
    removeToken
  }

}

export default useToken;
