import logo from './logo.svg';
import './App.css';
import LoginPage from './pages/login-page'

function App() {
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
