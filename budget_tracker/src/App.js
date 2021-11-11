import './App.css';
import LoginPage from './pages/login-page';
import {
  Routes,
  Route
} from "react-router-dom";
import DashboardPage from './pages/dashboard';
import { useState } from 'react';

function App() {
  
  const [userInfor, setUserInfor] = useState(null);
  
  return (
    <div className="App">
     <Routes>
        <Route path="/" exact element={<LoginPage userInfor={userInfor} setUserInfor={setUserInfor}/>}/>
        <Route path="/dashboard" element={<DashboardPage/>}/>
      </Routes>
    </div>
  );
}

export default App;
