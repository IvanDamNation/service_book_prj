import React, { useState } from 'react';

import MAIN_LOGO from '../../public/img/logo_main.svg';

import Contacts from '../reusable/Contacts';
import AuthForm from '../reusable/AuthForm';


const Header = () => {
    const [showAuthForm, setshowAuthForm] = useState<boolean>(false)

    return (
        <div className="headerContainer">
            <ul className="headerUp">
                <li className="logo">
                    <img src={MAIN_LOGO} alt="logo_silant" width="400" />
                </li>
                { showAuthForm ? <AuthForm /> : <Contacts />}
                <li className="authButton" hidden={ showAuthForm }>
                    <button onClick={() => setshowAuthForm(!showAuthForm)}>Авторизация</button>
                </li>
            </ul>
            <div className="headerDown">
                <h1>Электронная сервисная книжка "Мой Силант"</h1>
            </div>
        </div>
    );
};


export default Header;
