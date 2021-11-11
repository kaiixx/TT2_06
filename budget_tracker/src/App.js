import './App.css';
import LoginPage from './pages/login-page';
import {
  Routes,
  Route
} from "react-router-dom";
import { useState } from 'react';
import Dashboard from './components/Dashboard';


function App() {
  
  const [userInfor, setUserInfor] = useState(null);
  
  return (
    <div className="App">
     <Routes>
        <Route path="/" exact element={<LoginPage userInfor={userInfor} setUserInfor={setUserInfor}/>}/>
        <Route path="/dashboard" element={<Dashboard/>}/>
      </Routes>
    </div>
  );
}
export default App;
