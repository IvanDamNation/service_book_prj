import React from 'react';

import MAIN_LOGO from '../../public/img/logo_main.svg';

import Contacts from '../reusable/Contacts';


const Header = () => {
    return (
        <div className="headerContainer">
            <ul className="headerUp">
                <li className="logo">
                    <img src={MAIN_LOGO} alt="logo_silant" width="400" />
                </li>
                <Contacts />
                <li className="authButton">
                    <button type="submit">Авторизация</button>
                </li>
            </ul>
            <div className="headerDown">
                <h1>Электронная сервисная книжка "Мой Силант"</h1>
            </div>
        </div>
    );
};


export default Header;
