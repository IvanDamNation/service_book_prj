import React from "react";

import LOGO_MINI1 from '../../public/img/Logotype_accent RGB_1.png';
import LOGO_MINI2 from '../../public/img/Logotype_accent RGB_2.png';
import LOGO_MINI3 from '../../public/img/Logotype_accent RGB_3.png';
import Contacts from "../reusable/Contacts";


const Footer = () => {
    return (
        <div className="footer">
            <ul className="footerContainer">
                <Contacts />
                <li>
                    <img src={LOGO_MINI1} width={100} alt="Logo_mini1" />
                </li>
                <li>
                    <img src={LOGO_MINI2} width={100} alt="Logo_mini2" />
                </li>
                <li>
                    <img src={LOGO_MINI3} width={100} alt="Logo_mini3" />
                </li>
                <li className="footInfo">Мой Силант 2022</li>
            </ul>
        </div>
    );
};

export default Footer;