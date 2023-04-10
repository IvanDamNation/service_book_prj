import { FC } from "react";

import { NavLink } from "react-router-dom";

const NavAuth: FC = () => {
    return (
        <div className="infoNavContainer">
            <ul className="infoNav">
                <li className="mainInfoBtnWrapper">
                    <NavLink className="mainInfoBtn" to={'/main_info'}>Общая инфо</NavLink>
                </li>
                <li className="mainInfoBtnWrapper">
                    <NavLink className="mainInfoBtn" to={'/maintanence'}>Техобслуживание</NavLink>
                </li>
                <li className="mainInfoBtnWrapper">
                    <NavLink className="mainInfoBtn" to={'/reclamations'}>Рекламации</NavLink>
                </li>
            </ul>
        </div>
    );
}

export default NavAuth;