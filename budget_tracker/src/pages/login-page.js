import Login from "../containers/login/Login";

function LoginPage({userInfor, setUserInfor}) {
    return (
        <div className="login-page">
             <Login setUserInfor={setUserInfor}/>
        </div>
    );
};

export default LoginPage;
