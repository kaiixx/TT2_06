import './App.css';
import LoginPage from './pages/login-page';
import {
  Routes,
  Route,
  Navigate
} from "react-router-dom";
import DashboardPage from './pages/dashboard';
import Dashboard from './components/dashboard';
import ProjectDetailsPage from './pages/project-details';
import { useState } from 'react';

function App() {
  
  const [userInfor, setUserInfor] = useState(null);

  return (
    <div className="App">
     <Routes>
        <Route 
          path="/" 
          exact 
          element={
          userInfor !== null ?
          <Navigate to="/dashboard" /> :
          <LoginPage userInfor={userInfor} setUserInfor={setUserInfor}/>
        }/>
        <Route path="/dashboard" element={<Dashboard/>}/>
        <Route 
        path="/project-details" 
        element={<ProjectDetailsPage/>}/>
      </Routes>
    </div>
  );
}

export default App;
