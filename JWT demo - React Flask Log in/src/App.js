import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './components/Login'
import Profile from './components/Profile'
import useToken from './components/useToken'
import NotFound from './pages/404'
import './App.css'

function App() {
  const { setBanana, removeToken, token} = useToken();
  return (
    <BrowserRouter>
      <div className="App">
        {!token?
              <Login setToken={setBanana} />:
        (<>
            <Routes>
              <Route exact path="/" element={<Profile title="home" rmtoken={removeToken} token={token} setToken={setBanana}/>}></Route>
              <Route exact path="*" element={<NotFound/>} ></Route>
            </Routes>
        </>)}
      </div>
    </BrowserRouter>
  );
}

export default App;
