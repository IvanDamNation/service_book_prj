import { useState } from "react";


const AuthForm = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    // const [usernameDirty, setUsernameDirty] = useState(false)
    // const [passwordDirty, setPasswordDirty] = useState(false)
    // const [usernameError, setUsernameError] = useState('Логин не может быть пустым')
    // const [passwordError, setPasswordError] = useState('Пароль не может быть пустым')



    
    return (
        <li>
            <form className="authForm">
                <input className="authInput" type="text" placeholder="Логин"/>
                <input className="authInput" type="password" placeholder="Пароль"/>
                <button type="submit" className="authButton">Вход</button>
            </form>
        </li>
    );
};

export default AuthForm;